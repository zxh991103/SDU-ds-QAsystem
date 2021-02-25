MODEL_DIR="../../_4_model/models"


python run_deploy.py \
    -model_configs ${MODEL_DIR}/model_configs.json \
    -log_path deploy_log/ \
    -device_map "cpu"
