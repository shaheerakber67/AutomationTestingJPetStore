from selenium.webdriver.support.ui import Select

class neworderform():
    def __init__(self, driver):
        self.driver = driver
        self.creditCard_textbox_name = "order.creditCard"
        self.expiryDate_textbox_name = "order.expiryDate"
        self.billToFirstName_textbox_name = "order.billToFirstName"
        self.billToLastName_textbox_name = "order.billToLastName"
        self.billAddress1_textbox_name = "order.billAddress1"
        # self.billAddress2_textbox_name = "order.billAddress2"
        self.billCity_textbox_name = "order.billCity"
        self.billState_textbox_name = "order.billState"
        self.billZip_textbox_name = "order.billZip"
        self.billCountry_textbox_name = "order.billCountry"

        #Ship to Different Address
        self.shipToFirstName_textbox_name = "order.shipToFirstName"
        self.shipToLastName_textbox_name = "order.shipToLastName"
        self.shipAddress1_textbox_name = "order.shipAddress1"
        # self.shipAddress2_textbox_name = "order.shipAddress2"
        self.shipCity_textbox_name = "order.shipCity"
        self.shipState_textbox_name = "order.shipState"
        self.shipZip_textbox_name = "order.shipZip"
        self.shipCountry_textbox_name = "order.shipCountry"

    def PaymentDetails(self,cnum,expdate):
        select1 = Select(self.driver.find_element_by_name('order.cardType'))
        # select1.select_by_value('Visa')
        select1.select_by_value('MasterCard')
        # select1.select_by_value('American Express')
        
        self.driver.find_element_by_name(self.creditCard_textbox_name).clear()
        self.driver.find_element_by_name(self.creditCard_textbox_name).send_keys(cnum)
       
        self.driver.find_element_by_name(self.expiryDate_textbox_name).clear()
        self.driver.find_element_by_name(self.expiryDate_textbox_name).send_keys(expdate)


    def BillingAddress(self,fname,lname,address1,city,state,zip,country):
        self.driver.find_element_by_name(self.billToFirstName_textbox_name).clear()
        self.driver.find_element_by_name(self.billToFirstName_textbox_name).send_keys(fname)
        
        self.driver.find_element_by_name(self.billToLastName_textbox_name).clear()
        self.driver.find_element_by_name(self.billToLastName_textbox_name).send_keys(lname)

        self.driver.find_element_by_name(self.billAddress1_textbox_name).clear()
        self.driver.find_element_by_name(self.billAddress1_textbox_name).send_keys(address1)

        self.driver.find_element_by_name(self.billCity_textbox_name).clear()
        self.driver.find_element_by_name(self.billCity_textbox_name).send_keys(city)

        self.driver.find_element_by_name(self.billState_textbox_name).clear()
        self.driver.find_element_by_name(self.billState_textbox_name).send_keys(state)

        self.driver.find_element_by_name(self.billZip_textbox_name).clear()
        self.driver.find_element_by_name(self.billZip_textbox_name).send_keys(zip)

        self.driver.find_element_by_name(self.billCountry_textbox_name).clear()
        self.driver.find_element_by_name(self.billCountry_textbox_name).send_keys(country)


    ############################################################################################################

    # Ship to Different Address
    #Different Shipping Address
    
    def tick_DifferentShippingAddress(self):
       self.driver.find_element_by_name("shippingAddressRequired").click()

    def DifferentShippingAddress(self, fname, lname, address1, city, state, zip, country):
        self.driver.find_element_by_name(self.shipToFirstName_textbox_name).clear()
        self.driver.find_element_by_name(self.shipToFirstName_textbox_name).send_keys(fname)

        self.driver.find_element_by_name(self.shipToLastName_textbox_name).clear()
        self.driver.find_element_by_name(self.shipToLastName_textbox_name).send_keys(lname)

        self.driver.find_element_by_name(self.shipAddress1_textbox_name).clear()
        self.driver.find_element_by_name(self.shipAddress1_textbox_name).send_keys(address1)

        self.driver.find_element_by_name(self.shipCity_textbox_name).clear()
        self.driver.find_element_by_name(self.shipCity_textbox_name).send_keys(city)

        self.driver.find_element_by_name(self.shipState_textbox_name).clear()
        self.driver.find_element_by_name(self.shipState_textbox_name).send_keys(state)

        self.driver.find_element_by_name(self.shipZip_textbox_name).clear()
        self.driver.find_element_by_name(self.shipZip_textbox_name).send_keys(zip)

        self.driver.find_element_by_name(self.shipCountry_textbox_name).clear()
        self.driver.find_element_by_name(self.shipCountry_textbox_name).send_keys(country)
    
    ############################################################################################################
    
    def click_continue(self):
        self.driver.find_element_by_name("newOrder").click()

    def click_confirm(self):
            self.driver.find_element_by_xpath("//a[@href='/actions/Order.action?newOrder=&confirmed=true']").click()


