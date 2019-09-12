from math import log
import operator


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
            newline.extend(line[axis + 1:])
            returnDataSet.append(newline)
    return returnDataSet


def chooseBestFeatureToSplit(dataSet):
    """寻找最好的分类特征==> 寻找分类后，信息增益最大的特征"""
    numberOfFeature = len(dataSet[0]) - 1  # 最后一位不要，因为他是分类结果
    numberOfDataSet = len(dataSet)
    baseEntropy = calcShannonEnt(dataSet)  # 原始香农熵
    bestInfoGain = 0.0  # 用于记录最大信息熵
    bestFeature = -1  # 用于记录最大信息熵对应的特征下标

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
    """第一种递归终止情况，所有的属性已经用完，但是分类结果并不一致，此时采取多数元组
    classList是所有分类结果的列表"""
    classCounts = {}
    # 统计出所有labels的数量
    for item in classList:
        if item not in classCounts.keys():
            classCounts[item] = 0
        classCounts[item] += 1

    # 排序classCounts不是list，不可以用sort()，这里使用sorted()排序
    sortedClassCount = sorted(classCounts.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    """创建决策树。labels 是对每个特征值的含义的解释，方便建立决策树"""
    # 递归终止条件
    classList = [example[-1] for example in dataSet]
    # (1)属性已经用完
    if len(dataSet[0]) == 1:
        majorithCnt(classList)
    # (2)所有分类已经一致
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    # 1. 寻找最优特征
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeature]  # 只是标签，用于建树
    mytree = {bestFeatureLabel: {}}         # 初始化树
    subLabels = labels[:]                   # 复制该列表，因为labels是引用。避免值被改变
    del subLabels[bestFeature]                 # subLabels

    # 2. 当前最优特征的所有取值，去重
    totalValues = [example[bestFeature] for example in dataSet]
    uniqueValues = set(totalValues)

    # 3. 每个value一个分支，确定每个分支的值。因为是递归，所以分支下可能还有分支(字典里可能嵌套字典)，如果该分支已经可以结束，则返回返回classList中的一个(分类结果)
    for value in uniqueValues:
        subDataSet = splitDataSet(dataSet, bestFeature, value)
        mytree[bestFeatureLabel][value] = createTree(subDataSet, subLabels)
    return mytree


def classify(inputTree, featureLabels, testVec):
    """
    :param inputTree: 构建好的决策树
    :param featureLabels: 标签列表，也就是每个分类的属性名
    :param testVec: 测试数据
    """
    firstStr = list(inputTree.keys())[0]            # 其实根元素只有一个
    secondDict = inputTree[firstStr]                # 第二层
    featureIndex = featureLabels.index(firstStr)    # 当前属性的下标

    for key in secondDict.keys():
        if testVec[featureIndex] == key:
            if type(secondDict[key]).__name__ == "dict":
                classLabel = classify(secondDict[key], featureLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


if __name__ == "__main__":
    dataSet, labels = createDataSet()
    # print(calcShannonEnt(dataSet))
    # bestFeature = chooseBestFeatureToSplit(dataSet)
    # print(bestFeature)
    # print(dataSet)
    # print(majorithCnt(['a','a','a','b','b','b','b']))
    myTree = createTree(dataSet, labels)
    print(classify(myTree, labels, [1, 1]))
