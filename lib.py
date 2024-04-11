from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import time

link1 = "https://sbis.ru/"
link2 = 'https://tensor.ru/'
link3 = 'https://tensor.ru/about'
link4 = "https://sbis.ru/contacts"

def click(selector,driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        element.click()
        print(f"Succes click {selector}")
    except TimeoutError:
        pytest.fail('time is out, try again')
    except Exception as a:
        pytest.fail(a)

def clickscrol(selector,driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        print(f"Succes click {selector}")
    except TimeoutError:
        pytest.fail('time is out, try again')
    except Exception as a:
        pytest.fail(a)

def WidhtHeight (selector, driver, width, height):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, selector))
        )
        status = 1
        for i, element in enumerate(element):
            driver.execute_script("arguments[0].scrollIntoView();", element)
            size = element.size
            w = size['width']
            h = size['height']
            if w == width and h == height:
                status = 1
            else:
                status = 0
        if status == 1:
            print (f"Succes all img have size w= {width}, h= {height}")
        else:
            pytest.fail(f"error width size img {w}, {h}")
    except TimeoutError:
        pytest.fail('time is out, try again')
    except Exception as a:
        pytest.fail(a)

def text(selector,driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        word = element.text
        return word
    except TimeoutError:
          pytest.fail('time is out, try again')
    except Exception as a:
            pytest.fail(a)

def link (driver,link):
    window_handles = driver.window_handles
    if len(window_handles) > 1: 
        driver.switch_to.window(window_handles[1])
        if driver.current_url == link:
            print(f"Succes open {driver.current_url}")
        else:
            pytest.fail(f"Error open {link}")


def istext(text, case):
    if text == case:
        print(f"Succes test {text}")
    else:
        pytest.fail(f"Error test {case}")