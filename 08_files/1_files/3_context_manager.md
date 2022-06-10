# 上下文管理器

上下文管理器主要通过自定义魔术方法`__enter__`和`__exit__`实现。

> __enter__ and __exit__ methods are used along with the ‘with’ block in python. The ‘with’ block in python is used to open and close the file object or any other objects that have a close method.

## `__exit__`方法

```python
def __exit__（type, value, trace):
    return None
```

用于捕获异常。除了 self 之外，必须传入另外三个参数val,type 和 trace，分别表示 exception 的类型，值（如 IndexError: list index out of range 中，冒号后面的部分就是值），以及 traceback。

它的返回值是一个 boolean 对象:

- 返回 `True` 则表示这个异常被忽略。
- 返回 `None`, `False` 等则这个异常会抛出。

## 工具包`contextlib`

`contextlib.AbstractContextManager`

## 参考资料

- https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/
- https://blog.csdn.net/qq_35462323/article/details/100886654
- https://docs.python.org/3/library/contextlib.html
- https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers
