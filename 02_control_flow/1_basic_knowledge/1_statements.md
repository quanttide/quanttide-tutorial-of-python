# 语句

语句：可以单独执行的、能够产生实际效果的代码。

简单语句：简单语句由一个单独的逻辑行构成。

```{code-cell} ipython3
print("Hello, world!")    
```

复合语句：复合语句是包含其它语句的语句。

```{code-cell} ipython3
for i in range(10):
    print(i, end=' ')
```

Python中的简单语句和复合语句都有很多种，后续会逐步介绍，下面先介绍最基础的两种语句，表达式语句和赋值语句。

## 表达式语句

表达式：包含在语句中，根据某种条件计算出**一个值或得出某种结果**，然后由语句去判断和处理的代码

```{code-cell} ipython3
1 + 1
```

## 赋值语句

赋值：将名称（重）绑定到特定值，以及修改属性或可变对象的成员项

```{code-cell} ipython3
a = 1
```

`a`是变量，`=`是赋值。`a=1`是把`1`赋值给变量`a`。