# 字典索引

## 索引是否存在

```{code-cell} ipython3
my_dict = {'tttt':'ffff'}
try:
    my_dict['key']
except:
    print("没有key")
```

等价于：

```{code-cell} ipython3
if 'key' in my_dict:
    print(my_dict['key'])
else:
    print("没有key")
```