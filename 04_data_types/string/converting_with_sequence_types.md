# 序列类型的相互转换

这里先举一些比较简单的例子，详细的处理在后面的章节讲。

字符串转列表：

```{code-cell} ipython3
list('1234')
```

字符串转元组：

```{code-cell} ipython3
tuple('1234') 
'brand\nmodel'.split('\n') 
```

列表/元组转字符串：

```{code-cell} ipython3
print('\n'.join(['a','b','c','d']))
```
