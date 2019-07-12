from selenium import webdriver
import time


# driver = webdriver.Chrome()
class Login():
    def get_url(self, url):
        # 加载指定网页
        self.driver = webdriver.Chrome()  # 因为已经将path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'添加到了系统变量，所以不用填写执行路径
        self.driver.get(url)
        self.driver.maximize_window()
        title = self.driver.title
        print(title)

        # 开始登录
        # 1. 用户名

    def login(self, userphone, pwd, username):
        tc_account = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div[1]/input')
        tc_account.clear()
        tc_account.send_keys(userphone)
        # 2. 密码
        tc_password = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div[1]/input')
        tc_password.clear()
        tc_password.send_keys(pwd)
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
        Login_msg = str("欢迎，" + username)
        if login_name == Login_msg:
            print("Test Login PASS")
        else:
            print("Test Login Failed")
            self.driver.quit()

    def logout(self):
        self.driver.quit()


t = Login()
t.get_url("http://test-scm.fengdai.org/scm/index.html#/login")
t.login('18012345678', 'Aa123456', 'admin')
t.logout()
