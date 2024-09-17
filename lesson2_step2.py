from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_chest = browser.find_element(By.ID, "treasure")
    find_attribute = find_chest.get_attribute("valuex")
    y = calc(find_attribute)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()



finally:
    time.sleep(20)
    browser.quit()
