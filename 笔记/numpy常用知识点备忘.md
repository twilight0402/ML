---
title: numpy常用知识点备忘录
date: 2019-09-10 22:19:23
tags: ML
categories: ML
---

# 常用函数

- `a.max(axis=0)` `a.max(axis=1)` `a.argmax(axis=1)` ： 每列的最大值（在行方向找最大值）、每行的最大值（在列方向找对大致）、最大值的坐标 
- `sum()`求和、`mean()`平均值、`var()` 方差、`std()` 标准差  ： 用法与max类似
- `numpy.random.uniform(low=0,high=1,size)` 随机浮点数[low, high)。size可以是整数或者元组。默认是1
- `np.tile(a,(1,2))`：行上重复1次，列上重复两次。

<!-- more -->
- `arr.argsort()` ： 返回从小到大的序列号，返回值是python的list

- `sorted(iterable, cmp=None, key=None, reverse=False)` ： 对所有可迭代对象排序。保留原对象，返回新的对象。`reverse=False`表示从小到大
- `list.sort(cmp=None, key=None, reverse=False)` : 对列表排序，直接对原列表操作

- `operator`模块提供的`itemgetter`函数用于获取对象的哪些维的数据
```
a = [5,8,2,7,21]
b = operator.itemgetter(0)
b(a)

b = operator.itemgetter(1,0)
b(a)

###
5
(8,5)
```

- 使用`reload(KNN)`更新修改的模块
```
import importlib
importlib.reload(KNN)
```

- `list.extend(list1)`和`list.append(list1)`:??????????????????????????
- python字典的遍历
	- `for i in dict` <==> `for i in dict.keys()` ： 按key遍历
	- `for value in d.values()` ： 按值遍历
	- `for key,value in d.items()` ： 按键值对遍历

- `函数名.变量名` 用这种方式定义的变量，可以在任意位置访问，但是访问的方式必须是：`函数名.变量名`。直接访问变量名是无效的。当然必须要在函数执行过后，变量才能生效
```
def fun():
    fun.var1 = 1
    fun.var2 = 2
    print(fun.var1)
 #   print(var2)        # 报错

fun()
print(fun.var2)
```


## 矩阵
- `eye(n)` ： 创建单位矩阵
- `empty(shape, dtype = float, order = 'C'/'F')` ： 创建未初始化的数组
- `zeros(shape, dtype=float, order='C'/'F')` ： 创建全0数组
- `ones(shape, dtype=float, order='C'/'F')` ： 创建全1数组
- `full(shape, num)` 		： 				创建形状为shape的数组，用num填充 
- `ndarray arange(start=0, stop, step=1, dtype)` ： 等差数组。`arange(stop)`表示`[0,stop)`;  `arange(start,stop)`表示`[start, stop)`; `arange(start, stop, step)`表示步长。

## 运算
`+` `-` `*` `/` `%` `**n` : 矩阵的对应位置元素的加、减、乘、除、取余、n次方

- 矩阵乘法(二维数组时是当成矩阵乘法; 一维数组时计算的是内积，返回一个数值而不是数组)： `a.dot(b)`
- 矩阵转置： `a.transpose()` 或者 `a.T`
- 矩阵求逆： `np.linalg.pinv(a)` 或者 `a.I`
- 矩阵除法： `np.linalg.solve(matA, matB)`

## 随机数
### np.random.uniform
> np.random.uniform(low=0.0, high=1.0, size=None)

默认返回0~1之间的float随机数
- low、high：float，可以是数组类型
- size: int, 数字n表示n的随机数; 元组shape表示形状为shape的矩阵

### np.random.random && np.random.random_sample
> np.random.random(size)

返回0~1之间的float随机数，size指定形状

### np.random.rand
> np.random.rand(d0, d1, …, dn)

默认返回0~1之间的float随机数，参数表示矩阵的维度，没有参数就返回随机数

### numpy.random.randn(d0, d1, ..., dn)
> numpy.random.randn(d0, d1, ..., dn)

返回标准正太分布（均值为0，方差为1）。默认返回一个flaot随机数

### numpy.random.normal(loc=0.0, scale=1.0, size=None)
> numpy.random.normal(loc=0.0, scale=1.0, size=None)

返回一个由size指定形状的数组，数组中的值服从 μ=loc,σ=scale 的正态分布。默认返回一个随机数

### randint()
> randint(low, high=None, size=None, dtype=’l’)

返回整型随机数，low和high表示范围，如果不指定high，则返回0~low之间的随机数，size指定矩阵形状，dtpe可选int和int32

### shuffle() 和 permutation()
都是打乱数组的顺序，但是，shuffle()会改变原来数组的顺序，而permutation()返回一个新对象
- shuffle(list): 可以是list或者二维数组。按照第一个索引洗牌
- permutation(x): x整数时，返回一个不大于x的随机排列的数组（就是从0~x，随机排列），当X是list时，跟shuffle一样

# Tips
- 列表使用前需初始化，直接给不存在的数组赋值会报错: `data[0] = 1`
- `dict.keys()[0]`会报错，必须使用`list()`转型 ==> `list(dict.keys())[0]`
- `np.log(矩阵)` 表示对矩阵中的所有元素计算对数，但是，`math.log(矩阵)`会报错，报错信息如下：
    > TypeError: only size-1 arrays can be converted to Python scalars
- `a = range(1, 26); del a[0]` a是range对象，可以访问，但是不可以删除。可以转型之后再使用 `a = list(range(1, 26))`
- **不可以一边用for循环遍历list一边删除list中的元素！！！！！！！！！** ，他会一边删除，一边跳，根本删不完。。。正确操作是 使用while删除元素：
```python
    i = 0
    while i < len(wordList):
        if wordList[i] in stopwordList:
            del wordList[i]
        else:
            i += 1
```

- `zip()` 将多个list打包成元组列表。用在for里非常方便
```
a = [1,2,3,4]
b = [2,3,4,5,6]
c = [4,5,6,7,8,9]

ziped = zip(a,b,c)
for a,b,c in ziped:
    print (a, b, c)
```

- `assert condition "promot"` 断言，当condition为False时会报异常，同时给出prompt作为提示
- `a[a<6]` 似乎可以返回所有满足条件的索引，然后把所有满足条件的元素返回
```python
a = np.array([1,2,3,4,5,6,7,8])
b = np.array([2,3,4,4,4,4,4,4,4,4,5,6,7,8,9])
a = a[ b < 6 ]
```

- 对于 `(1, )`与`(1,1)`的差别：
    ```python
    a = np.array([1])       # (1, )
    b = np.array([[1]])     # (1,1)
    ```


# TODO
- python集合运算
- python正则表达式
- 正态分布