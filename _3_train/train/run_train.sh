CONFIG_FILE="train_config.json"
mkdir "/Users/admin/Desktop/qaresult/model/albert_base_/textcnn_idcnn"
SAVE_PATH="/Users/admin/Desktop/qaresult/model/albert_base_/textcnn_idcnn"
python run_train.py \
    -config ${CONFIG_FILE} \
    -save_path ${SAVE_PATH} \
    -device_map "2"
