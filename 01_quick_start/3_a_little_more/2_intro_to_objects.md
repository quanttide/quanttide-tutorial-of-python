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

# Python的类和实例

## Python的类(class)

- 属性 vs 方法
- 定义属性：`__init__`
- 定义方法
- `self`是什么？

```{code-cell} ipython3
# 实例
[1,2,3]
```

```{code-cell} ipython3
# 类
list
```

```{code-cell} ipython3
class Person:
    def __init__(self, name, age):
        """
        类的构造器，我们在这里定义实例属性
        """
        # self.<属性> = 参数 or 经过计算
        self.name = name
        self.age = age
        
    def is_adult(self):
        """
        定义实例方法
        """
        if self.age>=18:
            return True
        else:
            return False
        
    def some_method(self, arg):
        return self.name + '_' + str(arg)
    
    def __str__(self):
        return "一个叫做" + self.name + "的人"
    
    def __repr__(self):
        return self.name
```

## Python的实例

```{code-cell} ipython3
# 创建实例
person = Person("小明", 20)
```

```{code-cell} ipython3
# 访问实例属性
person.name
```

```{code-cell} ipython3
person.age
```

```{code-cell} ipython3
# 访问实例方法
# 对象.函数(参数)
person.is_adult()
```

```{code-cell} ipython3
# 带参数
person.some_method('是我兄弟')
```

```{code-cell} ipython3
print(person)
```

```{code-cell} ipython3
person
```

## 练习题

### 练习题1

定义`PrimeList`类，这个类接受传入的参数n(n>=2)，生成从2到n的所有质数。

- data属性以列表形式存储数据。
- 此类可以自定义计算所有列表质数之和。

```{code-cell} ipython3
def is_prime(i):
    """
    判断i是不是质数，返回True/False
    """
    pass

def get_primes(n):
    """
    ?
    """
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


class PrimeList(object):
    def __init__(self, n):
        pass
    
    def my_sum(self):
        pass
```

预期达到的调用效果如下：

```{code-cell} ipython3
prime_list = PrimeList(100)
prime_list.my_sum()
```

### 练习题2

自定义Vector类，实现向量常见的操作，比如加、减、点乘。

参考资料：https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html

```{code-cell} ipython3
class Vector(object):
    def __init__(self, *arg):
        self.arg = arg
    
    def __len__(self):
        return len(self.arg)
    
    def __add__(self, vector2):
        """
        重新定义加法
        """
        data1 = self.arg
        data2 = vector2.arg
        
        assert len(data1) == len(data2), "长度不一致"
        
        result = []
        for i in range(len(self)):
            value = data1[i] + data2[i]
            result.append(value)
        return result
    
    def __sub__(self, vector2):
        """
        重新定义减法
        """
        pass
    
    def __neg__(self):
        """
        重新定义负号
        """
        pass
    
    def dot(self, vector2):
        """
        点积，调用方式为 vector1.dot(vector2)
        """
        pass
    
    def __str__(self):
        return "Vector(" + str(self.data) + ")" 
```

```{code-cell} ipython3
vector1 = Vector(1,2,3)
vector2 = Vector(3,4,5)
vector3 = Vector(3,4,5,6)
```

```{code-cell} ipython3
len(vector1)
```

```{code-cell} ipython3
vector1 + vector2
```

```{code-cell} ipython3
vector1 + vector3
```

```{code-cell} ipython3
vector1 - vector2
```

```{code-cell} ipython3
- vector1
```

```{code-cell} ipython3
vector1.dot(vector2)
```

```{code-cell} ipython3

```

```{code-cell} ipython3
class Person:
    def __init__(self, *arg):
        self.arg = arg
        
    def __len__(self):
        return len(self.arg)
    
    def __add__(self, vector2):
        self.arg
        vector2.arg
        return 
        
person = Person(1,2,3)
len(person)
```

```{code-cell} ipython3
len((1,2,3))
```

```{code-cell} ipython3

```
