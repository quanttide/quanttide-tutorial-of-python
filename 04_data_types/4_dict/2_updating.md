# 更新字典

## 更新值

可以直接通过键来修改字典中的值。例如：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 修改字典中的值
my_dict["apple"] = 0.6
print(my_dict) # {"apple": 0.6, "banana": 0.25, "orange": 0.75}
```

如果你要向字典中添加一个新的键值对，也可以直接赋值：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 添加一个新的键值对
my_dict["pear"] = 0.3
print(my_dict) # {"apple": 0.5, "banana": 0.25, "orange": 0.75, "pear": 0.3}
```

## 删除键值对

如果你要删除字典中的一个键值对，可以使用`del`关键字：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 删除一个键值对
del my_dict["banana"]
print(my_dict) # {"apple": 0.5, "orange": 0.75}
```

## 整体更新字典

字典中也提供了`update()`方法,它可以用来更新或新增字典中的键值对。
在使用`update()`方法时,如果键值对已经存在,则会更新对应的值,否则会新增键值对。
例如：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 使用update()方法更新字典
my_dict.update({"apple": 0.6, "pear": 0.3})
my_dict
```

`apple`的值更新为了`0.6`，同时新增了值为0.3的`pear`。

要特别注意，`update()`的返回值是空，而不是更新后的字典。

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 使用update()方法更新字典
result = my_dict.update({"apple": 0.6, "pear": 0.3})
result
```
