# 基类，存放__int__,find
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    def __init__(self, driver:WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # option = webdriver.ChromeOptions()
            # option.binary_location = r'C:\Users\zxw\AppData\Local\Google\Chrome\Application'
            # self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,locator, value):
        return self.driver.find_element(locator, value)

    def finds(self,locator, value):
        return self.driver.find_elements(locator, value)

    def wait_for_click(self, timeout,locator):
        # 显示等待
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))