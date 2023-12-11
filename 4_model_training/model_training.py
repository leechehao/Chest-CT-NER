import os

import mlflow
import yaml


mlflow.set_tracking_uri(os.getenv("TRACKING_URI"))  # os.getenv("TRACKING_URI") "http://192.168.1.76:9527"
client = mlflow.MlflowClient()
model_name = os.getenv("PROJECT_NAME")  # os.getenv("PROJECT_NAME") chest_ct_ner

registered_model = client.get_registered_model(model_name).latest_versions[0]
config_path = mlflow.artifacts.download_artifacts(run_id=registered_model.run_id, artifact_path="config.yaml", dst_path=".")

with open(config_path, "r") as file:
    config = yaml.safe_load(file)

config["dataset"]["dataset_name"] = []
config["trainer"]["logger"]["run_name"] = f"re-train-version_{registered_model.version}"

program_data_dir = f"./{os.getenv('PROJECT_NAME')}/program_data"
# program_data_dir = "./chest_ct_ner/program_data"

for dataset_name in os.listdir(program_data_dir):
    dataset_path = os.path.join(program_data_dir, dataset_name)
    config["dataset"]["dataset_name"].append(dataset_path)

with open(config_path, "w") as file:
    yaml.dump(config, file, default_flow_style=False)
