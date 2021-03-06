MODEL_DIR="/Users/admin/Desktop/qaresult/model/albert_base_/textcnn_idcnn"


python run_deploy.py \
    -model_configs ${MODEL_DIR}/model_configs.json \
    -log_path deploy_log/ \
    -device_map "cpu"
