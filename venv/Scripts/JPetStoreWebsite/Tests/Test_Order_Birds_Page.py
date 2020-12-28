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

    def test_case_BuyBirdsPage(self):
        driver = self.driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        signin = signinpage(driver)
        signin.click_signin()
        signin.enter_username("ssuetsoftwareengineers")
        signin.enter_pwd("12345678")
        signin.enter_btn()
        Buy_Birds = buybirdpage(driver)
        # Catalog
        Buy_Birds.click_birds()
        # View Category
        # Amazon Parrot  Portion
        Buy_Birds.click_AmazonParrot()
        # view Product
        # Amazon Parrot Portion
        Buy_Birds.click_AmazonParrot_AdultMaleAmazonParrot()
        # In view Item  click Add to cart
        # Amazon Parrot Portion
        Buy_Birds.click_add_to_cart()
        # add Item To Cart
        # Amazon Parrot Portion
        Buy_Birds.enter_quantity_AmazonParrot_AdultMaleAmazonParrot("5")
        # Update Cart
        Buy_Birds.click_updatecart()
        Buy_Birds.click_proceedtocheckout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()
