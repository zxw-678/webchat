from seleniumpo.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        username = "王爽"
        account = "006"
        phonenumber = "15075649058"
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenumber)
        names = page.get_member()
        print(names)
        assert username in names

