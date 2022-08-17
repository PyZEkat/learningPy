from start import driver
from selenium.webdriver.common.by import By


def searchNclick(link):
    driver.find_element(By.XPATH, link).click()


def writeText(link, text):
    driver.find_element(By.XPATH, link).send_keys(text)



def search(link):
    driver.find_element(By.XPATH, link)


def cleartext(link):
    driver.find_element(By.XPATH, link).clear()
