# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import warnings

warnings.filterwarnings('ignore')
import sys

sys.path.append("../..")

import os
import json
import keras
import codecs
import pickle
import numpy as np
import tensorflow as tf
import random
from _3_train.keras_bert_kbqa.predict import predict
from _3_train.keras_bert_kbqa.utils.tokenizer import Tokenizer

model_configsd = {}

basepath = '/Users/admin/Desktop/qaresult/model/{}/model_configs.json'


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


def parse(graph, sess, l1):
    # 编码
    resclf = []
    resner = []
    for text in l1:
        text = text[:model_configsd["max_len"]]
        token, seg = model_configsd["tokenizer"].encode(text, first_length=model_configsd["max_len"])

        with graph.as_default():
            keras.backend.set_session(sess)
            clf_pred, ner_pred = model_configsd["model"].predict([[token], [seg]])
            clf_res = model_configsd["id_to_label"][np.argmax(clf_pred)]
            ner_pred = [model_configsd["id_to_tag"][item] for item in np.argmax(ner_pred, axis=-1)[0]]
            ner_res = get_entity(text, ner_pred)

            if len(ner_res) == 0:
                nres = ''
            else:
                if len(ner_res[0]) < 2:
                    nres = ''
                else:
                    nres = ner_res[0][1]
            resner.append(ner_pred)
            resclf.append(clf_res)

    return resclf, resner


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


def accclf(l1, l2):
    if len(l1) != len(l2):
        print('do not match')
        return
    s = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            s += 1
    return s / len(l1)


def checklist(l1, l2):
    r = 0
    len1 = min(len(l1), len(l2))
    for i in range(len1):
        if l1[i] != l2[i]:
            r += 1
    return 1.0 - r / len(l1)


def accner(l1, l2):
    s = 0
    if len(l1) != len(l2):
        print('do not match')
        return
    for i in range(len(l1)):
        s += checklist(l1[i], l2[i])

    return s / len(l1)


def r12(l1):
    r1 = random.randint(0, l1)
    while 1:
        r2 = random.randint(0, l1)
        if r2 != r1:
            break
    return min(r1, r2), max(r1, r2)


def metric():
    with codecs.open("../_2_traindataProcess/test_data.txt", "r", encoding="utf-8") as f:
        data = json.load(f)

    n1 = []
    tclf = []
    tner = []
    for i in data:
        n1.append(i[0])
        tclf.append(i[1])
        tner.append(i[2].split(' '))
        len1 = len(i[0])
        rk1, rk2 = r12(len1)
        n1.append(i[0][rk1:rk2])
        tclf.append(i[1])
        tner.append(i[2].split(' ')[rk1:rk2])

    res = {}
    paths = {}
    dirlist = os.listdir('/Users/admin/Desktop/qaresult/model')
    cnt = 0
    for i in dirlist:
        if '.' not in i:
            dir2 = os.listdir('/Users/admin/Desktop/qaresult/model/' + i)
            for j in dir2:
                if '.' not in j:
                    paths[i + '/' + j] = cnt
            cnt += 1

    for i in paths:

        graph, sess = run_deploy(basepath.format(i))
        resclf, resner = parse(graph, sess, n1)
        print(i)
        rc = accclf(resclf, tclf)
        rn = accner(resner, tner)
        print(rc)
        print(rn)
        res[i] = {
            'resclf': rc,
            'resner': rn
        }
        del graph
        del sess
        del resner
        del resclf
        del rc
        del rn

    return res


res = metric()

with open('metric_result.py', 'w+') as f:
    print(res, file=f)
