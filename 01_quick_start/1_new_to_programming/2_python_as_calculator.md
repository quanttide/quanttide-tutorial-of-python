# 把Python当做计算器

（简单用数字类型、列表、布尔类型，其他的下一讲详细说。）



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

## 运算符

运算符: 执行特定的**数学**或**逻辑**操作的符号。

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
1 in [1,2,3]
```

```{code-cell} ipython3
2 not in [4,5,6]
```
