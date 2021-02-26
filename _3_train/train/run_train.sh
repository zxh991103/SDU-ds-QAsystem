CONFIG_FILE="train_config.json"
mkdir "/Users/admin/Desktop/qaresult/model/albert_base_/dense_bilstm"
SAVE_PATH="/Users/admin/Desktop/qaresult/model/albert_base_/densen_bilstm"
python run_train.py \
    -config ${CONFIG_FILE} \
    -save_path ${SAVE_PATH} \
    -device_map "2"