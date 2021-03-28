from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from seleniumpo.page.add_member import AddMemberPage
from seleniumpo.page.base_page import BasePage

class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    def goto_add_member(self):

        """
        添加成员
        :return:
        """
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)
