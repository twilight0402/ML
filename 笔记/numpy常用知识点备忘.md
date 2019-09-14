# 常用函数

- `a.max(axis=0)` `a.max(axis=1)` `a.argmax(axis=1)` ： 每列的最大值（在行方向找最大值）、每行的最大值（在列方向找对大致）、最大值的坐标 
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

- 矩阵乘法： `a.dot(b)`
- 矩阵转置： `a.transpose()` 或者 `a.T`
- 矩阵求逆： `np.linalg.pinv(a)` 或者 `a.I`
- 矩阵除法： `np.linalg.solve(matA, matB)`

# Tips
- 列表使用前需初始化，直接给不存在的数组赋值会报错: `data[0] = 1`
- `dict.keys()[0]`会报错，必须使用`list()`转型 ==> `list(dict.keys())[0]`
- `np.log(矩阵)` 表示对矩阵中的所有元素计算对数，但是，`math.log(矩阵)`会报错，报错信息如下：
    > TypeError: only size-1 arrays can be converted to Python scalars
- `a = range(1, 26); del a[0]` a是range对象，可以访问，但是不可以删除。可以转型之后再使用 `a = list(range(1, 26))`


# TODO
- python集合运算
- python正则表达式


