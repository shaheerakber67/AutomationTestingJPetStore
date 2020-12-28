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
        cls.driver= webdriver.Chrome(executable_path="C:/Users/shahe/Anaconda3/Scripts/chromedriver.exe")
        cls.driver.implicitly_wait(2000)


    # def test_case1_RegistrationPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     registration = registrationpage(driver)
    #     registration.click_signin()
    #     registration.click_registernow()
    #     registration.user_information("g2","123456789","123456789")
    #     registration.account_information("Shaheer","Akber", "shaheerakber67@gmail.com","03242744870","7-C Lane 2","217-C Lane 1","Karachi","Sindh","75500","Pakistan")
    #     registration.profile_information()
    #     registration.enter_btn()



    # def test_case2_RegistrationPage(self):
    #     main_url = "https://petstore.octoperf.com/actions/Catalog.action"
    #     chromedriver = 'C:/Users/shahe/Anaconda3/Scripts/chromedriver.exe'
    #
    #     browser = webdriver.Chrome(chromedriver)
    #     browser.get(main_url)
    #     registration = registrationpage(browser)
    #     registration.click_signin()
    #     registration.click_registernow()
    #     registration.user_information("gss", "123456789", "123456789")
    #     registration.account_information("Shaheer", "Akber", "shaheerakber67@gmail.com", "03242744870",
    #                                      "7-C Lane 2", "217-C Lane 1", "Karachi", "Sindh", "75500", "Pakistan")
    #     registration.profile_information()
    #
    #     registration.enter_btn()
    #     time.sleep(5)


    #
    # def test_case3_RegistrationPage(self):
    #     main_url = "https://petstore.octoperf.com/actions/Catalog.action"
    #     chromedriver = 'C:/Users/shahe/Anaconda3/Scripts/chromedriver.exe'
    #
    #     browser = webdriver.Chrome(chromedriver)
    #     browser.get(main_url)
    #     registration = registrationpage(browser)
    #     registration.click_signin()
    #     registration.click_registernow()
    #     registration.user_information("abcd", "123456789", "123456789")
    #     registration.account_information("Shaheer", "Akber", "shaheerakber@gmail.com", "03242744870",
    #                                          "7-C Lane 2", "217-C Lane 1", "Karachi", "Sindh", "75500", "Pakistan")
    #     registration.profile_information()
    #     registration.enter_btn()
    #     time.sleep(5)


    # def test_case4_SignInPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     signin.click_signout()

    # def test_case5_BuyFishPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Buy_Fish = buyfishpage(driver)
    #     # Catalog
    #     Buy_Fish.click_fish()
    #     # Angelfish Portion
    #     # View Category
    #     Buy_Fish.click_Angelfish()
    #     # TigerShark Portion
    #     # View Category
    #     # Buy_Fish.click_TigerShark()
    #     # # Koi Portion
    #     # # View Category
    #     # Buy_Fish.click_Koi()
    #     # # Koi Portion
    #     # # View Category
    #     # Buy_Fish.click_Goldfish()
    #     #
    #     # view Product
    #     # Angelfish Portion
    #     # Buy_Fish.click_Angelfish_Large_Angelfish()
    #     Buy_Fish.click_Angelfish_Small_Angelfish()
    #
    #     # # view Product
    #     # # TigerShark Portion
    #
    #     # Buy_Fish.click_TigerShark_Toothless_TigerShark()
    #
    #     # # view Product
    #     # # Koi Portion
    #
    #     # Buy_Fish.click_Koi_Spotted_Koi()
    #     # Buy_Fish.click_Koi_Spotless_Koi()
    #
    #     # # view Product
    #     # # Goldfish Portion
    #
    #     # Buy_Fish.click_Goldfish_Adult_Male_Goldfish()
    #     # Buy_Fish.click_Goldfish_Adult_Female_Goldfish()
    #
    #     # In view Item  click Add to cart
    #     # Angelfish Portion
    #     # Buy_Fish.click_add_to_cart_Angelfish_Large_Angelfish()
    #     Buy_Fish.click_add_to_cart_Angelfish_Small_Angelfish()
    #     # # TigerShark Portion
    #     # Buy_Fish.click_add_to_cart_TigerShark_Toothless_TigerShark()
    #     # # Koi Portion
    #     #
    #     # Buy_Fish.click_add_to_cart_Koi_Spotted_Koi()
    #     # Buy_Fish.click_add_to_cart_Koi_Spotless_Koi()
    #     # # Goldfish Portion
    #     # Buy_Fish.click_add_to_cart_Goldfish_Adult_Male_Goldfish()
    #     # Buy_Fish.click_add_to_cart_Goldfish_Adult_Female_Goldfish()
    #     #
    #     ## add Item To Cart
    #     ## Angelfish Portion
    #     # Buy_Fish.enter_quantity_Angelfish_Large_Angelfish("1")
    #     Buy_Fish.enter_quantity_Angelfish_Small_Angelfish("2")
    #     # # TigerShark Portion
    #     # Buy_Fish.enter_quantity_TigerShark_Toothless_TigerShark("3")
    #     # # Koi Portion
    #     # Buy_Fish.enter_quantity_Koi_Spotted_Koi("4")
    #     # Buy_Fish.enter_quantity_Koi_Spotless_Koi("5")
    #     # # Goldfish Portion
    #     # Buy_Fish.enter_quantity_Goldfish_Adult_Male_Goldfish("20")
    #     # Buy_Fish.enter_quantity_Goldfish_Adult_Female_Goldfish("21")
    #     #
    #     Buy_Fish.click_updatecart()
    #     Buy_Fish.click_proceedtocheckout()
    #
    # def test_case6_NewOrderFormPage_For_BuyFish(self):
    #     driver = self.driver
    #     neworder = neworderform(driver)
    #     neworder.PaymentDetails("11121212121211", "12/21")
    #     neworder.BillingAddress("Shaheer", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     #neworder.tick_DifferentShippingAddress()
    #     # neworder.click_continue()
    #     # neworder.DifferentShippingAddress("ABC", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     neworder.click_continue()
    #     neworder.click_confirm()

    # def test_case7_BuyDogPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Buy_Dog = buydogpage(driver)
    #     # Catalog
    #     Buy_Dog.click_dog()
    #     # View Category
    #     # Bulldog Portion
    #     Buy_Dog.click_Bulldog()
    #     # view Product
    #     # Bulldog Portion
    #     Buy_Dog.click_Bulldog_FemalePuppyBulldog()
    #     # In view Item  click Add to cart
    #     # Bulldog Portion
    #     Buy_Dog.click_add_to_cart_Bulldog_FemalePuppyBulldog()
    #     # add Item To Cart
    #     # Bulldog Portion
    #     Buy_Dog.enter_quantity_Bulldog_FemalePuppyBulldog("4")
    #     # Update Cart
    #     Buy_Dog.click_updatecart()
    #     Buy_Dog.click_proceedtocheckout()
    #
    # def test_case8_NewOrderFormPage_For_BuyDog(self):
    #     driver = self.driver
    #     neworder = neworderform(driver)
    #     neworder.PaymentDetails("11121212121211", "12/21")
    #     neworder.BillingAddress("Shaheer", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     #neworder.tick_DifferentShippingAddress()
    #     # neworder.click_continue()
    #     # neworder.DifferentShippingAddress("ABC", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     neworder.click_continue()
    #     neworder.click_confirm()


    # def test_case9_BuyReptilesPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Buy_Reptiles = buyreptilespage(driver)
    #     # Catalog
    #     Buy_Reptiles.click_reptiles()
    #     # View Category
    #     # Iguana Portion
    #     Buy_Reptiles.click_Iguana()
    #     # view Product
    #     # Iguana Portion
    #     Buy_Reptiles.click_Iguana_GreenAdultIguana()
    #     # In view Item  click Add to cart
    #     # Iguana Portion
    #     Buy_Reptiles.click_add_to_cart()
    #     # add Item To Cart
    #     # Iguana Portion
    #     Buy_Reptiles.enter_quantity_Iguana_GreenAdultIguana("4")
    #     # Update Cart
    #     Buy_Reptiles.click_updatecart()
    #     Buy_Reptiles.click_proceedtocheckout()
    #
    # def test_case_NewOrderFormPage_For_BuyReptiles(self):
    #     driver = self.driver
    #     neworder = neworderform(driver)
    #     neworder.PaymentDetails("11121212121211", "12/21")
    #     neworder.BillingAddress("Shaheer", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     #neworder.tick_DifferentShippingAddress()
    #     # neworder.click_continue()
    #     # neworder.DifferentShippingAddress("ABC", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     neworder.click_continue()
    #     neworder.click_confirm()

    # def test_case11_BuyCatPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Buy_Cats = buycatpage(driver)
    #     # Catalog
    #     Buy_Cats.click_cat()
    #     # View Category
    #     # Manx Portion
    #     Buy_Cats.click_Manx()
    #     # view Product
    #     # Manx Portion
    #     Buy_Cats.click_Manx_WithtailManx()
    #     # In view Item  click Add to cart
    #     # Manx Portion
    #     Buy_Cats.click_add_to_cart()
    #     # add Item To Cart
    #     # Manx Portion
    #     Buy_Cats.enter_quantity_Manx_WithtailManx("4")
    #     # Update Cart
    #     Buy_Cats.click_updatecart()
    #     Buy_Cats.click_proceedtocheckout()
    #
    # def test_case_NewOrderFormPage_For_BuyCat(self):
    #     driver = self.driver
    #     neworder = neworderform(driver)
    #     neworder.PaymentDetails("11121212121211", "12/21")
    #     neworder.BillingAddress("Shaheer", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     #neworder.tick_DifferentShippingAddress()
    #     # neworder.click_continue()
    #     # neworder.DifferentShippingAddress("ABC", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     neworder.click_continue()
    #     neworder.click_confirm()

    # def test_case13_BuyBirdsPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Buy_Birds = buybirdpage(driver)
    #     # Catalog
    #     Buy_Birds.click_birds()
    #     # View Category
    #     # Amazon Parrot  Portion
    #     Buy_Birds.click_AmazonParrot()
    #     # view Product
    #     # Amazon Parrot Portion
    #     Buy_Birds.click_AmazonParrot_AdultMaleAmazonParrot()
    #     # In view Item  click Add to cart
    #     # Amazon Parrot Portion
    #     Buy_Birds.click_add_to_cart()
    #     # add Item To Cart
    #     # Amazon Parrot Portion
    #     Buy_Birds.enter_quantity_AmazonParrot_AdultMaleAmazonParrot("5")
    #     # Update Cart
    #     Buy_Birds.click_updatecart()
    #     Buy_Birds.click_proceedtocheckout()
    #
    # def test_case_NewOrderFormPage_For_BuyBirds(self):
    #     driver = self.driver
    #     neworder = neworderform(driver)
    #     neworder.PaymentDetails("11121212121211", "12/21")
    #     neworder.BillingAddress("Shaheer", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     #neworder.tick_DifferentShippingAddress()
    #     # neworder.click_continue()
    #     # neworder.DifferentShippingAddress("ABC", "Akber","7-C Lane 2", "Karachi", "Sindh", "75500", "Pakistan")
    #     neworder.click_continue()
    #     neworder.click_confirm()

    # def test_case15_SearchBar(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     Search_bar = SearchBar(driver)
    #     Search_bar.enter_search("Angelfish")
    #     Search_bar.click_searchbutton()

    # def test_case16_MyAccountPage(self):
    #     driver = self.driver
    #     driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    #     signin = signinpage(driver)
    #     signin.click_signin()
    #     signin.enter_username("shaheerakber67")
    #     signin.enter_pwd("123456789")
    #     signin.enter_btn()
    #     My_Acc = myaccountpage(driver)
    #     My_Acc.click_myaccount()
    #     My_Acc.user_information("123456789","123456789")
    #     My_Acc.account_information("Shaheer","Akber", "shaheerakber67@gmail.com","03242744870","7-C Lane 2","217-C Lane 1","Karachi","Sindh","75500","Pakistan")
    #     My_Acc.profile_information()
    #     My_Acc.btn_saveaccinfo()

    def test_case17_ViewCartPage(self):
        driver = self.driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        signin = signinpage(driver)
        signin.click_signin()
        signin.enter_username("shaheerakber67")
        signin.enter_pwd("12345678")
        signin.enter_btn()
        view_cart = viewcartpage(driver)
        view_cart.click_viewcart()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
        
if __name__ == '__main__':
    unittest.main()
