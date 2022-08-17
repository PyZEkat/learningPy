from start import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


def checkElement(link):
    try:
        WebDriverWait(driver, 10).until(es.presence_of_element_located((By.XPATH, link)))
        print("Найден " + link)
    except Exception as e:
        print(e)
        print("Не найден элемент " + link)


