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


    def test_case1_RegistrationPage(self):
        driver = self.driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        registration = registrationpage(driver)
        registration.click_signin()
        registration.click_registernow()
        registration.user_information("ssuetsoftwareengineers","12345678","12345678")
        registration.account_information("SSUET","Engineers", "ssuetengineers@gmail.com","1234567890","Lane 2"," Lane 1","Karachi","Sindh","75500","Pakistan")
        registration.profile_information()
        registration.enter_btn()

    def test_case2_RegistrationPage(self):
        main_url = "https://petstore.octoperf.com/actions/Catalog.action"
        chromedriver = 'C:/Users/shahe/Anaconda3/Scripts/chromedriver.exe'
        browser = webdriver.Chrome(chromedriver)
        browser.get(main_url)
        registration = registrationpage(browser)
        registration.click_signin()
        registration.click_registernow()
        registration.user_information("abcxyz", "12345678", "12345678")
        registration.account_information("ABC", "XYZ", "ssuetengineers1@gmail.com", "0987654321",
                                         " Lane 2", " Lane 1", "Karachi", "Sindh", "75500", "Pakistan")
        registration.profile_information()
        registration.enter_btn()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")



if __name__ == '__main__':
    unittest.main()
