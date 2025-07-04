from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def extract_price(price_str):
    price_str = price_str.replace("€", "").replace(" ", "").replace(",", ".").strip()
    try:
        return float(price_str)
    except:
        return None

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://skelbiu.lt")

driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

driver.find_element(By.ID, "searchKeyword").send_keys("karpis")
driver.find_element(By.ID, "searchButton").click()

skelbimai = driver.find_elements(By.CLASS_NAME, "ads__item")
print("Rasta skelbimų:", len(skelbimai))

prices = []

for ad in skelbimai:
    try:
        img_tag = ad.find_element(By.TAG_NAME, "img")
        img_url = img_tag.get_attribute("src")

        if img_url and img_url.startswith("https://skelbiu-img.dgn.lt"):
            price_tag = ad.find_element(By.CLASS_NAME, "price")
            price_text = price_tag.text.strip()
            price_num = extract_price(price_text)
            if price_num is not None:
                prices.append(price_num)
                print(f"Kaina: {price_num:.2f} €")
    except Exception as e:
        print(f"Error processing ad: {e}")
        continue

if prices:
    average = sum(prices) / len(prices)
    print(f"\nVidutinė kaina: {average:.2f} €")
else:
    print("\nNerasta kainų su paveikslėliais iš skelbiu domeno.")

driver.quit()

input()