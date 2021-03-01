CONFIG_FILE="train_config.json"
mkdir "/Users/admin/Desktop/qaresult/model/chinese_wwm_ext_L-12_H-768_A-12_/dense_idcnn"
SAVE_PATH="/Users/admin/Desktop/qaresult/model/chinese_wwm_ext_L-12_H-768_A-12_/dense_idcnn"
echo "/Users/admin/Desktop/qaresult/model/chinese_wwm_ext_L-12_H-768_A-12_/dense_idcnn"


python run_train.py \
    -config ${CONFIG_FILE} \
    -save_path ${SAVE_PATH} \
    -device_map "2"