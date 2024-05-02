from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestNegativeScenarios:
    driver = webdriver.Firefox()
    time.sleep(3)
    #Indicamos la pagina que vamos a visitar.
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    #Buscando los elementos de la pagina.
    username_locator = driver.find_element(By.NAME, "username")
    username_locator.send_keys("incorrectUser")

    password_locator = driver.find_element(By.NAME, "password")
    password_locator.send_keys("Password123")

    submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    submit_button_locator.click()
    time.sleep(2)

    #verify error message is displayed
    error_message_locator = driver.find_element(By.Id, "Error")
    assert error_message_locator.is_displayed(), "Error message is not dispayed, but it should be"

    #verify error message text is your username is invalid!
    error_messge = error_message_locator.text
    assert error_messge == "Your username is invalid!", "Error message is not expected"