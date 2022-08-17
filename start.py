from selenium import webdriver

path = 'C:\work\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.implicitly_wait(10)
