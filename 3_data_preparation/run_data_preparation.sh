#!/bin/bash

# 拉取舊資料
dvc pull

new_dataset_list=''

# 遍歷新資料
for file in "$NEW_DATA_DIR"/*
do
    # 檢查是否為檔案
    if [ -f "$file" ]
    then
        # 從檔案路徑中提取檔案名稱，去除路徑和副檔名
        basename=$(basename "$file")
        filename=${basename%.*}

        # 執行 python 腳本，並將檔案位置作為參數
        if ! python 3_data_preparation/data_preparation.py \
        --input_file "$file" \
        --field_name sentence \
        --output_dir ./"$PROJECT_NAME"/program_data/"$filename"; then
            echo "===== 建立 $filename 資料集失敗 >_< ====="
            continue
        fi

        # 複製 load_dataset_script.py 到新資料集
        cp ./"$PROJECT_NAME"/program_data/"$PROJECT_NAME"/"$PROJECT_NAME".py \
        ./"$PROJECT_NAME"/program_data/"$filename"/"$filename".py

        # 複製 new_data 到 raw_data
        cp "$file" ./"$PROJECT_NAME"/raw_data/

        new_dataset_list+="$filename "
        echo "===== 成功建立 $filename 資料集 ^_^ ====="
    fi
done

dvc add ./"$PROJECT_NAME"
dvc push

git config --global user.name "bryant"
git config --global user.email "leehao90301@gmail.com"
git checkout -b pipeline
git add --all
git commit -m "[Add] 新增 $new_dataset_list 資料集"
git checkout main
git merge pipeline --no-ff
git push http://$GITEA_CRED@${GIT_URL#http://} main
git branch -d pipeline
