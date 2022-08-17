from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime



def screenshot():
    now = datetime.datetime.now()
    driver.save_screenshot('C:\work\screen_selen\screen_' + str(now.day) + '.' + str(now.hour) + '.' + str(
    now.minute) + '.' + str(now.second) + '.' + str(now.microsecond) + '.png')

screenshot()



EXE_PATH = 'C:\work\selenium\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
driver = webdriver.Chrome(executable_path=EXE_PATH)

driver.get('https://www.bcgroup-online.com/')
driver.implicitly_wait(5)

element = driver.find_element(By.XPATH, '//input[@id="si"]')
element.send_keys('MOBILNI')
print(element.get_attribute('value'))

element = driver.find_element(By.XPATH, "//button[@type='submit']")    #//span[contains(text(),'Pronadji')]
element.click()



screenshot()
screenshot()
screenshot()


driver.quit()