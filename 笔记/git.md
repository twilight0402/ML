---
title: Git常用命令备忘
date: 2019-09-17 17:31:30
tags: Git
categories: Git
---


# 基本操作
- `git init` : 初始化
- `git add  file` : 添加
- `git commit -m ""` : 提交


- `git status` 查看哪些被修改，是否被提交
- `git diff  filename` :  查看修改了什么内容

readme.txt
```
Git is a version control system.
Git is free software.
```
修改后的readme.txt
```
Git is a distributed version control system.
Git is free software.
```

- git status:

1.刚刚编辑完成

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
2.执行完add操作后：

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   readme.txt
```
3.执行完commit

```
$ git status
On branch master
nothing to commit, working tree clean
```

- git diff:

```
$ git diff readme.txt 
diff --git a/readme.txt b/readme.txt
index 46d49bf..9247db6 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
```

# 版本回退

- `git log [--pretty=oneline]` 看到最近的修改和commit[一行显示简化结果]

```
$ git log
commit 7cc923c7c82f59baef45bad87a7fe92372141f31 (HEAD -> master)
Author: wangchao <twilight@0402.com>
Date:   Tue Aug 6 11:05:59 2019 +0800

    add GPL

commit f620929dc0099452ccbfd74f24627492488018e9
Author: wangchao <twilight@0402.com>
Date:   Tue Aug 6 10:51:26 2019 +0800

    add distributed

commit b09dc7d79bea6543be0491bd3779f561b25ec435
Author: wangchao <twilight@0402.com>
Date:   Tue Aug 6 10:50:17 2019 +0800

    wrote a readme file

```
git中，`HEAD` 表示当前版本，`HEAD^`表示前一个版本，`HEAD^^`表示上上一个版本，上100各版本表示为`HEAD~100`,`HEAD` 其实是一个指针，回退版本其实就是移动指针。回退到上一个版本的命令是：
- `git reset --hard HEAD^`	回退到上一个版本

此时 `git log` 已经不会展示之前的被抛弃的版本，如果上面的命令行没有关闭的话可以获得`append GPL`的`commit id`，此时用`git reset` 也可以还原：
- `git reset --hard 7cc923c7c82f59baef45b`   还原到指定`commit id`指定的版本，`id` 不需要全写


但是如果，命令行已经关闭，找不到`commit id`，此时使用 `git reflog` 命令可以查看：
- `git reflog` 记录每一次命令

```
$ git reflog
f620929 (HEAD -> master) HEAD@{0}: reset: moving to head^
7cc923c HEAD@{1}: reset: moving to 7cc923c7c82f59baef45bad87a7fe92372141f31
f620929 (HEAD -> master) HEAD@{2}: reset: moving to HEAD
f620929 (HEAD -> master) HEAD@{3}: reset: moving to HEAD^
7cc923c HEAD@{4}: commit: add GPL								# 找到这行，前面就是 commit id
f620929 (HEAD -> master) HEAD@{5}: commit: add distributed
b09dc7d HEAD@{6}: commit (initial): wrote a readme file

# 使用上面获得的id，就可以恢复到指定的版本
$ git reset --hard 7cc923c
HEAD is now at 7cc923c add GPL
```

# 删除文件
1.真的要删除 --> `git rm filename` --> `git commit -m 'del file'`
2.误删，需要恢复文件 --> `git checkout -- filename` (用版本库的版本替换工作区的版本)

```
# 删除文件
$ rm test.txt

# 查看状态
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    test.txt

no changes added to commit (use "git add" and/or "git commit -a")

# 提交删除文件操作到暂存区
git add test.txt  # 或者 git rm test.txt

# 查看状态
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        deleted:    test.txt

# 提交删除操作到版本库
$ git commit -m 'del test.txt'
[master 69c78ac] del test.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 test.txt

```


# 撤销更改
## 丢弃工作区的修改
- `git checkout -- readme.txt` ： 丢弃工作区的修改


1. 还没有执行add，那么工作区将回到暂存区的状态
2. 执行了add，还没有执行commit， 那么也将和暂存区一致


- `git reset HEAD <file>` : 可以把暂存区的修改撤销掉（unstage），重新放回工作区

<b>
总结如下：
- 只修改了工作区，--> `git checkout -- <fileName>` 
- 提交到了暂存区，把暂存区和工作区同时撤销，--> `git reset HEAD <file>` --> `git checkout -- <filename>`
- 提交到了版本库，就只能回退版本，--> `git reset --hard HEAD^`
</b>



# 远程仓库

- `ssh-keygen -t rsa -C "twilight0402@163.com"` : 创建RSA密钥对
- `git remote add origin git@github.com:1601436878/AAA.git` ： 关联远程仓库
- `git remote rm origin` : 解除与远程版本库的关联
- `git remote -v` : 查看git对应的远程仓库地址
- `git push -u origin master` ： 第一次提交到远程
- `git push origin master` ： 之后提交不需要 `-u`
- `git clone git@github.com:1601436878/AAA.git` : 克隆仓库，克隆后，保留了完整的git仓库，包括`git log`

> 如果远程仓库有readme，回出错，第一次导入需要先pull
> - git pull --rebase origin master 

# 分支

- `git branch` ： 查看分支
- `git branch "name"` ： 创建分支
- `git checkout "name"` ： 切换分支
- `git checkout -b "name"` ： 创建+切换分支
- `git merge "name"` ： 合并某分支到当前分支
- `git branch -d "name"` ： 删除分支

`git branch dev`创建dev分支，dev指向是指针，指向当前版本。master也是指针，指向master分支上的最新的位置，HEAD指向master或者dev

```
git branch dev		# 从master分支的当前位置，创建dev分区
git branch dev2		# 同理
```
在不同的分支下修改文件，并分别提交
```
git checkout dev
vim README.md

