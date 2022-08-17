from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

path = 'C:\work\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.google.ru/')
driver.maximize_window()

element = driver.find_element(By.XPATH, '//input[@title="Поиск"]')
element.send_keys('maps')
element.send_keys(Keys.ENTER)

driver.save_screenshot('C:\work\screen_selen\scr2.png')

driver.quit()