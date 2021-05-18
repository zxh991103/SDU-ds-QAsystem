# -*- coding: utf-8 -*-



from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import json
import keras
import codecs
import pickle
import numpy as np
from .utils.processor import Processor
from .utils.models import KbqaModel
from .utils.callbacks import KbqaCallbacks, TaskSwitch
from .utils.metrics import CrfAcc, CrfLoss


def train(args):
    """模型训练流程
    """
    # 环境设置
    os.environ["CUDA_VISIBLE_DEVICES"] = args.device_map if args.device_map != "cpu" else ""
    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)
    with codecs.open(args.config, "r", encoding="utf-8") as f:
        args.config = json.load(f)
    args.data_params = args.config.get("data")
    args.bert_params = args.config.get("bert")
    args.model_params = args.config.get("model")
    # 数据准备
    processor = Processor(args.data_params.get("train_data"), args.bert_params.get("bert_vocab"),
                          args.data_params.get("tag_padding"))
    train_tokens, train_segs, train_labels, train_tags = processor.process(args.data_params.get("train_data"),
                                                                           args.data_params.get("max_len"))

    train_x = [np.array(train_tokens), np.array(train_segs), np.array(train_labels), np.array(train_tags)]
    train_y = None
    if args.data_params.get("dev_data") is not None:
        dev_tokens, dev_segs, dev_labels, dev_tags = processor.process(args.data_params.get("dev_data"),
                                                                       args.data_params.get("max_len"))
        devs = [[np.array(dev_tokens), np.array(dev_segs), np.array(dev_labels), np.array(dev_tags)], None]
    else:
        devs = None
    # 模型准备
    model = KbqaModel(
        bert_config=args.bert_params.get("bert_config"),
        bert_checkpoint=args.bert_params.get("bert_checkpoint"),
        albert=args.bert_params.get("albert"),
        clf_configs=args.model_params.get("clf_configs"),
        ner_configs=args.model_params.get("ner_configs"),
        max_len=args.data_params.get("max_len"),
        numb_labels=processor.numb_labels,
        numb_tags=processor.numb_tags,
        tag_to_id=processor.tag_to_id,
        tag_padding=args.data_params.get("tag_padding"))
    model.build()
    crf_accuracy = CrfAcc(processor.tag_to_id, args.data_params.get("tag_padding")).crf_accuracy
    crf_loss = CrfLoss(processor.tag_to_id, args.data_params.get("tag_padding")).crf_loss
    # 模型基础信息
    bert_type = "ALBERT" if args.bert_params.get("albert") is "True" else "BERT"
    clf_type = args.model_params.get("clf_configs").get("clf_type").upper()
    ner_type = args.model_params.get("ner_configs").get("ner_type").upper() + "-CRF"
    print(model.sy())

