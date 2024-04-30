from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Iniciamos la confi del navegador.
driver = webdriver.Firefox()
time.sleep(3)
#Indicamos la pagina que vamos a visitar.
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#Buscando los elementos de la pagina.
username_locator = driver.find_element(By.NAME, "username")
username_locator.send_keys("student")

password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

actual_url = driver.current_url
#assert verifica que la condicion sea verdadera
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

#Verificando si la nueva pagina contiene el texto "Logged In Successfully"
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

log_out__button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out__button_locator.is_displayed()