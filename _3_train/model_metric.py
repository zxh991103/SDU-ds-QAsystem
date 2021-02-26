# -*- coding: utf-8 -*-

"""
@Author: Shaoweihua.Liu
@Contact: liushaoweihua@126.com
@Site: github.com/liushaoweihua
@File: run_deploy.py
@Time: 2020/3/16 3:33 PM
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import sys

sys.path.append("../..")

import os
import json
import keras
import codecs
import pickle
import numpy as np
import tensorflow as tf


from _3_train.keras_bert_kbqa.predict import predict
from _3_train.keras_bert_kbqa.utils.tokenizer import Tokenizer


model_configsd = {}

model_configss = [
    "/Users/admin/Desktop/qaresult/model/albert_base_/textcnn_idcnn/model_configs.json"
]


def run_deploy(model_configs):
    # 基础配置

    os.environ["CUDA_VISIBLE_DEVICES"] = 'cpu'
    sess = tf.Session()
    graph = tf.get_default_graph()
    keras.backend.set_session(sess)
    # 属性设置
    with codecs.open(model_configs, "r", encoding="utf-8") as f:
        model_configs = json.load(f)
    tokenizer = Tokenizer(model_configs.get("bert_vocab"))
    max_len = model_configs.get("max_len")
    tag_padding = model_configs.get("tag_padding")
    with codecs.open(model_configs.get("id_to_label"), "rb") as f:
        id_to_label = pickle.load(f)
    with codecs.open(model_configs.get("id_to_tag"), "rb") as f:
        id_to_tag = pickle.load(f)
    model = predict(model_configs.get("model_path"))
    # 新增属性

    model_configsd["tokenizer"] = tokenizer
    model_configsd["max_len"] = max_len
    model_configsd["tag_padding"] = tag_padding
    model_configsd["id_to_label"] = id_to_label
    model_configsd["id_to_tag"] = id_to_tag
    model_configsd["model"] = model

    return graph, sess





def parse(graph,sess,text):
    # 编码
    text = text[:model_configsd["max_len"]]
    token, seg = model_configsd["tokenizer"].encode(text, first_length=model_configsd["max_len"])


    with graph.as_default():
        keras.backend.set_session(sess)
        clf_pred, ner_pred = model_configsd["model"].predict([[token], [seg]])
        clf_res = model_configsd["id_to_label"][np.argmax(clf_pred)]
        ner_pred = [model_configsd["id_to_tag"][item] for item in np.argmax(ner_pred, axis=-1)[0]]
        ner_res = get_entity(text, ner_pred)
        if len(ner_res)==0:
            nres = ''
        else:
            if len(ner_res[0]) < 2:
                nres = ''
            else:
                nres = ner_res[0][1]
        return clf_res,nres


def get_entity(text, tokens):
    """获取ner结果
    """
    # 如果text长度小于规定的max_len长度，则只保留text长度的tokens
    text_len = len(text)
    tokens = tokens[:text_len]

    entities = []
    entity = ""
    for idx, char, token in zip(range(text_len), text, tokens):
        if token.startswith("O") or token.startswith(model_configsd["tag_padding"]):
            token_prefix = token
            token_suffix = None
        else:
            token_prefix, token_suffix = token.split("-")
        if token_prefix == "S":
            entities.append([token_suffix, char])
            entity = ""
        elif token_prefix == "B":
            if entity != "":
                entities.append([tokens[idx - 1].split("-")[-1], entity])
                entity = ""
            else:
                entity += char
        elif token_prefix == "I":
            if entity != "":
                entity += char
            else:
                entity = ""
        else:
            if entity != "":
                entities.append([tokens[idx - 1].split("-")[-1], entity])
                entity = ""
            else:
                continue

    return entities






def metric():
    print('----')
    graph, sess = run_deploy(model_configss[0])
    res = parse(graph,sess,"什么是数据结构？")

    return res



print(metric())
