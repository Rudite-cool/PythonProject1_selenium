import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def new_user():
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
    driver.find_element(By.ID, "Password").send_keys("bobiss12!")
    time.sleep(2)
    driver.find_element(By.ID, "Password2").send_keys("bobiss12!")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[value='Registruotis']").click()


# new_user()

def new_ad():
    pass

new_ad()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://elenta.lt/patalpinti/ivesti-informacija?categoryId=Kompiuterija_Kompiuteriai&actionId=Siulo&returnurl=%2Fpatalpinti%2Fpasirinkti-kategorija")
driver.find_element(By.CLASS_NAME, "fc-button-label").click()

driver.find_element(By.ID, "title").send_keys("Selling radio")
time.sleep(1)
driver.find_element(By.ID, "text").send_keys("Selling old radio, not working.")
time.sleep(1)
driver.find_element(By.ID, "price").send_keys("25")
time.sleep(1)
driver.find_element(By.ID, "location-search-box").send_keys("Vilnius")
time.sleep(1)
driver.find_element(By.ID, "phone").send_keys("+37061234567")
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("smulis404@emailas.lt")
time.sleep(1)
driver.find_element(By.ID, "submit-button").click()
time.sleep(1)
driver.find_element(By.ID, "inputfile").send_keys(r"C:\Users\rudul\Desktop\download.jpg")
driver.find_element(By.ID, "forward-button").click()
input()
