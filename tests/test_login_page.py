from fixtures.constants import LoginMessages


class TestLoginPage:

    def test_valid_login(self, app):
        """
        Valid logging.
        """
        app.login_page.open_login_page()
        username = LoginMessages.LOGIN
        password = LoginMessages.PASSWORD
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.dropdown_toggle_main_page() == LoginMessages.LOGIN

    def test_empty_username(self, app):
        """
        Empty username.
        """
        app.login_page.open_login_page()
        username = None
        password = "qwerqwerqwerqwer"
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.log_in() == LoginMessages.LOG_IN

    def test_empty_password(self, app):
        """
        Empty password.
        """
        app.login_page.open_login_page()
        username = "Aleppo"
        password = None
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.log_in() == LoginMessages.LOG_IN

    def test_invalid_password(self, app):
        """
        Invalid logging with invalid password.
        """
        app.login_page.open_login_page()
        username = LoginMessages.LOGIN
        password = "errrorpass123"
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.text_error_login_page() == LoginMessages.ERR_USERNAME_PASS

    def test_invalid_login(self, app):
        """
        Invalid logging with invalid login.
        """
        app.login_page.open_login_page()
        username = "errorlogin"
        password = LoginMessages.PASSWORD
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.text_error_login_page() == LoginMessages.ERR_USERNAME_PASS

    def test_invalid_login_and_password(self, app):
        """
        Invalid logging with invalid login and password.
        """
        app.login_page.open_login_page()
        username = "errorlogin"
        password = "errrorpass123"
        app.login_page.entry_data(username=username, password=password)
        assert app.login_page.text_error_login_page() == LoginMessages.ERR_USERNAME_PASS
