import os
import json

import mlflow
import yaml


mlflow.set_tracking_uri(os.getenv("TRACKING_URI"))
client = mlflow.MlflowClient()
experiment_id = client.get_experiment_by_name(os.getenv("EXPERIMENT_NAME")).experiment_id
all_runs = mlflow.search_runs(experiment_id)

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

run_name = config["trainer"]["logger"]["run_name"]
re_train_runs = all_runs[all_runs["tags.mlflow.runName"] == run_name]
best_run = re_train_runs.loc[re_train_runs["metrics.test_f1"].idxmax()]

with open("score.json", "r") as file:
    score_json = json.load(file)

if best_run["metrics.test_f1"] > score_json[0]["test_f1"]:
    mlflow.register_model(f"runs:/{best_run['run_id']}/onnx_model", os.getenv("EXPERIMENT_NAME"))
else:
    print("本次自動訓練沒有得到更好的模型")
