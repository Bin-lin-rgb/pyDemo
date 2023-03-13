from time import sleep
from selenium.webdriver.common.by import By
from base_page import BasePage


class ProfilePage(BasePage):
    # 定位器

    # 定位到要悬停的元素
    dropdown = (By.XPATH, '//*[@id="app"]/header[1]/div/div[2]/div[4]')
    # 下拉的元素
    dropdown_menu = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/ul')
    dropdown_menu_person = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/ul/li[2]')

    edit_btn = (By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div[1]/div[2]/div/div/div/button/span')

    username = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[3]/div[2]/div/input')
    position = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[5]/div[2]/div/input')
    company = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[7]/div[2]/div/input')
    personal_profile = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[9]/div[2]/div/input')
    introduction = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[11]/div[2]/textarea')

    ok_btn = (By.XPATH, '/html/body/div[1]/div/section/section/main/div/div[12]/button')

    def edit_profile(self, params):
        sleep(1)
        # 创建 ActionChains 对象并移动到元素上
        self.hover(self.dropdown)
        # 等待下拉菜单出现
        sleep(1)
        # 点解 个人按钮
        self.click(self.dropdown_menu_person)

        self.click(self.edit_btn)
        # 写入职位
        self.send_keys(self.username, params[0])
        self.send_keys(self.position, params[1])
        self.send_keys(self.company, params[2])
        self.send_keys(self.personal_profile, params[3])
        self.send_keys(self.introduction, params[4])

        # 点击确定
        self.click(self.ok_btn)

        sleep(2)
        self.refresh()
        sleep(2)

    def get_profile_info(self):
        # 避免 get_property 获取两倍值
        sleep(3)
        username = self.get_input_value(self.username)
        position = self.get_input_value(self.position)
        company = self.get_input_value(self.company)
        personal_profile = self.get_input_value(self.personal_profile)
        introduction = self.get_input_value(self.introduction)
        profile_info = [username, position, company, personal_profile, introduction]
        return profile_info



