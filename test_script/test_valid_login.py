from generic.base_test import BaseTest
from page.enter_time_track_page import Enter_Time_Track_Page
from page.login_page import Login_Page


class Test_Valid_Login(BaseTest):

    def test_valid_login(self):
# 1.	Enter valid username- admin
        login_page=Login_Page(self.driver)
        login_page.set_username("admin")

# 2.	Enter valid password-manager
        login_page.set_password("manager")

# 3.	Click login button
        login_page.click_login_button()

# 4.	Verify that home page is displayed
        ett_page=Enter_Time_Track_Page(self.driver)
        result=ett_page.verify_ett_page_is_displayed(self.wait)
        assert result
