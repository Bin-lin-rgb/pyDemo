from selenium import webdriver
from login_page import LoginPage
from profile_page import ProfilePage
from search_page import SearchPage
from post_page import PostPage
from time import sleep
import pytest
import yaml


class TestWeb:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()
        yield driver

    @pytest.fixture(scope="class")
    def login(self, browser):

        login_page = LoginPage(browser)
        login_page.open("http://www.hmzilvok.ltd/")
        browser.maximize_window()
        # 使用 utf-8 编码打开，避免默认 gbk 格式导致 yaml 文件读取失败
        with open('test_data.yaml', encoding='utf-8') as f:
            login_data = yaml.safe_load(f)['login']

        login_page.login(login_data["username"], login_data["password"])

        # yield 语句之前的代码会在测试用例执行之前运行，yield 语句之后的代码会在测试用例执行之后运行。
        yield
        # 在自动化测试中，希望测试用例之间是相互独立的，即一个测试用例的执行不会受到之前或之后测试用例的影响。
        browser.delete_all_cookies()
        # 把 token 也删了
        browser.execute_script("window.localStorage.clear();")

    def test_post(self, browser, login):

        post_page = PostPage(browser)
        post_page.open("http://www.hmzilvok.ltd/")
        with open('test_data.yaml', encoding='utf-8') as f:
            post_data = yaml.safe_load(f)['post']

        # 虽然理论上可以将文章放入 YAML 变量中，但这并不是一个好的做法。
        # YAML 的主要作用是为数据序列化和配置文件提供一种轻量级格式，而不是存储大量文本内容。
        # 所以采用 文件 读取方式获取 content
        with open('content.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        post_page.post(post_data["title"], content)
        # post_page.post(post_data["title"], post_data["content"])
        sleep(5)

    def test_profile(self, browser, login):
        profile_page = ProfilePage(browser)
        profile_page.open("http://www.hmzilvok.ltd/")
        with open('test_data.yaml', encoding='utf-8') as f:
            profile_data = yaml.safe_load(f)['profile']

        params = [profile_data["username"], profile_data["position"], profile_data["company"],
                  profile_data["personal_profile"], profile_data["introduction"]]

        profile_page.edit_profile(params)

        info = profile_page.get_profile_info()
        assert info == params
        sleep(3)

    def test_search(self, browser):
        search_page = SearchPage(browser)
        search_page.open("https://www.baidu.com/")
        with open('test_data.yaml', encoding='utf-8') as f:
            search_data = yaml.safe_load(f)['search']
        search_page.search(search_data["keyword"])
        results = search_page.get_search_results()
        assert search_data["keyword"] in results
        sleep(3)
