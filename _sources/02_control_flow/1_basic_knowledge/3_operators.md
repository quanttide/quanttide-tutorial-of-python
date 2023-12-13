---
level: introductory
stage: alpha
---

# 运算符

运算符: 执行特定的**数学**或**逻辑**操作的符号。

## 算术运算符

（前面已经介绍，这里简单重复一下。）

备注：`^`在Python中是位运算符，和二进制运算有关，不常用。

## 比较运算符

```{code-cell} ipython3
1>(0+3)
```

```{code-cell} ipython3
1 >= 0
```

```{code-cell} ipython3
1<0
```

```{code-cell} ipython3
1<=0
```

```{code-cell} ipython3
1 == 0
```

## 逻辑运算符

`and`："与"，两个条件都成立结果为真

```{code-cell} ipython3
a = 1
b = 3
c = 3
(a>b) and (b<c) or ('gege'=='gegege')
```

`or` ："或"，两个条件至少有一个条件成立结果为真

```{code-cell} ipython3
(0<1) or (1<0)
```

`not`："非"，本来值的反值

```{code-cell} ipython3
not (0<1)
```

## 成员运算符

```{code-cell} ipython3
1 in [1,2,3]
```

```{code-cell} ipython3
2 not in [4,5,6]
```
