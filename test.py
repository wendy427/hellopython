import unittest


class DemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("call setUpClass()")

    ## 每一个测试开始前的预置条件
    def setUp(self):
        print("call setUp()")

    ## 每一个测试结束以后的清理工作
    def tearDown(self):
        print("call tearDown()")

    ## 测试一（务必以test开头）
    def test_01(self):
        print("call test_01()")
        pass

    ## 测试三（务必以test开头）
    def test_02(self):
        print("call test_02()")
        pass

    ## 测试三（务必以test开头）
    def test_03(self):
        print("call test_03()")
        pass

    ## tearDownClass方法是执行完所有测试后调用的方法
    ## 是测试结束后的清除工作
    @classmethod
    def tearDownClass(cls):
        print("call tearDownClass()")


# 执行测试主函数
if __name__ == '__main__':
    ## 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)
