# 信息增益
- 香农熵： 指混乱程度，越混乱，值越大
- 信息增益（information gain）： 在划分数据集前后信息发生的变化称为信息增益（香农熵的差）

> **基尼不纯度**也可度量集合的无序程度

香农熵的计算公式如下：
$$
H=-\sum_{i=1}^{n}p(x_{i})log_{2}p(x_{i})
$$

- xi是目标变量的某个取值，
- H是一个数学期望
- 因为p(xi)<1，所以最后结果是正数

```python
def calcShannonEnt(dataSet):
    """计算香农熵"""
    labelCounts={}
    numEntries = len(dataSet)       # 数据集的总数，用于计算比例P

    # 1. 计算出每个label对应的数量
    for line in dataSet:
        label = line[-1]
        if label not in labelCounts.keys():
            labelCounts[label] = 0
        labelCounts[label] += 1
	
	# 2. 使用labelCounts计算prob和H
    shannonEnt = 0.0                # 熵的初值
    for label, count in labelCounts.items():
        prob = float(count) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt
```


# 找到最好的划分方式
## 划分数据集
`splitDataSet(dataSet,0,1)` 表示先选出满足条件"第0个标签的值等于0"的数据，再把数据中的第0个标签剔除掉。

> \>>> dataSet
> [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]


> \>>> splitDataSet(dataSet, 0, 1)
> [[1, 'yes'], [1, 'yes'], [0, 'no']]


> \>>> splitDataSet(dataSet, 0, 0)
> [[1, 'no'], [1, 'no']]


```python
def splitDataSet(dataSet, axis, value):
    """划分数据集。python使用引用传递列表，因此创建一个新的结果列表"""
    returnDataSet = []
    for line in dataSet:
        if line[axis] == value:
            newline = line[:axis]
            newline.extend(line[axis+1:])
            returnDataSet.append(newline)
    return returnDataSet
```

数据必须满足两点要求：
- 数据集必须是列表的列表，且每条数据长度相同
- 数据的最后一列是分类结果


## 寻找最好的特征进行分类
对每个特征进行划分，找到划分后，信息增益最大的特征
- 需要遍历所有特征，计算每次的信息增益
- 特征i可能有很多取值，会产生很多分支，对每个分支计算香农熵。最后的熵取所有分支熵的数学期望。
- 信息增益=原始熵-按特征i划分后各个分支熵的数学期望

```python
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
```

# 构建决策树
递归创建决策树，递归终止的条件有两个：
- 遍历完所有划分数据集的属性（每次划分会消耗一个属性，属性已经用完）
- 该分支下所有实例都是相同的分类