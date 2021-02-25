CONFIG_FILE="train_config.json"
SAVE_PATH="../../_4_model/models"

python run_train.py \
    -config ${CONFIG_FILE} \
    -save_path ${SAVE_PATH} \
    -device_map "2"
