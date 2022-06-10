# 临时文件

主要使用`tempfile`库。

## `TemporaryFile`和`TemporaryDirectory`

```python
from tempfile import TemporaryDirectory

tmp_dir = TemporaryDirectory()

# do something

tmp_dir.cleanup()
```

## 参考资料

- https://docs.python.org/zh-cn/3/library/tempfile.html
