from math import log


def createDataSet():
    dataSet = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    """计算香农熵"""
    labelCounts = {}
    numEntries = len(dataSet)  # 数据集的总数，用于计算比例P

    # 1. 计算出每个label对应的数量
    for line in dataSet:
        label = line[-1]
        if label not in labelCounts.keys():
            labelCounts[label] = 0
        labelCounts[label] += 1

    # 2. 使用labelCounts计算prob和H
    shannonEnt = 0.0  # 熵的初值
    for label, count in labelCounts.items():
        prob = float(count) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    """划分数据集。python使用引用传递列表，因此创建一个新的结果列表"""
    returnDataSet = []
    for line in dataSet:
        if line[axis] == value:
            newline = line[:axis]
            newline.extend(line[axis+1:])
            returnDataSet.append(newline)
    return returnDataSet


def chooseBestFeatureToSplit(dataSet):
    """寻找最好的分类特征==> 寻找分类后，信息增益最大的特征"""
    numberOfFeature = len(dataSet[0]) -1        # 最后一位不要，因为他是分类结果
    numberOfDataSet = len(dataSet)
    baseEntropy = calcShannonEnt(dataSet)       # 原始香农熵
    bestInfoGain = 0.0                          # 用于记录最大信息熵
    bestFeature = -1                            # 用于记录最大信息熵对应的特征下标

    # 对每个特征进行划分，找到划分后，信息增益最大的特征
    for i in range(numberOfFeature):
        # 1. 找到该特征的所有可能取值，去重
        values = [example[i] for example in dataSet]
        uniqueValue = set(values)
        # 2. 对于每一个取值，计算一次香农熵，信息增益就是不同取值的香农熵的数学期望
        newShannonEnt = 0.0
        for value in uniqueValue:
            splitedDataSet = splitDataSet(dataSet, i, value)
            prob = float(len(splitedDataSet)) / numberOfDataSet
            newShannonEnt += prob * calcShannonEnt(splitedDataSet)

        # 3. 寻找最大信息增益
        infoGain = baseEntropy - newShannonEnt
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i

    # 寻找最大的数学期望，返回该特征
    return bestFeature


def majorithCnt(classList):
    """"""


def createTree(dataSet, labels):
    """创建决策树"""
    # 递归终止条件

    # 寻找最优特征

    # 计算每个特征的所有值，

    return myTree


if __name__ == "__main__":
    dataSet, labels = createDataSet()
    print(calcShannonEnt(dataSet))
    bestFeature = chooseBestFeatureToSplit(dataSet)
    print(bestFeature)
    print(dataSet)
