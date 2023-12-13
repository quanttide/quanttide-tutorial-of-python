# 单元测试

假设我们在`mycode.py`有如下代码：

```python
# mycode.py
def my_function(arg1, arg2):
    return arg1 + arg2 * 2
```

我们实现一个测试模块`test_mycode.py`，注意模块名要带`test`，方便被自动发现。

```python
# test_mycode.py
import unittest

# 导入待测试函数
from mycode import my_function


# 继承`unittest.TestCase`类才是单元测试用例
class MyTestCase(unittest.TestCase):
    # `test`开头的会被识别为单元测试
    def test_my_function(self):
        # 测试数据
        expected_result = 10
        # 执行
        actual_result = my_function(4, 4)
        # 验证
        # unittest官方文档没有要求先后顺序，不过是把`expected_result`写第二个。
        # PyCharm把第一个作为`expected_result`进行识别，建议遵循，原因见本文参考资料。
        self.assertEqual(expected_result, actual_result)


# 运行单元测试
# 在PyCharm里可以配置运行Python测试
if __name__=="__main__":
    unittest.main()
```

## 参考资料

- [`unittest`官方文档](https://docs.python.org/zh-cn/3/library/unittest.html)
- [Why are assertEquals() parameters in the order (expected, actual)?](https://stackoverflow.com/questions/2404978/why-are-assertequals-parameters-in-the-order-expected-actual)
