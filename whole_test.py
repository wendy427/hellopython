import unittest
from fk_math_test import TestFkMath
from hello_py_test import TestHello
from Lib.HTMLTestRunner import HTMLTestRunner
import os
import time

test_cases = (TestHello, TestFkMath)


def whole_suite():
    # 创建测试加载器
    loader = unittest.TestLoader()
    # 创建测试包
    suite = unittest.TestSuite()
    # 遍历所有测试类
    for test_class in test_cases:
        # 从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(test_class)
        # 将测试用例添加到测试包中
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    # 创建测试运行器（TestRunner）
    runner = unittest.TextTestRunner(verbosity=2)
    rq = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.dirname(os.path.abspath('.')) + '\\test_report\\' + rq + '-result.html'
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    #  开始执行测试套件
    runner.run(whole_suite())
    fp.close()
