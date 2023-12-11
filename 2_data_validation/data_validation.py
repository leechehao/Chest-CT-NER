import os
import sys

import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError


NEW_DATA_DIR = os.getenv("NEW_DATA_DIR")


def main():
    with open("2_data_validation/schema.json") as file:
        schema =json.load(file)

    for file_name in os.listdir(NEW_DATA_DIR):
        file_path = os.path.join(NEW_DATA_DIR, file_name)
        if not os.path.isfile(file_path):
            continue
        print(f"驗證 {file_name} 資料中...")
        with open(file_path) as file:
            json_data = json.load(file)
            for i, instance in enumerate(json_data):
                try:
                    validate(instance=instance, schema=schema)
                except ValidationError as e:
                    print(f"第{i}筆 JSON data 無效 >_<")
                    print("Error message:", e.message)
                    sys.exit(1)
            print(f"恭喜 {file_name} 資料有效 ^_^")


if __name__ == '__main__':
    main()
