from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()


finally:
    time.sleep(20)
    browser.quit()