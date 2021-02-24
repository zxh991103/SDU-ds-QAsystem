import os


def nodedict():
    resdict = {}
    with open("node.txt") as f:
        ll = [[], [], [], [], [], []]
        for i in f:
            ss = i.split(' ')
            level = len(ss[0])
            datas = ss[1].split('\n')[0]
            ll[level - 1].append(datas)
            if level == 1:
                continue
            else:
                resdict[datas] = ll[level - 2][len(ll[level - 2]) - 1]
    return resdict


def nodelist():
    reslist = {}
    with open("node.txt") as f:
        for i in f:
            ss = i.split(' ')
            datas = ss[1].split('\n')[0]
            level = len(ss[0])
            reslist[datas] = "k{}".format(level)
    return reslist


def nodeid():
    idlist = {}
    cnt = 0
    with open("node.txt") as f:
        for i in f:
            ss = i.split(' ')
            datas = ss[1].split('\n')[0]
            idlist[datas] = cnt
            cnt += 1
    return idlist

def nodedesc():
    nodedescp={}

    for i in nodelist():
        nodedescp[i]='desc'
    return nodedescp


def nodecode():
    nodecodes = {}

    for i in nodelist():
        nodecodes[i] = 'code'
    return nodecodes

def noderes():
    noderesn={}
    for i in nodelist():
        noderesn[i] = 'reson'
    return noderesn
