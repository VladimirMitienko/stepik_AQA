from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest

login = "login"
password = "password"
answer = math.log(int(time.time()))

link = "https://stepik.org/lesson/236895/step/1?auth=login"
@pytest.parametrize()
def test_login(browser):
    browser.get("https://stepik.org/lesson/236895/step/1?auth=login")
    time.sleep(5)
    browser.find_element(By.ID, "id_login_email").send_keys(login)
    browser.find_element(By.ID, "id_login_password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
    time.sleep(5)