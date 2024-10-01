from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла


    browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']").send_keys("Владимир")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys("Иванов")
    browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("ivan@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()



finally:
    time.sleep(20)
    browser.quit()
