# 数据类型
dtype用于自定义类型。i1，i2，i4，i8表示int8，int16，int32，int64。`S20`表示特定长度的字符串
> dtype([('键','值类型'),('键','值类型'),...])


```
import numpy as np

# 定义类型
dt = np.dtype([("age","i4")])
Student = np.dtype([("name","S10"),("age", np.int32),("marks", "f4")])

# 创建自定义类型的变量
a = np.array([[1,2],[3,4],[5,6]], dtype=dt)
b = np.array([1,3,5], 			dtype=dt)
c = np.array([("tom", 20, 99.9),("tim", 22, 98.9),("karl", 22, 100)], dtype=Student)


print(dt)	# [('age', '<i4')]
print(a)	
print(b)	# [(1,) (3,) (5,)]
print(c)	# [(b'tom', 20,  99.9) (b'tim', 22,  98.9) (b'karl', 22, 100. )]

print(a["age"])		# [[1 2] [3 4] [5 6]]
print(c["name"])	# [b'tom' b'tim' b'karl']
```

# 数组 ndarray

- zeros(shape),ones(shape),empty(shape), `np.full(shape=(3,4), fill_value=4)`
- `eye(N, M=None, k=0, dtype=<class 'float'>)` : 对角矩阵，k>0时，表示右上方第一条线，k=0表示单位矩阵

## `ndarray`的构造函数
> numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

- dtype: 规定数组元素的类型
- copy：对象是否需要复制
- order：创建数组的样式，C为行方向，F为列方向，A为任意方向。
- subok：返回一个与基类类型一致的数组
- ndmin：指定最小维度

```
a = np.array([1,2,3,4,5,6])
b = np.array([[1,2,3],[4,5,6]])
c = np.array([1,2,3,4,5,6], ndmin=2)
d = np.array([1,2,3,4,5,6], ndmin=3)	
e = np.array([[1,2,3],[4,5,6]],ndmin=3)

print(a)	# [1 2 3 4 5 6]
print(b)	# [[1 2 3] [4 5 6]] 
print(c)	# [[1 2 3 4 5 6]]
print(d)	# [[[1 2 3 4 5 6]]]
print(e)	# [[[1 2 3] [4 5 6]]]

print(d[0,0,0])		# 三维的数组就是把一维数组当成第三层维度
print(e[0,0,0])
print(e[0,1,0])		# 三维数组把二维数组当成第2,3维度
```

## `ndarray` 属性

|属性|说明|
|:----:|:----:|
| ndim | 秩，轴的数量，维度的数量| 
| shape| 数组的维度，对于矩阵是n行m列| 
| size | 总个数，n*m| 
| dtype|  元素类型| 
| itemsize | 每个元素的大小，以字节为单位| 

### np.shape和np.reshape()

```
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)		# (2,3)	
a.shape = (3,2) 	# 相当于 a.reshape(3,2)
print(a)			# (3,2)
```

### 维度

```
a = np.arange(24)
b = a.reshape(2,3,4)
print(a)
print(b)

###
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

### 2个 3*4的数组（2*3*4）
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

### 创建空数组(元素为随机值) 

> np.empty(shape, dtype = float, order = 'C'/'F')


```
np.empty((2,2), dtype=int)
np.empty(2,dtype=int)

###
[[1701540705, 1635131492],
 [1936029036,  537528878]]

[0, 1073741824]
```

### 创建全0数组

> np.zeros(shape, dtype=float, order='C'/'F')


```
np.zeros(5, dtype=int)
np.zeros((5,), dtype=int)
np.zeros((2,2), dtype=[('x', int),('y', int)])

###
array([0, 0, 0, 0, 0])
array([0, 0, 0, 0, 0])
array([[(0, 0), (0, 0)],
       [(0, 0), (0, 0)]], dtype=[('x', '<i4'), ('y', '<i4')])
```


### 创建全1数组：


> numpy.ones(shape, dtype = None, order = 'C')


```
np.ones(5)
np.ones((2,2))

###
array([1., 1., 1., 1., 1.])
array([[1., 1.],
       [1., 1.]])
