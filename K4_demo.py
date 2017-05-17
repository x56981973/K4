# -*- coding: utf-8 -*-

import time

dic = {}
edges = []

pointNum = 200


def factorial(n):
    ret = 1
    for i in xrange(2, n + 1):
        ret = ret * i
    return ret


def comb(n, m):
    return factorial(n) / (factorial(n - m) * factorial(m))


def initModel():
    global dic
    global edges
    edges = [[0 for i in range(pointNum)] for j in range(pointNum)]
    for a in range(pointNum):
        for b in range(a + 1, pointNum):
            for c in range(b + 1, pointNum):
                for d in range(c + 1, pointNum):
                    dic[getKeyFast(a, b, c, d)] = 0.5 ** 5


def updateAllEdges():
    global edges
    for i in range(pointNum):
        for j in range(i + 1, pointNum):
            updateOneEdge(i, j)


def updateOneEdge(a, b):
    global edges
    blackE = detectAllK4(1, a, b)
    whiteE = detectAllK4(2, a, b)
    if blackE > whiteE:
        color = 2
    else:
        color = 1
    edges[a][b] = color
    updateAllK4(color, a, b)


def updateAllK4(color, a, b):
    global dic
    global edges
    for i in range(pointNum):
        if i != a and i != b:
            for j in range(i + 1, pointNum):
                if j != a and j != b:
                    newE = detectSingleK4(color, a, b, i, j)
                    if newE == 0:
                        key = getKey(a, b, i, j)
                        if dic.get(key) != None:
                            dic.pop(key)
                    else:
                        dic[getKey(a, b, i, j)] = newE


def detectAllK4(color, a, b):
    global edges
    expection = 0
    for i in range(pointNum):
        if i != a and i != b:
            for j in range(i + 1, pointNum):
                if j != a and j != b:
                    expection += detectSingleK4(color, a, b, i, j)
    return expection


def detectSingleK4(color, a, b, c, d):  # a, b为被染色边的两点，c, d为K4的其他两点
    global dic
    global edges
    newExpection = 0
    if dic.get(getKey(a, b, c, d)) != None:
        origin = [color, getEdge(a, c), getEdge(a, d), getEdge(b, c), getEdge(b, d), getEdge(c, d)]
        tmp = filter(lambda e: e != 0, origin)
        if len(set(tmp)) <= 1:
            newExpection = 0.5 ** (6 - len(tmp))

    return newExpection


def getKey(a, b, c, d):
    x = [a, b, c, d]
    x.sort()
    key = '{0},{1},{2},{3}'.format(x[0], x[1], x[2], x[3])
    return key


def getKeyFast(a, b, c, d):
    return '{0},{1},{2},{3}'.format(a, b, c, d)


def getEdge(a, b):
    global edges
    x = [a, b]
    x.sort()
    return edges[x[0]][x[1]]


startTime = time.time()
print 'upper limit = ', comb(pointNum, 4)

initModel()
updateAllEdges()

print 'Count: ', len(dic)
print "Time used: ", time.time() - startTime
