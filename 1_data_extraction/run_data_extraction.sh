#!/bin/bash

echo "新資料路徑：${NEW_DATA_DIR}"

if [ $(ls ${NEW_DATA_DIR} | wc -l) -eq 0 ]; then
    echo "沒有偵測到新資料。"
    exit 1
else
    echo "有偵測到新資料。"
    ls ${NEW_DATA_DIR}
fi
