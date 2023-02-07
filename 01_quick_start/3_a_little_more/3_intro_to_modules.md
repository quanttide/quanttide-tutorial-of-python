---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python的模块

## 本讲大纲

- 介绍什么是Python模块
- 介绍如何创建Python模块
- 介绍如何使用Python模块
- 介绍Python模块的组织结构

## 什么是模块？

- 模块(Module)是一个包含Python定义和语句的以.py为后缀的文件。（Python官方文档）
- 模块是一种组织形式，把彼此有关系的Python代码组织到一个个独立文件当中（《Python核心编程》）


## 创建模块

1. 创建一个命名为mymodule.py的文件；
2. 打开mymodule.py，创建一个main函数，保存文件

## 导入模块

- 模块名即为.py文件不带后缀的文件名，这里是mymodule；
- 函数名即为<模块名>.<模块内的函数名>，这里是mymodule.main。

```{code-cell} ipython3
import my_module
```

```{code-cell} ipython3
my_module.func()
```

```{code-cell} ipython3
import math
```

```{code-cell} ipython3
math.sqrt(5)
```

```{code-cell} ipython3
# 导入自建模块
import mymodule

from imp import reload
reload(mymodule)
```

```{code-cell} ipython3
# 使用自建模块中定义的函数
mymodule.main()
```

也可以导入某一个Python对象

```{code-cell} ipython3
from mymodule import main
```

```{code-cell} ipython3
main()
```

```{code-cell} ipython3
import my_package
```

```{code-cell} ipython3
my_package.my_module.main()
```

```{code-cell} ipython3
import my_package.my_module as my_module2
```

```{code-cell} ipython3
my_module2.main()
```

```{code-cell} ipython3
from my_package.my_module import main
```

```{code-cell} ipython3
main()
```

```{code-cell} ipython3
import my_new_module
```

## 模块内结构（重点）

- 头部注释
- 导入模块
- 模块内的全局变量
- 定义函数
- 定义函数
- 主函数

## 拓展知识

- 为什么要用<模块名>.<函数名>的方式调用？为了防止不同的模块中有相同的函数名冲突。
- 在教学环境中我们使用的是Jupyter Notebook，可以简单理解为一个加强版的Python解释器，教学环境中实现的效果和在Python解释器中实现基本相同，在IDE中的实现效果在后面的教程再演示。
- 在一个Python环境中，模块导入以后不会再重复导入覆盖，如果在运行过程中模块中途有更新，需要使用reload函数实现重新导入；使用IDE运行代码通常情况下会创建一个新的Python环境，所以问题被掩盖了。
- 关于Python模块和导入系统的更多知识，详见本系列课程的第八章。

## 本讲作业

- 创建一个自定义模块，并在Python解释器环境中导入模块。

### 作业1

```{code-cell} ipython3
import mymodule
```

```{code-cell} ipython3
mymodule.ROOT_URL
```

```{code-cell} ipython3
mymodule.list_primes(100)
```

```{code-cell} ipython3
from mymodule import Vector
```

```{code-cell} ipython3
vector1 = Vector(1,2,3)
vector2 = Vector(2,2,3)
vector3 = Vector(3,4,5,4)
```

```{code-cell} ipython3
vector1 + vector2
```

```{code-cell} ipython3
vector1 + vector3
```

```{code-cell} ipython3

```
