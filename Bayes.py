import random

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


def bagOfWords2Vec(vocabList, inputSet):
    """[词袋模型]将输入数据转换为向量.存在这个单词记为1，不存在则记为0"""
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
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
            p0 += trainMatrix[i]                            # 统计先验概率c0下，每个单词出现的次数
            p0Total += sum(trainMatrix[i])
        else:
            p1 += trainMatrix[i]                            # 统计先验概率c1下，每个单词出现的次数
            p1Total += sum(trainMatrix[i])

    p0 = p0 / p0Total           # 用c0下每个单词出现的次数，分别除以c0下的总数==> p(wi|c0)
    p1 = p1 / p1Total           # p(wi|c1)

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
    prob0 = np.sum(inputData * p0) + np.log(1-pc1)
    prob1 = np.sum(inputData * p1) + np.log(pc1)
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


def textParse(bigString):
    """将字符串返回成单词列表
    1. 以空白字符作为分隔符
    2. 排除长度小于2的单词，他可能没有实际意义
    3. 所有单词转换为小写
    """
    import re
    listOfWords = re.split(r'\W*', bigString)
    return [word.lower() for word in listOfWords if len(word) > 2]


def spamTest():
    """测试算法。使用交叉验证"""
    docList, classList, fullText = [], [], []
    # 1. 解析文本文件。一个文件解析成一个list，所有文件保存为一个二维list
    for i in range(1, 26):
        spam = open("dataset/email/spam/%d.txt" % i)
        wordList = textParse(spam.read())
        docList.append(wordList)
        classList.append(1)

        ham = open("dataset/email/ham/%d.txt" % i)
        wordList = textParse(ham.read())
        docList.append(wordList)
        classList.append(0)

    # 2.格式化
    vocabList = createVocabList(docList)     # 创建词汇表

    # 3. 随机挑选10个测试数据（可能没有10个）
    trainSet = list(range(50))            # 记录了所有用于训练的数据集的下标
    testSet = []                    # 记录了所有用于测试的数据集的下标
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainSet)))
        testSet.append(trainSet[randIndex])
        del trainSet[randIndex]

    # 4. 训练
    trainMatrix, trainCategory = [], []
    for i in range(len(trainSet)):
        trainMatrix.append(bagOfWords2Vec(vocabList, docList[trainSet[i]]))
        trainCategory.append(classList[trainSet[i]])
    p0, p1, pc1 = trainNB1(trainMatrix, trainCategory)

    # 5. 测试
    testMatrix, testCategory, error = [], [], 0
    for i in range(len(testSet)):
        line = bagOfWords2Vec(vocabList, docList[testSet[i]])
        result = classifyNB(line, p0, p1, pc1)
        if result != classList[testSet[i]]:
            error += 1
    print("错误率为：", (float(error)/len(testSet)))


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
    #testNB()
    # print(setOfWords2Vec(vocabList, docList[0]))
    spamTest()