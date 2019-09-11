import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt
import os


def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    """KNN算法"""
    dataSetSize = dataSet.shape[0]  # 获得数据集的条数,shape[0]表示第一维的数量
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet  # 让测试数据与每条dataSet数据集作减法运算
    sqdiffMat = diffMat ** 2  # 平方
    sqDistance = sqdiffMat.sum(axis=1)  # 每行求和
    distance = sqDistance ** 0.5  # 求和之后开根号，表示距离
    sortedDistanceIndices = distance.argsort()  # 按从小到大的顺序返回下标
    classCount = {}
    for i in range(k):  # 拿前k的label
        voteIlabel = labels[sortedDistanceIndices[i]]  # 按从小到大那label
        classCount[voteIlabel] = classCount.get(voteIlabel,
                                                0) + 1  # 使用classCount.get()当voteIlabel不存在时，返回默认的值（0）。用classCount[voteIlabel]当不存在时会报错

    # 此时前k的元素的label数目已经统计在classCount里。现在对classCount排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 返回一个列表
    return sortedClassCount[0][0]


def file2matrix(fileName):
    """将文件转换为矩阵"""
    # 读取文件，得到文件行数
    with open(fileName) as dataSet:
        dataSetLines = dataSet.readlines();
    numberOfLines = len(dataSetLines)
    # 创建返回的矩阵
    returnMat = np.zeros((numberOfLines, 3))  # 保存数据集所有特征的矩阵
    # 解析数据
    classLabelVedtor = []
    for i in range(numberOfLines):
        line = dataSetLines[i].strip()
        values = line.split(sep="\t")
        returnMat[i, :3] = values[:3]
        classLabelVedtor.append(values[3])
    # 返回
    return returnMat, classLabelVedtor


def autoNum(dataSet):
    """归一化数据: newValue = (oldValue-min)/(max-min)"""
    maxVals = dataSet.max(axis=0)  # 每个列的最大值
    minVals = dataSet.min(axis=0)  # 每个列的最小值
    ranges = maxVals - minVals

    number = len(dataSet)
    minTile = np.tile(minVals, (number, 1))
    rangesTile = np.tile(ranges, (number, 1))
    normDataSet = (dataSet - minTile) / rangesTile

    return normDataSet, ranges, minVals


def datingClassTest():
    """计算分类器准确率"""
    hoRatio = 0.10  # 测试数据所占的比例
    # 获得数据集
    dataSet, labels = file2matrix("dataset/datingTestSet2.txt")
    # 归一化处理
    normDataSet, ranges, minVals = autoNum(dataSet)

    wrongNum = 0;
    dataSetLen = dataSet.shape[0]
    runnableNum = hoRatio * dataSetLen  # 用于测试的数据条数
    runnableNum = int(runnableNum)
    for i in range(runnableNum):  # 此处必须保证range里面是整数
        result = classify0(normDataSet[i, :], normDataSet[runnableNum:, :], labels[runnableNum:], 3)
        print("计算出的结果是：", result, "实际结果是：", labels[i])
        if result != labels[i]:
            wrongNum = wrongNum + 1
    print("错误率是：", (wrongNum / runnableNum))


def classifyPerson():
    """预测函数"""
    resultList = ["not at all", "in small doses", "in large doses"]
    game = input("请输入玩游戏的时间：")
    ffmiles = input("请输入长跑：")
    iceCream = input("请输入冰淇凌")
    dataSet, labels = file2matrix("dataset/datingTestSet2.txt")
    normDataSet, ranges, minVals = autoNum(dataSet)

    inx = np.array([float(ffmiles), float(game), float(iceCream)])
    result = classify0((inx - minVals) / ranges, normDataSet, labels, 3)

    print("结果是：", resultList[int(result) - 1])


def paint():
    dataSet, labels = file2matrix("dataset/datingTestSet2.txt")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSet[:, 0], dataSet[:, 1], s=15.0 * np.array(labels, dtype=float),
               c=15.0 * np.array(labels, dtype=float))
    #    ax.scatter(dataSet[:, 1], dataSet[:, 2], c='b', alpha=0.5)
    plt.show()


### 以下是手写识别：
def img2vector(filename):
    """将图像转换成[1,1024的向量，图像是32*32，向量中保存的是int型"""
    returnVect = np.zeros((1, 1024), dtype=int)     # 构造结果矩阵
    with open(filename) as file:
        fileLines = file.readlines()
        for i in range(len(fileLines)):
            line = fileLines[i].strip()
            for j in range(len(line)):
                returnVect[0, i*32 + j] = int(line[j])
    return returnVect

def handwritingClassTest():
    """手写识别系统"""
    ## 训练样本集(准备数据集和labels)
    # 获取目录内容
    trainSetFilenames = os.listdir("dataset/trainingDigits")
    numberOfTrainSet = len(trainSetFilenames)
    # 从文件名解析分类数字
    labels = []
    trainDataSet = np.zeros((numberOfTrainSet, 1024))     # n行，1024列的训练数据矩阵
    for i in range(numberOfTrainSet):                     # 给每行赋值
        fileMatrix = img2vector("dataset/trainingDigits/%s" % trainSetFilenames[i])
        trainDataSet[i, :] = fileMatrix
        file_label = trainSetFilenames[i].split(".")[0].split("_")[0]
        labels.append(int(file_label))

    # 开始测试（准备测试数据集）
    testSetFilenames = os.listdir("dataset/testDigits/")
    numberOfTestSet = len(testSetFilenames)
    testDataSet = np.zeros((numberOfTestSet, 1024))
    error = 0
    for i in range(numberOfTestSet):
        testFileMatrix = img2vector("dataset/testDigits/%s" % testSetFilenames[i])
        resultLabel = classify0(testFileMatrix, trainDataSet, labels, 3)
        rightLbael = testSetFilenames[i].split(".")[0].split("_")[0]
        print("label是：", rightLbael, "计算的结果是：", resultLabel)
        resultLabel = int(resultLabel)
        rightLbael = int(rightLbael)
        if resultLabel != rightLbael:
            error += 1
    print("计算错误的个数是：", error, "计算的错误率是：", error/numberOfTestSet)



if __name__ == "__main__":
    # datingClassTest()
    # paint()
    # classifyPerson()
    handwritingClassTest()
