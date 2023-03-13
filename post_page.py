from time import sleep
from selenium.webdriver.common.by import By
from base_page import BasePage


class PostPage(BasePage):
    # 定位器

    # 定位到要悬停的元素
    dropdown = (By.XPATH, '//*[@id="app"]/header[1]/div/div[2]/div[4]')
    # 下拉的元素
    dropdown_menu = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/ul')
    dropdown_menu_write = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/ul/li[1]')
    dropdown_menu_person = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div/ul/li[2]')

    title = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/input')
    content = (By.ID, 'md-editor-v3-textarea')
    post_btn = (By.XPATH, '/html/body/div[1]/div[1]/button[2]/span')
    read_btn = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/label[8]/span[2]')
    ok_btn = (By.XPATH, '/html/body/div[1]/div[3]/div[2]/button[1]/span')
    back_btn = (By.XPATH, '/html/body/div[1]/div/div/div[4]/button/span')

    home_img = (By.XPATH, '/html/body/div[1]/header/div/h1/img')
    first_article = (By.XPATH, '/html/body/div[1]/div/section/main/ul/li[1]')
    heading_4 = (By.XPATH, '/html/body/div[1]/div/div/section/main/div/div[2]/div[1]/div/div/h4[3]')

    def post(self, title, content):
        sleep(1)
        # 创建 ActionChains 对象并移动到元素上
        self.hover(self.dropdown)
        # 等待下拉菜单出现
        sleep(1)
        # 点解 写文章按钮
        self.click(self.dropdown_menu_write)

        # 此时需要切换句柄
        self.switch_to_new_window(2)
        # 写入标题
        self.send_keys(self.title, title)
        # 写入内容
        self.send_keys(self.content, content)
        # 点击发布
        self.click(self.post_btn)
        sleep(1)
        self.click(self.read_btn)
        sleep(1)
        self.click(self.ok_btn)
        sleep(1)

        # 点击返回
        self.click(self.back_btn)

        # 主页
        self.click(self.home_img)
        # 点击第一篇刚发的文章
        self.click(self.first_article)
        # 定位到 heading4
        sleep(3)
        self.scroll_to_element(self.heading_4)


