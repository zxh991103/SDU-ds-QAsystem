import codecs
import json
import random

from _1_dataprocess.data2dict import nodelist

nlist = []

for i in nodelist():
    nlist.append(i)

questionformat = [["{}是什么？", "什么是{}?", "{}的概念是什么？", "{}的含义是什么？",
                   "{}什么意思？", "怎么学{}?", "如何学习{}?", "{}是啥？"
                      , "啥是{}?", "{}是？"
                   ],
                  ["为什么引入{}?", "{}有什么用？", "{}什么用？", "{}的原因是？",
                   "{}的成因是？", "为啥{}?", "为啥有{}?", "为何有{}?", "{}的情形是什么？"
                      , "有{}的理由是什么？"
                   ],
                  ["怎么做{}?", "如何实现{}？", "{}怎么写？", "怎么写{}代码？"
                      , "{}代码？", "{}如何做？", "在语言下{}如何做？"
                      , "怎么完成{}任务？", "做{}需要写什么？", "如何写{}？"
                   ]
                  ]

questionlabel = ['concept', 'reason', 'codes']

data = []
devdata = []
for i in nlist:
    for j in range(3):
        for k in questionformat[j]:
            t = []
            s1 = ""
            s2 = ""
            s3 = ""

            s1 = k.format(i)

            s2 = questionlabel[j]

            for p in k:
                if p == '{':
                    ct = 0
                    for q in i:
                        if ct == 0:
                            s3 = s3 + "B-title "
                            ct += 1
                        else:
                            s3 = s3 + "I-title "
                            ct += 1
                else:

                    if p == '?' or p == '？':
                        s3 = s3 + "O"
                    else:
                        if p != '}':
                            s3 = s3 + "O "

            t.append(s1)
            t.append(s2)
            t.append(s3)
            if random.randint(1, 10) % 9 == 0:
                devdata.append(t)
            else:
                data.append(t)
with codecs.open("train_data.txt", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
with codecs.open("dev_data.txt", "w", encoding="utf-8") as f:
    json.dump(devdata, f, ensure_ascii=False, indent=4)

print(len(data))
print(len(devdata))
