from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://elenta.lt")
driver.find_element(By.XPATH, "//p[contains(@class, 'fc-button-label') and contains(text(), 'Sutik')]").click()

login_button = driver.find_element(By.XPATH, "//a[contains(@href, '/prisijungti')]")
login_button.click()
register_link = driver.find_element(By.XPATH, "//a[contains(@href, '/registracija')]")
register_link.click()
input()
