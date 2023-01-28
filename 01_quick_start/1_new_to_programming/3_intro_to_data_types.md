---
level: introductory
stage: alpha
---

# Python的基本数据类型

本讲的教学目标为：

- 熟悉。认识Python的基本数据类型长啥样，分辨不同的数据类型有什么区别。
- 建模/抽象。搞清楚这些基本数据类型用来表示什么抽象的数据模型，**建立对数据类型从具象到抽象的认知**。

## 数字类型

### 整型

正数

```{code-cell} ipython3
10
```

类型

```{code-cell} ipython3
type(10)
```

负数

```{code-cell} ipython3
-100
```

零

```{code-cell} ipython3
0
```

### 浮点数

```{code-cell} ipython3
10.1
```

```{code-cell} ipython3
type(10.1)
```

```{code-cell} ipython3
-9.34
```

科学计数法

```{code-cell} ipython3
# 1.23*10**9
1.23e9
```

```{code-cell} ipython3
# -6.74*10**(-5)
-6.74e-5
```

浮点数和整数的值相等，但类型不同。

```{code-cell} ipython3
10 == 10.0
```

```{code-cell} ipython3
type(10.0)
```

```{code-cell} ipython3
type(10)
```

### 布尔数

真（`True`）或者假（`False`）

```{code-cell} ipython3
True
```

```{code-cell} ipython3
type(True)
```

True的本质是1

```{code-cell} ipython3
int(True)
```

```{code-cell} ipython3
False
```

False的本质是0

```{code-cell} ipython3
int(False)
```

## 列表

可变的有序表

```{code-cell} ipython3
my_list = [1,2,3,4,5]
my_list
```

```{code-cell} ipython3
type(my_list)
```

```{code-cell} ipython3
my_list[0]
```

```{code-cell} ipython3
i = 0
my_list[i:i+1]
```

空列表：

```{code-cell} python
[]
```

## 元组

不可变的有序表

```{code-cell} ipython3
my_tuple = (1,2,3,4)
my_tuple
```

```{code-cell} ipython3
type(my_tuple)
```

```{code-cell} ipython3
my_tuple[1]
```

空元组：

```{code-cell} python
()
```

## 字符串

有字符组成、有序可按顺序索引。

单行字符串：单引号或者双引号。

```{code-cell} ipython3
"1234"
```

```{code-cell} ipython3
'1234'
```

```{code-cell} ipython3
type("type")
```

多行字符串：三个单引号或者三个双引号。

```{code-cell} ipython3
my_str = """my love
Python"""
print(my_str)
```

```{code-cell} ipython3
my_str2 = '''
my love
Python
'''
print(my_str2)
```

空字符串：

```{code-cell} ipython3
""
```

## 字典

由键值对（key-value）组成，可以通过键（key）查询值（value）。

创建一个字典：

```{code-cell} python
my_dict = {"key1":1, "key2":2}
my_dict
```

创建一个空字典：

```{code-cell} python
empty_dict = {}
empty_dict
```

查看字典的类型：

```{code-cell} python
my_dict = {"key1":1, "key2":2}
type(my_dict)
```

访问字典中的值可以使用键名：

```{code-cell} python
my_dict = {"key1":1, "key2":2}
my_dict['key1']
```

如果你想在字典中添加一个新项，可以使用键名为索引，并将值赋给它：

```{code-cell} python
my_dict = {"key1":1, "key2":2}
my_dict['key3'] = 0.4
my_dict
```

## 集合

自动去重复值，类似于数学上的集合

```{code-cell} ipython3
{4, 2, 3, 4, 5, 1, 'd', 'b', 'c'}
```

```{code-cell} ipython3
type({1,3,4})
```

空集合：

```{code-cell} ipython3
set()
```

## 空值

- 空值是一个单独的数据类型，一个特殊的值，用来表示空的情况
- 空值不是0、空字符串、空列表、空字典、空集合等等
- 关于空值和其他”空XX“的使用将会在后续章节中详细讨论

```{code-cell} ipython3
None
```
