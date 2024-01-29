import os

import mlflow
import yaml


mlflow.set_tracking_uri(os.getenv("TRACKING_URI"))  # os.getenv("TRACKING_URI") http://192.168.1.76:9487
client = mlflow.MlflowClient()
model_name = os.getenv("REGISTERED_MODEL_NAME")  # os.getenv("REGISTERED_MODEL_NAME") chest-ct-ner

registered_model = client.get_registered_model(model_name).latest_versions[0]

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

config["run_id"] = registered_model.run_id

with open("config.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)
