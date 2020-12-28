from selenium.webdriver.support.ui import Select

class registrationpage():
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_name = "username"
        self.password_textbox_name="password"
        self.repeatpassword_textbox_name="repeatedPassword"
        
        self.firstname_textbox_name="account.firstName"
        self.lastname_textbox_name = "account.lastName"
        self.email_textbox_name = "account.email"
        self.phone_textbox_name = "account.phone"
        self.address1_textbox_name = "account.address1"
        self.address2_textbox_name = "account.address2"
        self.city_textbox_name = "account.city"
        self.state_textbox_name = "account.state"
        self.zip_textbox_name = "account.zip"
        self.country_textbox_name = "account.country"
        self.saveaccinfo_button_name = "newAccount"


    def click_signin(self):
        self.driver.find_element_by_link_text("Sign In").click()

    def click_registernow(self):
        self.driver.find_element_by_link_text("Register Now!").click()

    def user_information(self,uname,pwd,rpwd):
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(uname)
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)
        self.driver.find_element_by_name(self.repeatpassword_textbox_name).send_keys(rpwd)

    def account_information(self, fname,lname,email,phone,address1,address2,city,state,zip,country):
        self.driver.find_element_by_name(self.firstname_textbox_name).send_keys(fname)
        self.driver.find_element_by_name(self.lastname_textbox_name).send_keys(lname)
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)
        self.driver.find_element_by_name(self.phone_textbox_name).send_keys(phone)
        self.driver.find_element_by_name(self.address1_textbox_name).send_keys(address1)
        self.driver.find_element_by_name(self.address2_textbox_name).send_keys(address2)
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(city)
        self.driver.find_element_by_name(self.state_textbox_name).send_keys(state)
        self.driver.find_element_by_name(self.zip_textbox_name).send_keys(zip)
        self.driver.find_element_by_name(self.country_textbox_name).send_keys(country)
                    
    def profile_information(self):
        select1 = Select(self.driver.find_element_by_name('account.languagePreference'))
        select1.select_by_value('english')
        select2 = Select(self.driver.find_element_by_name('account.favouriteCategoryId'))
        select2.select_by_value('FISH')
        self.driver.find_element_by_name("account.listOption").click()
        self.driver.find_element_by_name("account.bannerOption").click()
       
            
            
    def enter_btn(self):
        self.driver.find_element_by_name(self.saveaccinfo_button_name).click()


       
