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

下面列举一些操作技巧。

## 一个Pickle文件连续存储多个变量

```python
>>> mystring2 = '这是又一段中文'
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring, f)
>>> pickle.dump(mystring2, f)
>>> f.close()
>>> f = open('test.pickle', 'rb')
>>> pickle.load(f)
'这是一段中文'
>>> pickle.load(f)
'这是又一段中文'
>>> f.close()
```

使用`ab`格式也同样可行：

```python
>>> f = open('test.pickle', 'wb')
>>> pickle.dump(mystring, f)
>>> f.close()
>>> f = open('test.pickle', 'ab')
>>> pickle.dump(mystring2, f)
>>> f.close()
>>> f = open('test.pickle', 'rb')
>>> pickle.load(f)
'这是一段中文'
>>> pickle.load(f)
'这是又一段中文'
>>> f.close()
```

## 写入后不关闭文件直接读取

```python
>>> f = open('test.pickle', 'wb+')
>>> pickle.dump(mystring, f)
>>> f.seek(0)
0
>>> pickle.load(f)
'这是一段中文'
>>> f.close()
```

但从代码规范的角度，不建议采用不关闭文件直接读取的操作。

## 使用二进制格式读写

注意文件读写**必须**使用二进制格式，如`wb`和`rb`。

如果使用`w`格式写入，则会报错：

```python
>>> f = open('test.pickle', 'w')
>>> pickle.dump(mystring, f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: write() argument must be str, not bytes
>>> f.close()
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
