---
author: 张果
created_at: "2022-05-27"
updated_at: "2022-05-27"
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

# 输入和输出

## 从"Hello, World!"开始

- 输出 “Hello, World”

```{code-cell} ipython3
print("Hello, World!")
```

这里使用的是交互式Python解释器，结果会输出到控制台上。

## 语句

- 语句：可以单独执行的、能够产生实际效果的代码
- 简单语句：简单语句由一个单独的逻辑行构成。

```{code-cell} ipython3
print("Hello, world!")    
```

- 复合语句：复合语句是包含其它语句的语句。

```{code-cell} ipython3
for i in range(10):
    print(i, end=' ')
```

- Python中的简单语句和复合语句都有很多种，后续会逐步介绍，下面先介绍最基础的两种语句，表达式语句和赋值语句。

### 表达式语句

- 表达式：包含在语句中，根据某种条件计算出**一个值或得出某种结果**，然后由语句去判断和处理的代码

```{code-cell} ipython3
1 + 1
```

### 赋值语句

- 赋值：将名称（重）绑定到特定值，以及修改属性或可变对象的成员项

```{code-cell} ipython3
a = 1
```

- `a`：变量
- `=`：赋值
- `a=1`：把1赋值给变量a

## 注释

- 用于在源代码中解释代码的功用，可以增强程序的可读性，可维护性；
- 用于在源代码中处理不需运行的代码段，来调试程序的功能执行。

```{code-cell} ipython3
# 这是一行没什么卵用并且不会对程序有任何影响的注释
# print("这是一行有用但是不会运行的代码")
print("这才是有用的信息") 
```

## 运算符

- 执行特定的**数学**或**逻辑**操作的符号

### 算术运算符

- 加法

```{code-cell} ipython3
1+1
```

- 减法

```{code-cell} ipython3
1334-2435
```

- 乘法

```{code-cell} ipython3
134*243.5
```

- 除法

```{code-cell} ipython3
123/34
```

- 取整

```{code-cell} ipython3
123.5//34
```

- 取余

```{code-cell} ipython3
123%34
```

- 乘方

```{code-cell} ipython3
12**4
```

- 注意：`^`在Python中是位运算符，和二进制运算有关，不常用。

- 开方

```{code-cell} ipython3
2**(1/2)
```

### 比较运算符

```{code-cell} ipython3
1>(0+3)
```

```{code-cell} ipython3
1 >= 0
```

```{code-cell} ipython3
1<0
```

```{code-cell} ipython3
1<=0
```

```{code-cell} ipython3
1 == 0
```

### 逻辑运算符

- `and`："与"，两个条件都成立结果为真

```{code-cell} ipython3
a = 1
b = 3
c = 3
(a>b) and (b<c) or ('gege'=='gegege')
```

- `or` ："或"，两个条件至少有一个条件成立结果为真

```{code-cell} ipython3
(0<1) or (1<0)
```

- `not`："非"，本来值的反值

```{code-cell} ipython3
not (0<1)
```

### 成员运算符

```{code-cell} ipython3
'in' in 'integer'
```

```{code-cell} ipython3
'out' not in 'find'
```

## 延伸阅读：`print`表达式

实际上，`print()`也是一个表达式。

- 在`print`函数被调用的时候，对象的`__str__`方法被调用，把输入值输出到屏幕上；
- 表达式直接在解释器中运行的时候，对象的`__repr__`方法被调用，把表达式的结果输出到屏幕上；如果结果为None，则无任何输出。

```{code-cell} ipython3
result = print("Hello,world!")
result
```

```{code-cell} ipython3
result = 1
result
```
