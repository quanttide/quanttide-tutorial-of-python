# Python的控制语句

本讲主要对基本控制语句进行了一些说明，对于每个语句的详细细节以及应用方法将在第二章中阐述。

教学目标：

- 理解什么是条件语句、如何使用if语句。
- 理解什么是循环语句、如何使用for语句和while语句。

特别注意：

- Python中使用四个空格来表达"子代码块"这一逻辑，使用复合语句时注意空格！！
- Python专用编辑器通常会自动帮助空格，尽管如此依然要注意。

## 条件语句

条件语句是判断给定的条件是否满足(表达式值是否为0)，并根据判断的结果(真或假)决定执行的语句。

选择结构用条件语句来实现。

### if语句

```{code-cell} ipython3
a = 16
if a>10:
    print("我是一个小可爱")  # 子代码块，四个空格开头
```

### if...else...语句

```{code-cell} ipython3
b = 3
if b>5:
    print("我是一个沙雕网友")
else:
    print("你才是沙雕网友！你全家都是！")
```

### if...elif...else语句

```{code-cell} ipython3
x = 10
if x>6:
    print("x比6大")
elif x==6:
    print("x等于6")
else:
    print("x比6小")
```

## 循环语句

循环语句是在程序中只出现一次，但可能会连续运行多次的代码。

### for循环

for循环是指定次数的循环。

```{code-cell} ipython3
for i in range(0, 5):
    print(i)
```

`range(0,5)`表示从`0`到`5-1`。关于`range`的详细用法会在后面的部分详细阐述。

### while循环

while循环是指定条件的循环。

```{code-cell} ipython3
i = 1
while True:
    print(i)
    i+=1
    if (i>=5):
        break
```
