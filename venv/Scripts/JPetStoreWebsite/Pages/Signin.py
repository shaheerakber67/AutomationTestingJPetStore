from selenium.webdriver.support.ui import Select

class signinpage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.signin_button_name = "signon"
        
    def click_signin(self):
        self.driver.find_element_by_link_text("Sign In").click()

    def enter_username(self,username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_pwd(self,pwd):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)

    def enter_btn(self):
        self.driver.find_element_by_name( self.signin_button_name).click()
        
    def click_signout(self):
        self.driver.find_element_by_link_text("Sign Out").click()
        