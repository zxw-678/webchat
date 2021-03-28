from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpo.page.base_page import BasePage

class AddMemberPage(BasePage):
    def add_member(self, username, account, phonenumber):
        """
        添加联系人
        输入用户名
        输入账号
        输入手机号
        保存
        提交
        :return:
        """
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenumber)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return True
    def get_member(self):
        """
        获取所有的联系人姓名
        :return:
        """
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10,locator)
        eles_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute("title"))
        return names