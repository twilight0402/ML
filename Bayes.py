import numpy as np

def loadDataSet():
    """
    创建数据集
    :return: 文档列表 docList, 所属类别classVec
    """
    docList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return docList, classVec


def createVocabList(docList):
    """构造词汇表，统计所有文本中的所有单词
    :return list 去重的词汇表
    """
    vocalSet = set([])
    for line in docList:
        vocalSet = vocalSet | set(line)     # 集合求并集操作
    return list(vocalSet)


def setOfWords2Vec(vocabList, inputSet):
    """将输入数据转换为向量.存在这个单词记为1，不存在则记为0"""
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    """分类器训练函数"""
    numberOfAttr = len(trainMatrix[0])
    numbrOfDoc = len(trainMatrix)
    p0 = np.zeros((1, numberOfAttr))                # p(wi|c0)
    p1 = np.zeros((1, numberOfAttr))                # p(wi|c1)
    p0Total = 0.0
    p1Total = 0.0
    pc1 = float(sum(trainCategory)) / numbrOfDoc          # p(c1)

    for i in range(numbrOfDoc):
        if trainCategory[i] == 0:
            p0 += trainMatrix[i]
            p0Total += sum(trainMatrix[i])
        else:
            p1 += trainMatrix[i]
            p1Total += sum(trainMatrix[i])

    # print("p0Total:", p0Total)
    # print("p1Total:", p1Total)
    # print("p0:", p0)
    # print("p1:", p1)

    p0 = p0 / p0Total
    p1 = p1 / p1Total

    return p0, p1, pc1


def trainNB1(trainMatrix, trainCategory):
    """分类器训练函数"""
    numberOfAttr = len(trainMatrix[0])
    numbrOfDoc = len(trainMatrix)
    p0 = np.ones((1, numberOfAttr))                # p(wi|c0)
    p1 = np.ones((1, numberOfAttr))                # p(wi|c1)
    p0Total = 2.0                                   # 不唯一
    p1Total = 2.0
    pc1 = float(sum(trainCategory)) / numbrOfDoc          # p(c1)

    for i in range(numbrOfDoc):
        if trainCategory[i] == 0:
            p0 += trainMatrix[i]
            p0Total += sum(trainMatrix[i])
        else:
            p1 += trainMatrix[i]
            p1Total += sum(trainMatrix[i])

    p0 = np.log(p0 / p0Total)
    p1 = np.log(p1 / p1Total)

    return p0, p1, pc1


def classifyNB(inputData, p0, p1, pc1):
    """使用计算得到的概率分类"""
    prob0 = np.sum(inputData * p0) + (1-pc1)
    prob1 = np.sum(inputData * p1) + pc1
    if prob0 > prob1:
        return 0
    else:
        return 1


def testNB():
    """测试函数"""
    docList, classVec = loadDataSet()
    vocabList = createVocabList(docList)

    trainMat = []                       # 由0/1组成的数据集 ： [[0,1,0,0,1,....],[0,0,0,0,0,1,...]]
    for doc in docList:
        trainMat.append(setOfWords2Vec(vocabList, doc))
    p0, p1, pc1 = trainNB0(trainMat, classVec)

    testData = ['love', 'my', 'dalmation']
    thisDoc = setOfWords2Vec(vocabList, testData)
    print("分类结果是：", classifyNB(thisDoc, p0, p1, pc1))

    testData = ['stupid', 'garbage']
    thisDoc = setOfWords2Vec(vocabList, testData)
    print("分类结果是：", classifyNB(thisDoc, p0, p1, pc1))



if __name__ == "__main__":
    docList, classVec = loadDataSet()
    vocabList = createVocabList(docList)
    print("文档列表：", docList, "\n分类向量：", classVec)
    # print("词汇表：", vocabList)
    # trainMat = []
    # for doc in docList:
    #     trainMat.append(setOfWords2Vec(vocabList, doc))
    # p0v, p1v, pAb = trainNB0(trainMat, classVec)
    # print("p0:", p0v, "\np1:", p1v, "\npAb:", pAb)
    testNB()
    # print(setOfWords2Vec(vocabList, docList[0]))