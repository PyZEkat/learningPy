from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

def screenshot():
    now = datetime.datetime.now()
    driver.save_screenshot('C:\work\screen_selen\screen_' + str(now.day) + '.' + str(now.hour) + '.' + str(
    now.minute) + '.' + str(now.second) + '.' + str(now.microsecond) + '.png')

#########################

EXE_PATH = 'C:\work\selenium\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
driver = webdriver.Chrome(executable_path=EXE_PATH)

driver.get('https://www.lambdatest.com/')
driver.maximize_window()

driver.implicitly_wait(10)

element = driver.find_element(By.XPATH, '//a[@href="https://accounts.lambdatest.com/login"]')
driver.implicitly_wait(10)
element.click()


element = driver.find_element(By.XPATH, '//input[@id="email"]')
element.send_keys("emailid@lambdatest.com")

element = driver.find_element(By.XPATH, '//input[@id="password"]')
element.send_keys("password")

screenshot()

element = driver.find_element(By.XPATH, '//button[@id="login-button"]')
element.click()

a = 0
while a < 5:
    element = driver.find_element(By.XPATH, '//button[@id="login-button"]')

    if element.get_attribute('willValidate') == 'true':
        time.sleep(1)
        a += 1
        print("Элемент не найден " + str(a) +" раз, ждем 1 секунду и пробуем еще раз")
    else:
        element2 = driver.find_element(By.XPATH, '//p[@data-testid="errors-email"]')
        if element2.get_attribute('textContent') == 'Please enter a correct username and password. Note that the password is case-sensitive':
            screenshot()
            a += 10
            print("Элемент найден делаю скриншет")
        else:
            time.sleep(1)
            a += 1
            print("Элементqq не найден " + str(a) + " раз, ждем 1 секунду и пробуем еще раз")

#driver.implicitly_wait(15)
#driver.set_page_load_timeout(5)
#time.sleep(5)






driver.quit()