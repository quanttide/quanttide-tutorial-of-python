# 2.1 Hello, World!


## 从"Hello, world!"开始


- 输出 “Hello, world”


```python
print("Hello, world!")
```

    Hello, world!
    gegersg


这里使用的是交互式Python解释器，结果会输出到控制台上。

## 语句


- 语句：可以单独执行的、能够产生实际效果的代码

- 简单语句：简单语句由一个单独的逻辑行构成。


```python
print("Hello, world!")    
```

    Hello, world!
    hello!


- 复合语句：复合语句是包含其它语句的语句。


```python
for i in range(10):
    print(i, end=' ')
```

    0 1 2 3 4 5 6 7 8 9 

- Python中的简单语句和复合语句都有很多种，后续会逐步介绍，下面先介绍最基础的两种语句，表达式语句和赋值语句。

### 表达式语句

- 表达式：包含在语句中，根据某种条件计算出**一个值或得出某种结果**，然后由语句去判断和处理的代码


```python
1 + 1
```




    2



### 赋值语句

- 赋值：将名称（重）绑定到特定值，以及修改属性或可变对象的成员项


```python
a = 1
```

- `a`：变量
- `=`：赋值
- `a=1`：把1赋值给变量a


## 注释

- 用于在源代码中解释代码的功用，可以增强程序的可读性，可维护性；
- 用于在源代码中处理不需运行的代码段，来调试程序的功能执行。


```python
# 这是一行没什么卵用并且不会对程序有任何影响的注释
# print("这是一行有用但是不会运行的代码")
print("这才是有用的信息") 
```

    这才是有用的信息


## 运算符

- 执行特定的**数学**或**逻辑**操作的符号

### 算术运算符


- 加法


```python
1+1
```




    2



- 减法


```python
1334-2435
```




    -1101



- 乘法


```python
134*243.5
```




    32629.0



- 除法


```python
123/34
```




    3.6176470588235294



- 取整


```python
123.5//34
```




    3.0



- 取余


```python
123%34
```




    21



- 乘方


```python
12**4
```




    20736



- 注意：`^`在Python中是位运算符，和二进制运算有关，不常用。

- 开方


```python
2**(1/2)
```




    1.4142135623730951



### 比较运算符


```python
1>(0+3)
```




    False




```python
1 >= 0
```




    True




```python
1<0
```




    False




```python
1<=0
```




    False




```python
1 == 0
```




    False



### 逻辑运算符

- `and`："与"，两个条件都成立结果为真


```python
a = 1
b = 3
c = 3
(a>b) and (b<c) or ('gege'=='gegege')
```




    False



- `or` ："或"，两个条件至少有一个条件成立结果为真


```python
(0<1) or (1<0)
```




    True



- `not`："非"，本来值的反值


```python
not (0<1)
```




    False



### 成员运算符


```python
'in' in 'integer'
```




    True




```python
'out' not in 'find'
```




    True



## 延伸阅读：`print`表达式

实际上，`print()`也是一个表达式
- 在`print`函数被调用的时候，对象的`__str__`方法被调用，把输入值输出到屏幕上；
- 表达式直接在解释器中运行的时候，对象的`__repr__`方法被调用，把表达式的结果输出到屏幕上；如果结果为None，则无任何输出。


```python
result = print("Hello,world!")
result
```

    Hello,world!



```python
result = 1
result
```




    1


