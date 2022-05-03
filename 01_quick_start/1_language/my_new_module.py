# -*- coding: utf-8 -*-
"""
@author: Guo Zhang
@email: zhangguo@quanttide.com

This is a module that ...

Ref:
    - https://www.quanttide.com
"""

# ----- 导入模块 ------

# 标准库
import math
import os
from math import sqrt, sin

# 第三方库
# pip install requests
import requests

# from django.db import models

# 自定义库
from my_package.my_module import main


# ----- 全局变量（模块内）-----

ROOT_URL = 'www.baidu.com'

my_data = math.sqrt(5)


# ----- 函数 -----

def func():
    """
    这是函数注释
    @param data:
    
    @return
    """
    # 这是一段干啥啥的代码
    print("Hello, world!")  # 这是一个做啥啥的东西


# ----- 类 -----

class MyClass():
    """
    这是类注释
    ...
    """
    def __init__(self):
        pass
    
    # ---- ..... -----
    def func(self):
        """
        """
        pass


# ----- 调用 -----

if __name__=="__main__":
    func()
