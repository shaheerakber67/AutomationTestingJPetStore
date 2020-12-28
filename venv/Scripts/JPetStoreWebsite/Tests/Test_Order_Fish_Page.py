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

    def test_case_BuyFishPage(self):
        driver = self.driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        signin = signinpage(driver)
        signin.click_signin()
        signin.enter_username("ssuetsoftwareengineers")
        signin.enter_pwd("12345678")
        signin.enter_btn()
        Buy_Fish = buyfishpage(driver)
        # Catalog
        Buy_Fish.click_fish()
        # Angelfish Portion
        # View Category
        Buy_Fish.click_Angelfish()
        # TigerShark Portion
        # View Category
        # Buy_Fish.click_TigerShark()
        # # Koi Portion
        # # View Category
        # Buy_Fish.click_Koi()
        # # Koi Portion
        # # View Category
        # Buy_Fish.click_Goldfish()
        #
        # view Product
        # Angelfish Portion
        # Buy_Fish.click_Angelfish_Large_Angelfish()
        Buy_Fish.click_Angelfish_Small_Angelfish()

        # # view Product
        # # TigerShark Portion

        # Buy_Fish.click_TigerShark_Toothless_TigerShark()

        # # view Product
        # # Koi Portion

        # Buy_Fish.click_Koi_Spotted_Koi()
        # Buy_Fish.click_Koi_Spotless_Koi()

        # # view Product
        # # Goldfish Portion

        # Buy_Fish.click_Goldfish_Adult_Male_Goldfish()
        # Buy_Fish.click_Goldfish_Adult_Female_Goldfish()

        # In view Item  click Add to cart
        # Angelfish Portion
        # Buy_Fish.click_add_to_cart_Angelfish_Large_Angelfish()
        Buy_Fish.click_add_to_cart_Angelfish_Small_Angelfish()
        # # TigerShark Portion
        # Buy_Fish.click_add_to_cart_TigerShark_Toothless_TigerShark()
        # # Koi Portion
        #
        # Buy_Fish.click_add_to_cart_Koi_Spotted_Koi()
        # Buy_Fish.click_add_to_cart_Koi_Spotless_Koi()
        # # Goldfish Portion
        # Buy_Fish.click_add_to_cart_Goldfish_Adult_Male_Goldfish()
        # Buy_Fish.click_add_to_cart_Goldfish_Adult_Female_Goldfish()
        #
        ## add Item To Cart
        ## Angelfish Portion
        # Buy_Fish.enter_quantity_Angelfish_Large_Angelfish("1")
        Buy_Fish.enter_quantity_Angelfish_Small_Angelfish("2")
        # # TigerShark Portion
        # Buy_Fish.enter_quantity_TigerShark_Toothless_TigerShark("3")
        # # Koi Portion
        # Buy_Fish.enter_quantity_Koi_Spotted_Koi("4")
        # Buy_Fish.enter_quantity_Koi_Spotless_Koi("5")
        # # Goldfish Portion
        # Buy_Fish.enter_quantity_Goldfish_Adult_Male_Goldfish("20")
        # Buy_Fish.enter_quantity_Goldfish_Adult_Female_Goldfish("21")
        #
        Buy_Fish.click_updatecart()
        Buy_Fish.click_proceedtocheckout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()
