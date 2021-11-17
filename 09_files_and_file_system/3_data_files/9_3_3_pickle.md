# Pickle数据

Pickle是Python官方提供的用来做Python对象缓存的标准库。

它的原理是把Python对象写成二进制格式的文件，需要使用的时候再重新读进程序里。

代码示例：

```python
>>> import pickle
>>> mystring = '这是一段中文'
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring, f)
>>> f.close()
>>> f = open('test.pickle', 'rb')
>>> pickle.load(f)
'这是一段中文'
>>> f.close()
```

下面列举一些常见错误。

## 写入状态时不可读

```python
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring, f)
>>> pickle.load(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: read
```

这里再次体现了关闭文件的必要性。

按照上面的写法`rb`模式打开文件以后是正常的。

## 使用二进制格式读写

注意文件读写使用二进制格式`wb`和`rb`。

如果使用`w`格式写入，则会报错：

```python
>>> f = open('test.pickle', 'w')
>>> pickle.dump(mystring, f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: write() argument must be str, not bytes
```

如果使用`r`格式写入，则会报错：

```python
>>> f = open('test.pickle', 'r')
>>> pickle.load(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/zhangguo/.pyenv/versions/3.9.0/lib/python3.9/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
>>> f.close()
```

## 一个Pickle文件只能存储一个变量

```python
>>> mystring2 = '这是又一段中文'
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring2, f)
>>> f.close()
>>> f = open('test.pickle', 'rb')
>>> pickle.load(f)
'这是又一段中文'
>>> f.close()
```

我们看到数据已经被替换了。

如果我们换成`ab`格式呢？

```python
>>> mystring2 = '这是又一段中文'
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring2, f)
>>> f.close()
>>> mystring3 = '这段中文覆盖前面的'
>>> f = open('test.pickle', 'ab')
>>> pickle.dump(mystring3, f)
>>> f.close()
>>> f = open('test.pickle', 'rb')
>>> pickle.load(f)
'这是又一段中文'
```

依然只有一个，并且是**第一个**写入的。
