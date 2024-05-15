from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage(BasePage):
    __username_field = (By.ID, "username")
    __pasword_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(
        self,
        username: str,
        password: str
    ):
        super()._type(
            self.__username_field,
            username
        )
        super()._type(
            self.__pasword_field,
            password
        )
        super()._click(
            self.__submit_button
        )