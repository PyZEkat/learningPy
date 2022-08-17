from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'C:\work\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://duckduckgo.com/')
driver.maximize_window()

element = driver.find_element(By.XPATH, '//input[@id="search_form_input_homepage"]')
element.send_keys('youtube')

element = driver.find_element(By.XPATH, '//input[@id="search_button_homepage"]')
element.click()

driver.save_screenshot('C:\work\screen_selen\scr1.png')

driver.quit()