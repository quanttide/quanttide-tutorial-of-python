# 错误和异常

异常指在程序运行过程中发生的异常事件，通常是由外部问题（如硬件错误、输入错误）所导致的。

## 常见异常

### SyntaxError

```{code-cell} ipython3
print "test"
```

```{code-cell} ipython3
len "gege"
```

### IndentationError

```{code-cell} ipython3
for i in range(10):
print("test")
```

### KeyboardInterrupt

```{code-cell} ipython3
import time
time.sleep(100)
```

### NameError

```{code-cell} ipython3
name
```

### AttributeError

```{code-cell} ipython3
'my_string'.list()
```

```{code-cell} ipython3
'my_string'.len
```

### KeyError

```{code-cell} ipython3
my_dict = {"gege": "gege"}
my_dict['key']
```

### TypeError

```{code-cell} ipython3
1 + "3"
```

```{code-cell} ipython3
list(1)
```

### ValueError

```{code-cell} ipython3
int('99 years')
```

### ImportError

```{code-cell} ipython3
from pandas import qt
```

### ModuleNotFoundError

```{code-cell} ipython3
import numpyt
```

```{code-cell} ipython3
assert 1>2, "此处为提示语"
```

```{code-cell} ipython3
if a>b:
    print(a,b)
else:
    raise Exception("错误了")
```

## 异常处理

Python中用try-except语句处理异常，语法格式为

```python
try:
    <statement>
except <Exception> as e:
    <other statement>
```

举个例子：

```{code-cell} ipython3
my_dict = {'tttt':'ffff'}
try:
    my_dict['key']
except KeyError as e:
    print(e)
```

## 参考资料

- [Python官方文档](https://docs.python.org/3/library/exceptions.html)
