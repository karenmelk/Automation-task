from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest
import time



@pytest.fixture(scope="class",autouse=True)
def driver():
    url = 'https://demowebshop.tricentis.com/'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
@pytest.fixture(autouse=True)
def navigate_homepage(driver):
    driver.get(url='https://demowebshop.tricentis.com/')


class Testsuit_1:
    def test_TC01(self,driver):
        register = driver.find_element(By.CSS_SELECTOR,'.ico-register')
        register.click()
        gender = driver.find_element(By.CSS_SELECTOR,'#gender-male')
        gender.click()
        first_name = driver.find_element(By.CSS_SELECTOR,'#FirstName')
        first_name.send_keys('Karen')
        last_name = driver.find_element(By.CSS_SELECTOR,'#LastName')
        last_name.send_keys('Melkonyan')
        
        email = driver.find_element(By.CSS_SELECTOR,'#Email')
        email.send_keys('provideemail@mail.ru')
        
        passwd = driver.find_element(By.CSS_SELECTOR,'#Password')
        passwd.send_keys('Qwerty1234')
        
        confrm_passwd = driver.find_element(By.CSS_SELECTOR,'#ConfirmPassword')
        confrm_passwd.send_keys('Qwerty1234')

        reg = driver.find_element(By.CSS_SELECTOR,'#register-button')
        reg.click()

        assert driver.find_element(By.CSS_SELECTOR,'.result').text == 'Your registration completed' ,'User is not registered and logged in successfully'
    def test_TC02(self,driver):
        product = driver.find_element(By.CSS_SELECTOR,'#small-searchterms')
        product.send_keys('Laptop')

        search = driver.find_element(By.CSS_SELECTOR,"input[value='Search']")
        search.click()

        assert  'Laptop' in driver.find_element(By.CSS_SELECTOR,'.product-title > a').text , 'Related not displays'
    def test_TC03(self,driver):
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)
        product = driver.find_element(By.CSS_SELECTOR,'#small-searchterms')
        product.send_keys('Laptop')

        search = driver.find_element(By.CSS_SELECTOR,"input[value='Search']")
        search.click()

        laptop = driver.find_element(By.CSS_SELECTOR,'.product-title')
        laptop.click()
        time.sleep(3)
        product_name = driver.find_element(By.CSS_SELECTOR,"h1[itemprop='name']").text

        add_card = driver.find_element(By.CSS_SELECTOR,'#add-to-cart-button-31')
        add_card.click()
        time.sleep(3)
        shopping_card = driver.find_element(By.CSS_SELECTOR,'#topcartlink')
        shopping_card.click()

        assert driver.find_element(By.CSS_SELECTOR,'.product-name').text == product_name , 'Product is not added to the shopping cart.'
    def test_TC04(self,driver):
        # Testsuit_1.test_TC03()
        add_card = driver.find_element(By.CSS_SELECTOR,'#topcartlink')
        add_card.click()

        terms = driver.find_element(By.CSS_SELECTOR,"#termsofservice")
        terms.click()

        checkout = driver.find_element(By.CSS_SELECTOR,"#checkout")
        checkout.click()

        # company = driver.find_element(By.CSS_SELECTOR,'#BillingNewAddress_Company')
        # company.send_keys('Apple')

        country = driver.find_element(By.CSS_SELECTOR,"#BillingNewAddress_CountryId")
        country.click()

        Armenia = driver.find_element(By.CSS_SELECTOR,"option[value='4']")
        Armenia.click()

        state = driver.find_element(By.CSS_SELECTOR,"#BillingNewAddress_StateProvinceId")
        state.click()

        city = driver.find_element(By.CSS_SELECTOR,'#BillingNewAddress_City')
        city.send_keys('Yerevan')

        address = driver.find_element(By.CSS_SELECTOR,'#BillingNewAddress_Address1')
        address.send_keys('Manadyan 22')

        zipcode = driver.find_element(By.CSS_SELECTOR,'#BillingNewAddress_ZipPostalCode')
        zipcode.send_keys('0006')

        phone = driver.find_element(By.CSS_SELECTOR,'#BillingNewAddress_PhoneNumber')
        phone.send_keys('+37491424014')
        cnt = driver.find_element(By.CSS_SELECTOR,'.new-address-next-step-button')
        cnt.click()

        cnt = driver.find_element(By.CSS_SELECTOR,"input[onclick='Shipping.save()']")
        cnt.click()

        cnt = driver.find_element(By.CSS_SELECTOR,".shipping-method-next-step-button")
        cnt.click()     

        cnt = driver.find_element(By.CSS_SELECTOR,".payment-method-next-step-button")
        cnt.click()     

        cnt = driver.find_element(By.CSS_SELECTOR,".payment-info-next-step-button")
        cnt.click()   

        confirm = driver.find_element(By.CSS_SELECTOR,"input[value='Confirm']")
        confirm.click() 

        assert driver.find_element(By.CSS_SELECTOR,"div[class='title'] strong").text == "Your order has been successfully processed!" , 'Your order has not been successfully processed!'




        


