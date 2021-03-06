from py2neo import Graph, Node, Relationship

g = Graph(
    host="121.5.144.6",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
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

ns = nodelist()
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
    n1 = np.zeros(163)
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


def answer(question):
    from _1_dataprocess.data2dict import nodelist, nodeid

    ns = nodelist()
    nid = nodeid()

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
    k1 = ''

    k2 = ''

    min2 = 9999

    for j in range(3):
        for i in questionformat[j]:
            if i in question:
                t = Levenshtein.distance(question, i)
                if t < min2:
                    min2 = t
                    k2 = questionlabel[j]
    min1 = 9999

    for i in ns:
        if i in question:
            t = Levenshtein.distance(question, i)
            if t < min1:
                min1 = t
                k1 = i

    if min1 == 9999 or min2 == 9999:
        print('use  nn')
        res, clf = pre(question)
        print('nn:{},{}'.format(res, clf))
        if res == "noa":
            return "no answer"

        maxl = 0
        k1 = res
        v1 = makesenv(res)

        if np.linalg.norm(v1) == 0:

            vpy = getpy(res)
            print('pinyin:{}'.format(vpy))
            minl = 9999

            for i in ns:
                v2py = getpy(i)

                t = Levenshtein.distance(vpy, v2py)
                if t < minl:
                    minl = t
                    k1 = i


        else:
            print('use word vector')
            for i in ns:
                v2 = makesenv(i)
                t = cosin(v1, v2)
                if t > maxl:
                    k1 = i
                    maxl = t
        res = k1
    else:
        print('use regular')
        res, clf = k1, k2
        print('regular:{},{}'.format(res, clf))

    sqls = "MATCH (n) where n.id = {} return n.{}"
    reid = nid[res]

    qtype = {
        'concept': 'desc',
        'reason': 'importres',
        'codes': 'code'
    }
    result = k1
    gd = g.run(sqls.format(reid, qtype[clf])).data()

    for i in gd[0]:
        result = result + "</br>" + i + "</br>" + gd[0][i]
    return result


