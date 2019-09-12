---
title: python常用工具
date: 2019-03-28 09:47:59
tags: ML
categories: Python
---



> 工欲善其事必先利其器(不搞清楚这个代码实在敲不下去。。)

# Jupyter 的常见用法
两种模式。命令模式（蓝色）和编辑模式（绿色），直接使用 `Enter` 进入编辑模式， 使用 `Esc` 进入命令模式。类似于 `VIM`。

 <!-- more -->

## 命令模式下快捷键：

- `j/k` : 在上下cell间切换，之后直接`Enter`可以进入编辑模式，很实用
- `shift + j/k(up/down)` : 选中多个cell。
- `shift + M` : 合并cell
- `L` : 显示/关闭**行号**
- `c/v` : 复制cell / 粘贴到当前行的下一行
- `F` : 在代码中查找
- `O` : 展开/收缩输出结果

## 编辑模式下快捷键：

- `Tab` : 代码补全/缩进
- `shift + Tab` : 提示函数细节信息
- `Ctrl-]` : 缩进
- `Ctrl-[` : 解除缩进
- `ctrl-z/ ctrl-shift-z` : 撤回/迭代取消撤回再做
- `Esc / Ctrl+M` : 进入命令模式
- `Shift+Enter` : 运行本cell，并切换到下一个单元
- `Ctrl+Enter` : 运行本cell
- `Alt+Enter` : 运行本cell，并在下面插入一个单元

# 安装python虚拟环境virtualenv
默认安装到系统python的lib目录下
> pip install virtualenv

```
D:\Code\Python\机器学习>pip install virtualenv
Looking in indexes: http://mirrors.aliyun.com/pypi/simple/
Collecting virtualenv
  Downloading http://mirrors.aliyun.com/pypi/packages/33/5d/314c760d4204f64e4a968275182b7751bd5c3249094757b39ba987dcfb5a/virtualenv-16.4.3-py2.py3-none-any.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 2.3MB/s
Installing collected packages: virtualenv
Successfully installed virtualenv-16.4.3
```

**新建虚拟环境**
> virtualenv envTest 


```
D:\Code\Python\Pyenvs>virtualenv envTest
Using base prefix 'd:\\programdata\\anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in D:\Code\Python\Pyenvs\envTest\Scripts\python.exe
Installing setuptools, pip, wheel...
done.
```

**进入虚拟环境的 `Scripts`目录下，执行 `activate.bat`**
> cd envTest/Scripts
> activate.bat
> 
> (envTest) D:\Code\Python\Pyenvs\envTest\Scripts>

此时再安装numpy，就会安装到虚拟环境的site-packages目录下
```
(envTest) D:\Code\Python\Pyenvs\envTest\Scripts>pip install numpy

(envTest) D:\Code\Python\Pyenvs\envTest\Scripts>pip show numpy
Name: numpy
Version: 1.16.2
Summary: NumPy is the fundamental package for array computing with Python.
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD
Location: d:\code\python\pyenvs\envtest\lib\site-packages
Requires:
Required-by:
```

**退出虚拟环境 **
> deactivate.bat

# 安装 virtualenvwrapper-win

> pip3 install virtualenvwrapper-win
> workon   # 万能命令。。。

出现下列结果表示成功
```
D:\Code\Python\Pyenvs\envTest\Scripts>workon

Pass a name to activate one of the following virtualenvs:
==============================================================================
找不到文件
```
使用 `mkvirtualenv` 创建新的虚拟环境，并自动进入虚拟环境中。
> mkvirtualenv envTest

所有的虚拟环境默认放到了 `C:\Users\twili\Envs` 目录下，可以更改环境变量`WORKON_HOME`改变这个目录。改变目录后可以手动将之前的虚拟环境复制到新的目录下，依然可以使用。
```
D:\Code\Python\Pyenvs\envTest\Scripts>mkvirtualenv envTest2
 C:\Users\twili\Envs is not a directory, creating
Using base prefix 'd:\\programdata\\anaconda3'
  No LICENSE.txt / LICENSE found in source
New python executable in C:\Users\twili\Envs\envTest2\Scripts\python.exe
Installing setuptools, pip, wheel...
done.

(envTest2) D:\Code\Python\Pyenvs\envTest\Scripts>
```

直接使用workon查看已有的虚拟环境
```
(envTest2) D:\Code\Python\Pyenvs\envTest\Scripts>workon

Pass a name to activate one of the following virtualenvs:
==============================================================================
envTest2
```

总结如下：
- 列出虚拟环境列表 ：`workon`
- 新建虚拟环境 ：`mkvirtualenv [虚拟环境名称]`
- 启动/切换虚拟环境 ：`workon [虚拟环境名称]`
- 离开虚拟环境 ：`deactivate`

# 使用pycharm的坑
pycharm新建项目默认会创建一个虚拟环境，并自动切换到虚拟环境中，terminal也在默认的虚拟环境下，使用时经常出错。。。（可能时当时没注意已经在虚拟环境下了）。导包导不进去，pip install又提示包已安装。气得我把键盘都抠坏了。。

特地研究了一下`virtualenv`，使用`virtualenvwrapper`手动管理虚拟空间，并在创建项目时指定已有的虚拟空间，这样各个空间相互隔离。但是之前安装的包都要重新安装了


最后，`virtualenvwrapper` 真好用！