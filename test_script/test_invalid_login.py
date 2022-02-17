import pytest

from generic.base_test import BaseTest
from generic.excel import Excel
from page.login_page import Login_Page
class Test_Invalid_Login(BaseTest):

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        #get data from excel
        un=Excel.get_data(self.xl_path,"InvalidLogin",2,1)
        pw = Excel.get_data(self.xl_path, "InvalidLogin", 2, 2)

        # 1.	Enter invalid username-abcd
        login_page=Login_Page(self.driver)
        login_page.set_username(un)

        # 2.	Enter invalid password -xyz
        login_page.set_password(pw)

        # 3.	Click login button
        login_page.click_login_button()

        # 4.	Verify that error message Is displayed
        result=login_page.verify_err_msg_is_displayed(self.wait)
        assert result