```

### 使用arange创建数组（直接返回ndarray，range()返回list对象）
> numpy.arange(start=0, stop, step=1, dtype) # 如果只有1个参数，表示[0,stop)
> - start 起始值（0）
> - stop 终止值 `[start, stop)`
> - step 步长
> - dtype 数据类型


### 等差数列 np.linspace()
> np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

>  - start	:  起始值
>  - stop	:  终止值
>  - num	:  等步长的样本数量(默认为50)
>  - endpoint	: ture 则包含stop值，反之不包含（默认是True）
>  - retstep	: 如果为 True 时，生成的数组中会显示间距，反之不显示。
>  - dtype		: `ndarray` 的数据类型

```
np.linspace(0,10,5)
np.linspace(1,10,5)
np.linspace(0,10,5,endpoint=False)
```

### 等比数列 np.logspace()
> np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
>  - start	: 起始值为：`base ** start`
>  - stop	: 序列的终止值为：`base ** stop`。
>  - num	: 等步长的样本数量(默认为50)
>  - endpoint	: ture 则包含stop值，反之不包含(默认是True)
>  - base	: 对数 log 的底数（默认是10）
>  - dtype	: ndarray 的数据类型

```
np.logspace(1,10,10,base=2)
np.logspace(0,9,10,base=2)
np.logspace(0,9,10)
np.logspace(0,9,10,base=10)

###
array([   2.,    4.,    8.,   16.,   32.,   64.,  128.,  256.,  512.,  1024.])
array([  1.,   2.,   4.,   8.,  16.,  32.,  64., 128., 256., 512.])
array([1.e+00, 1.e+01, 1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06, 1.e+07, 1.e+08, 1.e+09])  ## 1.0e+00 省掉了小数点后的0
array([1.e+00, 1.e+01, 1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06, 1.e+07, 1.e+08, 1.e+09])
```

## asarray 和 array 
在用ndarray 初始化数组时，如果array保留的是副本，asarray没有使用副本.[[参考]](https://blog.csdn.net/gobsd/article/details/56485177)
> numpy.asarray(a, dtype = None, order = None)


```
array = np.eye(3,3)
array1 = np.array(array)
array2 = np.asarray(array)
array[0] = 2			# 改变array的值

print(array1)
print(array2)

###
array([[1., 0., 0.],		# array1 的值不变，是副本
       [0., 1., 0.],
       [0., 0., 1.]])
array([[2., 2., 2.],		# array2 的值也变了，不是副本
       [0., 1., 0.],
       [0., 0., 1.]])
```

## 小结
- `eye(n)` ： 创建单位矩阵
- `empty(shape, dtype = float, order = 'C'/'F')` ： 创建未初始化的数组
- `zeros(shape, dtype=float, order='C'/'F')` ： 创建全0数组
- `ones(shape, dtype=float, order='C'/'F')` ： 创建全1数组
- `full(shape, num)` 		： 				创建形状为shape的数组，用num填充 
- `ndarray arange(start=0, stop, step=1, dtype)` ： 等差数组。`arange(stop)`表示`[0,stop)`;  `arange(start,stop)`表示`[start, stop)`; `arange(start, stop, step)`表示步长。

# 索引
> slice(start, stop, step)        # 返回的是slice类型
> 或 array[start : stop : step]   # [start, stop)

```
a = np.arange(1,11)
s = slice(0,10,2)
print(a[s])
print(a[0:11:2])

###
[1 3 5 7 9]
```
```
a = np.arange(start=1,stop=11, step=1)
a		# [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
a[2:5]	# [3, 4, 5]
a[0:]	# [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
a[:2]	# [1, 2]
```

多维数组:
```
a = np.array([[1,2,3],[3,4,5],[4,5,6],[7,8,9]])  
print(a) 			# [[1 2 3] [3 4 5] [4 5 6] [7 8 9]]
print (a[...,1])  	# 第2列元素 [2 4 5 8]
print (a[1,...])    # 第2行元素 [3 4 5]
print (a[...,1:])   # 第2列及剩下的所有元素 [[2 3] [4 5] [5 6] [8 9]]
```


# 运算
`+` `-` `*` `/` `%` `**n` : 矩阵的对应位置元素的加、减、乘、除、取余、n次方

- 矩阵乘法： `a.dot(b)`
- 矩阵转置： `a.transpose()` 或者 `a.T`
- 矩阵求逆： `np.linalg.pinv(a)` 或者 `a.I`
- 矩阵除法： `np.linalg.solve(matA, matB)`

# 常用函数

`a.max(axis=0)` `a.max(axis=1)` `a.argmax(axis=1)` ： 每列的最大值（在行方向找最大值）、每行的最大值（在列方向找对大致）、最大值的坐标 
- `sum()`求和、`mean()`平均值、`var()` 方差、`std()` 标准差  ： 用法与max类似
- `np.random.uniform(a,b)` 随机小数
- `np.tile(a,(1,2))`：行上重复1次，列上重复两次。


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