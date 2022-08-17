from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = 'C:\work\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://yandex.ru/')
driver.implicitly_wait(10)
driver.maximize_window()

element = driver.find_element(By.XPATH, '//input[@id="text"]')
element.send_keys("Python course")

element = driver.find_element(By.XPATH, '//button[@type="submit"]')
element.click()
driver.save_screenshot('C:\work\screen_selen\scr1.png')

driver.quit()