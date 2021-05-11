from py2neo import Graph, Node, Relationship

g = Graph(
    host="139.224.63.113",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
    http_port=7474,  # neo4j 服务器监听的端口号
    user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
    password="2021sdu")

from _4_predict.preapi import pre
import Levenshtein


def createdict(l):
    d1 = {}
    for i in l:
        for j in i:
            d1[j] = 0
    res = []
    for i in d1:
        res.append(i)
    return res


from _1_dataprocess.data2dict import nodelist, nodeid

import numpy as np
import csv
data = []
with open('node_all.txt', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        data.append(row[0].lower())
ns = data

# ns = nodelist()
nid = nodeid()
allchar = createdict(ns)

allno = [i for i in range(len(allchar))]

allno = np.array(allno).reshape(len(allno), -1)
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder()
enc.fit(allno)
allarray = enc.transform(allno).toarray()

worddic = {}

for i in range(len(allarray)):
    worddic[allchar[i]] = allarray[i]


def makesenv(s):
    n1 = np.zeros(289)
    for i in s:
        if i in worddic:
            n1 += np.array(worddic[i])
    k2 = np.linalg.norm(n1)
    if k2 == 0:
        return n1
    return n1 / k2


def cosin(v1, v2):
    cos_ = np.dot(v1, v2)
    return cos_


def getpy(word):
    import pypinyin
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


def pretype(question):
    r1 = 'concept'
    questionformat = [["是什么", "什么是", "概念？", "含义",
                       "什么意思", "怎么学", "如何学习", "是啥"
                          , "啥是"
                       ],
                      ["为什么", "有什么用", "什么用", "原因",
                       "成因", "为啥", "为啥有", "为何有", "情形"
                          , "理由"
                       ],
                      ["怎么做", "如何实现", "怎么写", "代码"
                          , "代码", "如何做", "语言"
                          , "完成", "写", "如何写"
                       ]
                      ]
    questionlabel = ['concept', 'reason', 'codes']
    min2 = 9999

    for j in range(3):
        for i in questionformat[j]:
            if i in question:
                t = Levenshtein.distance(question, i)
                if t < min2:
                    min2 = t
                    r1 = questionlabel[j]

    nres = 'notnn'
    if min2 == 9999:
        t1, t2 = pre(question)
        r1 = t2

        if len(t1) == 0:
            nres = 'noa'
        else:
            nres = t1[0][1]
        print("use nn for clf " + r1 + ' ' + str(t1))
    else:
        print("use regular for clf " + r1)

    return r1 , nres


def preentity(question,nner):
    k1 = 'noa'

    min1 = 9999

    for i in ns:
        if i == question:
            return i
        if i in question:
            t = Levenshtein.distance(question, i)
            print(question,i,t)
            if t < min1:
                min1 = t
                k1 = i
                print(k1)
    if min1 == 9999:
        if nner == "notnn":
            t1 , t2 = pre(question)
            print("for ner first use nn! and nn preedict is "+ str(t1))
            if len(t1) == 0:
                nner = 'noa'
            else:
                nner = t1[0][1]
        else:
            print("Already use nn! and nn predict is " + nner)
        if nner == "noa":
            return k1
        else:
            min2 = 9999
            for i in ns:
                if i == nner:
                    return i
                if nner in i:
                    t = Levenshtein.distance(question, i)
                    print(nner, i, t)
                    if t < min1:
                        min2 = t
                        k1 = i
                        print(k1)
            if min2 == 9999:
                maxl = 0
                k1 = nner
                v1 = makesenv(nner)

                if np.linalg.norm(v1) == 0:

                    vpy = getpy(nner)
                    minl = 9999

                    for i in ns:
                        v2py = getpy(i)
                        t = Levenshtein.distance(vpy, v2py)
                        if t < minl:
                            minl = t
                            k1 = i
                    print("use nn + pinyin + edit for ner " + k1)
                else:
                    for i in ns:
                        v2 = makesenv(i)
                        t = cosin(v1, v2)
                        if t > maxl:
                            k1 = i
                            maxl = t
                    print("use nn + onehot vector for ner " + k1)
            else:
                print("use nn + regular for ner" + k1)
    else:
        print("use regualr for ner " + k1)
    return k1



def answer(question):
    hello = ['你好！','hello!','hi!','早上好！','中午好！','晚上好！']
    for i in hello:
        if question.lower() in i or i in question.lower():
            return i



    question = question.lower()
    print(question)
    nid = nodeid()
    print("----------calculate question type----------")
    clf , nnres = pretype(question)
    print("----------calculate question entity----------")
    ner = preentity(question,nnres)
    print("----------calculate END----------")

    if ner == 'noa':
        return "你说什么我听不懂呐！"+"</br>"+"请换个问法。"



    if ner in nid:
        sqls = "MATCH (n) where n.id = {} return n.{}"
        reid = nid[ner]

        qtype = {
            'concept': 'desc',
            'reason': 'importres',
            'codes': 'code'
        }

        result = ner

        gd = g.run(sqls.format(reid, qtype[clf])).data()
        print('recall:------------')
        print(gd)
        print('recallend:------------')
        for i in gd[0]:
            result =gd[0][i]

    else:
        result = ner + "</br>" + clf
    print(result)
    return result





