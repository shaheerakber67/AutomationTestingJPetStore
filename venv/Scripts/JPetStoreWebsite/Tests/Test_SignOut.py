from Scripts.JPetStoreWebsite.Pages.RegistrationPage import registrationpage
from Scripts.JPetStoreWebsite.Pages.Signin import signinpage
from Scripts.JPetStoreWebsite.Pages.Buy_Fish import buyfishpage
from Scripts.JPetStoreWebsite.Pages.newOrderForm import neworderform
from Scripts.JPetStoreWebsite.Pages.Buy_Dog import buydogpage
from Scripts.JPetStoreWebsite.Pages.Buy_Reptiles import buyreptilespage
from Scripts.JPetStoreWebsite.Pages.Buy_Cat import buycatpage
from Scripts.JPetStoreWebsite.Pages.Buy_Birds import buybirdpage
from Scripts.JPetStoreWebsite.Pages.SearchBar import SearchBar
from Scripts.JPetStoreWebsite.Pages.MyAccountPage import myaccountpage
from Scripts.JPetStoreWebsite.Pages.ViewCartPage import viewcartpage

from selenium import webdriver
from selenium.webdriver.support.ui import Select


import time
import unittest


class JPetStoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/shahe/Anaconda3/Scripts/chromedriver.exe")
        cls.driver.implicitly_wait(2000)

    def test_case_SignInPage(self):
        driver = self.driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        signin = signinpage(driver)
        signin.click_signin()
        signin.enter_username("ssuetsoftwareengineers")
        signin.enter_pwd("12345678")
        signin.enter_btn()
        signin.click_signout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()
