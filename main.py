import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://elenta.lt")
driver.find_element(By.CLASS_NAME, "fc-button-label").click()

driver.find_element(By.XPATH, "//a[contains(@href, '/prisijungti')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[contains(@href, '/registracija')]").click()


driver.find_element(By.ID, "UserName").send_keys("bobis04")
time.sleep(2)
driver.find_element(By.ID, "Email").send_keys("smulis404@emailas.lt")
time.sleep(2)
driver.find_element(By.ID, "Password").send_keys("<bobiss12!>")
time.sleep(2)
driver.find_element(By.ID, "Password2").send_keys("<bobiss12!>")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value='Registruotis']").click()

input()
