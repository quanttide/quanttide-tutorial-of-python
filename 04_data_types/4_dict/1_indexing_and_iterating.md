# 索引和遍历字典

## 索引

字典是通过键来索引的。你可以使用键名作为索引访问字典中的值。例如：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
# 访问字典中的值
price = my_dict["apple"]
print(price) # 0.5
```

你也可以使用 `get()` 方法来访问字典中的值。这个方法会返回一个键的值，如果该键不存在，则返回 `None` 或者你自己定义的值。例如：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 使用get()方法访问字典中的值
price = my_dict.get("apple", "not found")
print(price) # 0.5

# 访问不存在的键
price = my_dict.get("pear", "not found")
print(price) # "not found"
```

如果想同时从字典里抛出键值，可以使用`pop`方法。例如：

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 使用pop()方法抛出字典中的值
price = my_dict.pop("apple", "not found")
print(my_dict)
print(price) # 0.5

# 访问不存在的键
price = my_dict.pop("pear", "not found")
print(price) # "not found"
```

## 检查索引是否存在

如果你不确定一个键是否存在于字典中，你可以使用`in`关键字来检查。例如：

```{code-cell} ipython3
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 检查键是否存在
if "apple" in my_dict:
    my_dict['apple']
else:
    print("字典里没有apple")
```

等价于：

```{code-cell} ipython3
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 等价的try-except语句
try:
    my_dict['apple']
except KeyError:
    print("字典里没有apple")
```

## 遍历

如果你需要遍历字典中的所有键和值，可以使用 items() 方法返回键值对的迭代器。

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

for key, value in my_dict.items():
    print(key, value)
```

如果需要只遍历键或者值，也可以使用`keys()`或`values()`方法。

```{code-cell} python
my_dict = {"apple": 0.5, "banana": 0.25, "orange": 0.75}

# 遍历字典中的键
for key in my_dict.keys():
    print(key)

# 遍历字典中的值
for value in my_dict.values():
    print(value)
```
