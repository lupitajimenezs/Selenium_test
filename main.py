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
password_locator = driver.find_element(By.NAME, "password")
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")