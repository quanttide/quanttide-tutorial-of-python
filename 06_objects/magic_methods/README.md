# 魔术方法

> Magic methods are special methods in python that have double underscores (dunder) on both sides of the method name. Magic methods are predominantly used for operator overloading. Operator overloading means provided additional functionality to the operators, the python implicitly invokes the magic methods to provide additional functionality to it. For example, multiplying two integers can be done using the multiplying operator (2*3 = 6) and the same operator can be used to repeat the string (“apple- ” * 3 = ‘apple- apple- apple’).
> Some examples of magic methods are __init__, __len__, __repr__, __add__, and etc.

## `print`相关

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

## 参考资料

- https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/
