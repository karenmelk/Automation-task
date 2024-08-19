from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest
import time

@pytest.fixture(scope="class",autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.explicit_wait(3)
    driver.get("https://demowebshop.tricentis.com/")
    yield driver



class Testsuit_1:
    def test_TC01(self,driver):
        register = driver.find_element(By.CSS_SELECTOR,'.ico-register')
        register.click()
        time.sleep(10)

        
