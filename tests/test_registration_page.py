import random
import pytest

from fixtures.constants import RegisterMessages
from models.registration import RegisterUserModel
from tests.parametrize_data import Data


class TestRegistrationPage:
    def test_valid_registration_all_fields(self, app):
        """
        Valid registration with all possible fields.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_log_in() == RegisterMessages.LOG_IN

    def test_valid_registration_without_fields(self, app):
        """
        Registration without fields "firstname" and "email".
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.firstname = ""
        data.email = ""
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_log_in() == RegisterMessages.LOG_IN

    def test_registration_already_exists_username(self, app):
        """
        Registering an existing username.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = "Aleppo"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ALREADY_EXISTS

    def test_registration_pass_similar_username(self, app):
        """
        Registration password is similar to username.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = "testtesttest11"
        data.password_1 = "testtesttest"
        data.password_2 = "testtesttest"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.SIMILAR_PASS

    def test_two_password_fields_did_not_match(self, app):
        """
        Registration with different passwords.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_2 = "different"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.PASS_DIDNT_MATCH

    @pytest.mark.parametrize("valid", Data.VALID_SPECIAL_CHARACTERS)
    def test_valid_username_special_character(self, app, valid):
        """
        Registration with valid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + valid
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_log_in() == RegisterMessages.LOG_IN

    @pytest.mark.parametrize("invalid", Data.INVALID_SPECIAL_CHARACTERS)
    def test_invalid_username_special_character(self, app, invalid):
        """
        Registration with invalid special characters.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.username = data.username + invalid
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ERROR_USERNAME

    def test_short_password(self, app):
        """
        Registration with a short password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "HbnkIla"
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ERROR_SHORT_PASS

    def test_numeric_password(self, app):
        """
        Registration with a numeric password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "23416435674"
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ERROR_NUMERIC_PASS

    def test_easy_password(self, app):
        """
        Registration with easy password.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.password_1 = "qwerty123"
        data.password_2 = data.password_1
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ERROR_COMMON_PASS

    def test_invalid_email(self, app):
        """
        Registration with invalid email.
        """
        app.registration_page.open_registration_page()
        data = RegisterUserModel.random()
        data.email = "invalid"
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_log_in() != RegisterMessages.LOG_IN

    def test_invalid_age(self, app):
        """
        Registration with invalid age.
        """
        app.registration_page.open_registration_page()
        app.registration_page.clear_and_fill(random.randint(0, 17))
        data = RegisterUserModel.random()
        app.registration_page.entry_data_registration(data=data)
        assert app.registration_page.text_error() == RegisterMessages.ERROR_AGE
