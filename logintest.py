from selenium import webdriver
import time
import unittest

# chrome_drive = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'


class TestLogin(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=option)
        # 加载指定网页
        self.driver.get("http://test-scm.fengdai.org/scm/index.html#/login")
        self.driver.maximize_window()

    def test_login(self):
        title = self.driver.title
        print(title)
        # 开始登录
        # 1. 用户名
        tc_account = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input')
        tc_account.clear()
        tc_account.send_keys("18012345678")
        # 2. 密码
        tc_password = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input')
        tc_password.clear()
        tc_password.send_keys("Aa123456")
        # 2. 验证码
        tc_password = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div[1]/input')
        tc_password.clear()
        tc_password.send_keys("1111")
        # 3. 登录
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[4]/div/div/div[1]/button/span').click()
        time.sleep(3)
        # 登录成功断言
        self.driver.get_screenshot_as_file("D:\\py\\test.png")
        login_name = self.driver.find_element_by_class_name('text_hide').text
        print(login_name)
        Login = str("欢迎，admin")
        self.assertEqual(login_name, Login, msg='登录失败')

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
