from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# expected_conditions 是 WebDriverWait 类中的一个子模块，它包含了许多用于等待页面元素出现或某些条件成立的方法。
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        # presence_of_element_located: 表示等待页面元素出现在DOM中，但不一定可见，直到找到该元素或等待超时。
        # visibility_of_element_located: 表示等待指定的元素在页面中可见。
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        # 显性等待: 等待元素显示再执行 click()
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text.strip())

    def hover(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def switch_to_new_window(self, page=1):
        current_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        if len(handles) < page:
            raise ValueError("Invalid page number")
        new_handle = handles[page - 1]
        if new_handle == current_handle:
            raise ValueError("New window is the same as current window")
        self.driver.switch_to.window(new_handle)

    def refresh(self, timeout=10):
        self.driver.refresh()
        # 这里指定了<body>标签，因为这是页面中最后加载的元素之一。
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def get_input_value(self, locator):
        element = self.wait_for_element(locator)
        # return element.get_attribute("value")
        return element.get_property("value")

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        # arguments[0]: 引用 element 参数
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
