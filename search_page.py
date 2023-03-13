from selenium.webdriver.common.by import By
from base_page import BasePage


class SearchPage(BasePage):

    # 定位器
    search_box_locator = (By.ID, 'kw')
    search_button_locator = (By.ID, 'su')
    search_result_locator = (By.XPATH, '/html/body/div[2]/div[3]/div[1]/div[3]')

    def search(self, keyword):
        self.send_keys(self.search_box_locator, keyword)
        self.click(self.search_button_locator)

    def get_search_results(self):
        return self.wait_for_element(self.search_result_locator).text

