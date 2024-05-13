import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        #open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #click add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        # wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@id='row2']/input")))

        # #verify row 2 input field is displayed
        # row_2_input_element = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        #open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #click add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        #Type text into the second input field
        row_2_input_element.send_keys("Sushi")

        #Push save button using locator By.name("Save")
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        #Verify text saved
        confirmation_element = wait.until(ec.presence_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        #open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)

        #clear input field
        row_1_edit_button_locator = driver.find_element(By.ID, "edit_btn")
        row_1_edit_button_locator.click()

        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        # Type text into the input field
        row_1_input_element.send_keys("Sushi")

        row_1_save_button = driver.find_element(By.ID, "save_btn")
        row_1_save_button.click()

        #verify text changed
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_state_element_reference_exception(self, driver):
        #open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (
               By.ID,
                "instructions"
            )
        )), "Instruction text element should not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        #open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.visibility_of_element_located(
            (
                By.XPATH,
                "//div[@id='row2']/input"
            )
        ), "Failed waiting for row 2 input to be visible")

        # Verify second input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it's not"