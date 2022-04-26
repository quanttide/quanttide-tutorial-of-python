# 字典排序和比较

## 使用max或sorted的key参数

假设我们有一个批量下载很多大小不一的文件的程序，我们希望在调试时把最大的一个或者多个文件取出尝试。我们可以使用max或者sorted的key参数帮助我们。

我们首先模拟一个文件信息列表。

```python
import random

file_list = [{"file_name": f"name{i}", "file_size": random.randint(1, 1000000)}
for i in range(1000)]
```

我们尝试print前十个看看它长什么样子。


我们希望拿出最大的一个来试试。

max例子。


我们如果希望拿最大的10个呢？

sorted的例子。


作业题：

{file name: {content-length: 6}}
