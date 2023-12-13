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

# Python的函数

## 本讲大纲

- 定义函数
- 调用函数
- 常见内置函数

## 定义函数

### `def`

- 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
- 函数内容以' : '起始，并且缩进
- 可以不带参数，可以多个参数

### `return`

- return有结束函数的作用
- 有return [表达式](如下列例子中的 return result) 才可以返回函数执行结果。
- 不带表达式的return相当于返回 None。
- 可以同时以元组的方式返回多个值

```{code-cell} ipython3
# 例1.有return有表达式的函数
def power(n):
    """
    n!
    """
    result = 1
    for i in range(1,n+1):
        result *= i
    if result>0:
        return result
    else:
        print(result)


power(10)
```

```{code-cell} ipython3
# 例2.有return无表达式的函数
def power(n):
    result = 1
    for i in range(1,n+1):
        result *= i

power(10)
```

```{code-cell} ipython3
# 例3.没有return的函数
def sqrt(s):
    print(s)
    pass
    print(s+1)

sqrt(4)
```

### 练习1

定义函数my_sum，当a>5时，计算a+b*2，当a<3时，计算a+b*4，其他情况计算a+b*3

```{code-cell} ipython3
def f(a,b):

    a = float(a)
    b = float(b)    
        
    if a>5:
        return a + b*2
    elif a<3:
        return a + b*4
    else:
        return a + b*3

    
f('1.1', '1.2')
```

## 调用函数

- 调用先前定义的三个函数，观察结果

```{code-cell} ipython3
power(10)
```

```{code-cell} ipython3
sum(10)
```

```{code-cell} ipython3
sqrt(4)
```

return和print都可以返回值，但只有return才可以保留结果

对比下列两个函数的语句及结果

```{code-cell} ipython3
def odd(x):
   if x%2 != 0:
        return x
   else:
        return 0

odd(3)+odd(4)
```

```{code-cell} ipython3
def odd(x):
   if x%2 != 0:
        print(x)
   else:
        print(0)
        
odd(3) + odd(4)
None + None
```

## 常见内置函数

```{code-cell} ipython3
# len()函数
len([1,3,4,5,7])
```

```{code-cell} ipython3
# sum()函数
sum([1,3,4,5,7])
sum((1,3,4,5,7))
```

```{code-cell} ipython3
# abs()函数   求绝对值
abs(-1)
```

```{code-cell} ipython3
# int()函数   向下取整
int(5.7)
```

```{code-cell} ipython3
# str()函数   将对象转化为字符串
str(5+3)
```

```{code-cell} ipython3
# print()函数   打印
print('Hello, world')
```

```{code-cell} ipython3
# input()函数   接受键盘输入，返回输入对象
a=input('请输入一个整数')
print(a)
```

```{code-cell} ipython3
# round(a,b)  对a进行四舍五入，保留b位小数 （该方法不可靠，不推荐使用）
round(10.3)
```

```{code-cell} ipython3
a = input("请输入一个Python语句")
eval(a)    #计算字符串中表达的值并返回
```

## 友情链接

- 关于Python函数的深入用法，请参见"Python函数和函数式编程"一章。
- 关于函数式编程的详细内容，请参见"Python函数和函数式编程"一章。

## 本讲作业

1.请定义一个函数，输出‘开始做作业’

2.请定义一个函数，接收两个参数，返回较大的数字

3.请定义一个函数，接受一个由数字组成的列表，返回该列表的平均值

3.请定义一个函数，判断一个数是否为素数，然后调用该函数输出100以内的素数

```{code-cell} ipython3
def avg(numbers):
    return sum(numbers)/len(numbers)

avg([1,3,5,6,9])
```

```{code-cell} ipython3
def is_not_prime(n):
    for i in range(2, n+1):
        _is_prime = 1
        for j in range(2, i):
            if (i % j == 0):
                _is_prime = 0
                break
        if not _is_prime:
            print(i)        
        
is_not_prime(100)
```

```{code-cell} ipython3

```