git checkout dev2
vim README.md
```
现在各个分支之间是这样的结构：
![git分支](https://twilightblog.oss-cn-shenzhen.aliyuncs.com/photo/git1.png)


在不同的分支中，看不到其他分支的提交。但是`git reflog`可以看到所有分支的所有变化。没有被add或commit的变化在所有分支都是可见的。
在master分支中执行 `git merge dev` 合并后，`head`和`master`都指向了dev。这时可以删除dev了。
![git分支](https://twilightblog.oss-cn-shenzhen.aliyuncs.com/photo/git2.png)

但是此时无法删除dev2.如果执行`git branch -d dev2` 会报错，此时可以用`git branch -D dev2`强行删掉dev2。如果想恢复到dev2的状态，就只能用 `git reflog`找到之前的 `commit id`了。


## 冲突
如果出现了一下这种情况，在合并分支时就会出现冲突

![git冲突](https://twilightblog.oss-cn-shenzhen.aliyuncs.com/photo/git%E5%86%B2%E7%AA%81.PNG)

```
$ git merge feature
Auto-merging readme.txt
CONFLICT (content): Merge conflict in readme.txt
Automatic merge failed; fix conflicts and then commit the result.
```

冲突后readme.md文件变成了这样：
```
$ cat README.md
git is a distributed version control system.
git is a free software under GPL.
git has a mutable index called stage.

<<<<<<< HEAD
Creating a new branch is quick AND Simple.
=======
Creating a branch is quick & Simple.
>>>>>>> dev
```

此时需要手动修改readme.me文件，然后再 add 和 commit， 这样冲突才会解决

```
$ cat README.md
git is a distributed version control system.
git is a free software under GPL.
git has a mutable index called stage.

Creating a new branch is quick and Simple.
```

`git log --graph` 可以查看分支合并的情况
```
$ git log --graph
*   commit a40de601e061a393fae40df28796d9db4387bc27 (HEAD -> master)
|\  Merge: d6314aa 8dbf53c
| | Author: wangchao <twilight@0402.com>
| | Date:   Thu Aug 8 15:21:12 2019 +0800
| |
| |     fix confict
| |
| * commit 8dbf53c2d89e026544cc82be87ea21f593782ef8 (dev)
| | Author: wangchao <twilight@0402.com>
| | Date:   Thu Aug 8 15:07:13 2019 +0800
| |
| |     & Simple
| |
* | commit d6314aa206fcae0f103015933fe8027da2e763fb
|/  Author: wangchao <twilight@0402.com>
|   Date:   Thu Aug 8 15:04:19 2019 +0800
|
|       AND Simple
|
* commit 499304186d8522d0beb2ed328ead76631bf81a2f
| Author: wangchao <twilight@0402.com>
| Date:   Thu Aug 8 11:12:24 2019 +0800

```

```
$ git log --graph --pretty=oneline --abbrev-commit
*   a40de60 (HEAD -> master) fix confict
|\
| * 8dbf53c (dev) & Simple
* | d6314aa AND Simple
|/
* 4993041 edit in dev2
* f8e17ea (origin/master) del readme.txt
* 94571cf prepare
* 2adf4b6 del test.txt
* ee7d4b3 test.txt
* 52cc68c understand how stage works
* 16d5749 add GPL
* ff98a79 add distributed
* c435423 wrote a readme file
* 1891025 Initial commit
```

# 坑
git的`.gitignore`文件必须在项目push之前就创建。如果已经push过了再创建`.gitignore`就不会生效。。。。win下无法创建空文件名的文件，只能用gitBash的touch命令了


# 小结

- git status : 查看哪些被修改，是否被提交
- git diff  <filename> : 查看修改了什么内容，工作区和暂存区
- git diff HEAD -- readme.txt ： 查看工作区和版本库的区别
- git log [--pretty=oneline] : 看到最近的`commit`记录 [一行显示简化结果]
- git reflog : 记录每一次状态变化的命令，可以查看到每一次变化的 `commit id`

从版本库恢复到工作区
- git reset --hard HEAD^ : 回退到上一个版本
- git reset --hard 7cc923c7c82f59baef45b   : 还原到指定`commit id`指定的版本，`id` 不需要全写

<b>
撤销工作区：
- 只修改了工作区，--> `git checkout -- <fileName>` 
- 提交到了暂存区，把暂存区和工作区同时撤销，--> `git reset HEAD <file>` --> `git checkout -- <filename>`
- 提交到了版本库，就只能回退版本，--> `git reset --hard HEAD^`
</b>

删除文件：
1.真的要删除 --> `git rm filename` --> `git commit -m 'del file'`
2.误删，需要恢复文件 --> `git checkout -- filename` (用版本库的版本替换工作区的版本)