from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage():
    __username_field = (By.ID, "username")
    __pasword_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self.__url)

    def execute_login(
        self,
        username: str,
        password: str
    ):
        wait = WebDriverWait(self._driver, 10)
        

        #Type user name student into Username field
        username_locator = self._driver.find_element(By.ID, self.__username_field)
        username_locator.send_keys(username)

        #Type password Password123 into password field
        password_locator = self._driver.find_element(By.NAME, self.__pasword_field)
        password_locator.send_keys(password)

        #push Submit button
        submit_button_locator = self._driver.find_element(By.XPATH, self.__submit_button)
        submit_button_locator.click()
        time.sleep(2)