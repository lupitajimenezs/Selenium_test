from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage

class LoggedInSuccessfullyPage(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver) -> str:
        self._driver = driver

    def current_url(self) -> str:
        return self._driver.current_url
    
    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super().is_displayed(self.__log_out_button_locator)