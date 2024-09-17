from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return str(int(x) + int(y))

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum = calc(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:
    time.sleep(20)
    browser.quit()
