#!/bin/bash

echo "新資料路徑：$NEW_DATA_DIR"

files=$(find "$NEW_DATA_DIR" -maxdepth 1 -type f -exec basename {} \;)

if [ -n "$files" ]; then
    echo "有偵測到新資料:"
    echo "$files"
else
    echo "沒有偵測到新資料"
    exit 1
fi