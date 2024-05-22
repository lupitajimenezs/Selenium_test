import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptios_page import ExceptionsPage

class TestExceptions:

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_no_such_element_exception(self, driver):
        exeptions_page = ExceptionsPage(driver)
        exeptions_page.open()
        exeptions_page.add_second_row()
        assert exeptions_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exeptions_page = ExceptionsPage(driver)
        exeptions_page.open()
        exeptions_page.add_second_row()
        exeptions_page.add_second_food("sushi")
        assert exeptions_page.get_confirmation_message() == "Row 2 was saved"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exeptions_page = ExceptionsPage(driver)
        exeptions_page.open()
        exeptions_page.modify_row_1_input("sushi")

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