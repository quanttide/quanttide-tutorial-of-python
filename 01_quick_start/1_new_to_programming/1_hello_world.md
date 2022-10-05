---
author: 张果
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Hello, World

```{code-cell} python
print("Hello, World!")
```

这里使用的是交互式Python解释器，结果会输出到控制台上。

(解释说明，程序=输入（hello world）->处理（print）->输出（打印出来的结果）)

(进一步给一个可以调节输入的例子。)

```{code-cell} python
my_name = "QuantTide"
print(f"Hello, {my_name}")
```

(异常情况举例)

(括号误输入中文)

```{code-cell} python
print（"Hello, World!"）
```

(误使用中文引号)

```{code-cell} python
print(“Hello, World!”)
```

(异常情况解释)
