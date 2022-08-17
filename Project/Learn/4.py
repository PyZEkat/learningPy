from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path = 'C:\work\selenium\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://duckduckgo.com/')
driver.maximize_window()

element = driver.find_element(By.XPATH, '//a[starts-with(@href, "#")]')
element.click()

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li/span[contains(text(), "Настройки")]')))

#wait.until(ExpectedConditions.invisibilityOfElementLocated('//li/span[contains(text(), "Настройки")]')
    #driver.find_element(By.XPATH, '//li/span[contains(text(), "Настройки")]').visibilityOfElementLocated







#//a[starts-with(@href, "#")]