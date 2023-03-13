from time import sleep
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    # 定位器
    login_bottom = (By.XPATH, '//*[@id="app"]/header[1]/div/div[2]/div[4]/a')
    # 默认复制的 Xpath 是 id，而 id 是变化的，所以使用 placeholder 定位 [或者 copy full Xpath]
    # username_locator = (By.XPATH, '//*[@id="el-id-8011-8"]')
    username_locator = (By.XPATH, '//input[@placeholder="请输入您的用户名"]')
    password_locator = (By.XPATH, '//input[@placeholder="请输入您的密码"]')
    submit_locator = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div/div/div/div/form/div[3]/div/button[1]')

    def login(self, username, password):
        self.click(self.login_bottom)
        self.send_keys(self.username_locator, username)
        self.send_keys(self.password_locator, password)
        self.click(self.submit_locator)
        sleep(3)
