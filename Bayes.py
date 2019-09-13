

def loadDataSet():
    """
    创建数据集
    :return: 单词列表postingList, 所属类别classVec
    """
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def createVocabList(dataSet):
    """构造词汇表，统计所有文本中的所有单词
    :return list 去重的词汇表
    """
    vocalSet = set([])
    for line in dataSet:
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


if __name__ == "__main__":
    listOPosts, listClasses = loadDataSet()
    vocabList = createVocabList(listOPosts)
    trainMat = []
    for postInDoc in listOPosts:
        trainMat.append(setOfWords2Vec(postInDoc))
    p0v, p1v, pAb = trainNB(trainMat, listClasses)