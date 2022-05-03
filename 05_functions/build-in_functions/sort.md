---
author: 张果
created_at: 2022-04-27
updated_at: 2022-05-02
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 排序和比较

- `max`、`min`
- `sorted`

## 使用key参数

假设我们有一个批量下载很多大小不一的文件的程序，我们希望在调试时把最大的一个或者多个文件取出尝试。我们可以使用max或者sorted的key参数帮助我们。

我们首先模拟一个文件信息列表。

```{code-cell} ipython
import random

file_list = [{"file_name": f"name{i}", "file_size": random.randint(1, 1000000)}
for i in range(1000)]
```

我们尝试print前十个看看它长什么样子。

```{code-cell} ipython
print(file_list[0:10])
```

我们希望拿出最大的一个来试试。

```python
max(file_list, key=lambda item: item['file_size'])
```

特别注意，这里的`key`需要填一个函数，列表中的元素按照此函数的返回值比较大小。

我们如果希望拿最大的10个呢？

```python
sorted(file_list, key=labmda item: item['file_size'], reverse=True)[0:10]
```

`reverse`参数控制降序或者升序。默认为`False`升序，即从小到大排；我们这里调整成`True`降序，即从大到小排。

## 练习题

假设我们的数据变成了如下结构：

```python
file_dict = {
    'name_1': {'file_size': 10},
    'name_2': {'file_size': 100},
    ...
}
```

如何获取最大的一个或者十个？

## 参考资料

- [Python的max函数](https://www.programiz.com/python-programming/methods/built-in/max)
