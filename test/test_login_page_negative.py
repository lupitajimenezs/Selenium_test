from selenium.webdriver.common.by import By
import pytest
from page_objects.login_page import LoginPage

class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "username",
        "password",
        "expected_error_message",
        [
            (
                "incorrectUser",
                "Password123",
                "Your user name is invalid!"
            ),
            (
                "student",
                "incorrectPassword",
                "your password is invalid!"
            )
        ]
    )#permite parametrizacion de argumentos para la prueba
    def test_negative_login(
        self,
        driver,
        username,
        password,
        expected_error_message
    ):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"