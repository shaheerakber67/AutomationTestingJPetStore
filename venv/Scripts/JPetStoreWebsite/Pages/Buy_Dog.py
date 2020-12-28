from selenium.webdriver.support.ui import Select

class buydogpage():
    def __init__(self, driver):
        self.driver = driver
        # Bulldog Portion
        self.quantity_Bulldog_MaleAdultBulldog_textbox_name = "EST-6"
        self.quantity_Bulldog_FemalePuppyBulldog_textbox_name = "EST-7"
        # Poodle Portion
        self.quantity_Poodle_MalePuppyPoodle_textbox_name = "EST-8"
        # Dalmation Portion
        self.quantity_Dalmation_SpotlessMalePuppyDalmation_textbox_name = "EST-9"
        self.quantity_Dalmation_SpottedAdultFemaleDalmation_textbox_name = "EST-10"
        # Golden Retriever Portion
        self.quantity_GoldenRetriever_AdultFemaleGoldenRetriever_textbox_name = "EST-28"
        # Labrador Retriever Portion
        self.quantity_LabradorRetriever_AdultMaleLabradorRetriever1_textbox_name = "EST-22"
        self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever1_textbox_name = "EST-23"
        self.quantity_LabradorRetriever_AdultMaleLabradorRetriever2_textbox_name = "EST-24"
        self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever2_textbox_name = "EST-25"
        # Chihuahua Portion
        self.quantity_Chihuahua_AdultMaleChihuahua_textbox_name = "EST-26"
        self.quantity_Chihuahua_AdultFemaleChihuahua_textbox_name = "EST-27"

        #Update Cart
        self.update_textbox_name="updateCartQuantities"

    #Catalog
    def click_dog(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewCategory=&categoryId=DOGS']").click()

    #View Category

    # Bulldog Portion
    def click_Bulldog(self):
       self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewProduct=&productId=K9-BD-01']").click()

    # Poodle Portion

    def click_Poodle(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=K9-PO-02']").click()

    # Dalmation Portion

    def click_Dalmation(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=K9-DL-01']").click()

    # Golden Retriever Portion

    def click_GoldenRetriever(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=K9-RT-01']").click()

    # Labrador Retriever Portion

    def click_LabradorRetriever(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=K9-RT-02']").click()

    # Chihuahua Portion

    def click_Chihuahua(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=K29-CW-01']").click()

    #view Product
    #Bulldog Portion
    def click_Bulldog_MaleAdultBulldog(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-6']").click()

    def click_Bulldog_FemalePuppyBulldog(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-7']").click()

    # Poodle Portion

    def click_Poodle_MalePuppyPoodle(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-8']").click()

    #Dalmation Portion

    def click_Dalmation_SpotlessMalePuppyDalmation(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-9']").click()

    def click_Dalmation_SpottedAdultFemaleDalmation(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-10']").click()

    # Golden Retriever Portion

    def click_GoldenRetriever_AdultFemaleGoldenRetriever(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-28']").click()

    # Labrador Retriever Portion

    def click_LabradorRetriever_AdultMaleLabradorRetriever1(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-22']").click()

    def click_LabradorRetriever_AdultFemaleLabradorRetriever1(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-23']").click()

    def click_LabradorRetriever_AdultMaleLabradorRetriever2(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-24']").click()

    def click_LabradorRetriever_AdultFemaleLabradorRetriever2(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-25']").click()

    # Chihuahua Portion

    def click_Chihuahua_AdultMaleChihuahua(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-26']").click()

    def click_Chihuahua_AdultFemaleChihuahua(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-27']").click()

    #In view Item  click Add to cart
    # Bulldog Portion
    
    def click_add_to_cart_Bulldog_MaleAdultBulldog(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-6']").click()

    def click_add_to_cart_Bulldog_FemalePuppyBulldog(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-7']").click()

    # Poodle Portion

    def click_add_to_cart_Poodle_MalePuppyPoodle(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-8']").click()

    #Dalmation Portion
    
    def click_add_to_cart_Dalmation_SpotlessMalePuppyDalmation(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-9']").click()

    def click_add_to_cart_Dalmation_SpottedAdultFemaleDalmation(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-10']").click()

    # Golden Retriever Portion

    def click_add_to_cart_GoldenRetriever_AdultFemaleGoldenRetriever(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-28']").click()

    # Labrador Retriever Portion

    def click_add_to_cart_LabradorRetriever_AdultMaleLabradorRetriever1(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-22']").click()

    def click_add_to_cart_LabradorRetriever_AdultFemaleLabradorRetriever1(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-23']").click()

    def click_add_to_cart_LabradorRetriever_AdultMaleLabradorRetriever2(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-24']").click()

    def click_add_to_cart_LabradorRetriever_AdultMaleLabradorRetriever2(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-25']").click()

    # Chihuahua Portion

    def click_add_to_cart_Chihuahua_AdultMaleChihuahua(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-26']").click()

    def click_add_to_cart_Chihuahua_AdultFemaleChihuahua(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-27']").click()



    #add Item To Cart
    #Bulldog Portion

    def enter_quantity_Bulldog_MaleAdultBulldog(self,qty):
        self.driver.find_element_by_name(self.quantity_Bulldog_MaleAdultBulldog_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Bulldog_MaleAdultBulldog_textbox_name).send_keys(qty)

    def enter_quantity_Bulldog_FemalePuppyBulldog(self,qty):
        self.driver.find_element_by_name(self.quantity_Bulldog_FemalePuppyBulldog_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Bulldog_FemalePuppyBulldog_textbox_name).send_keys(qty)

    # Poodle Portion

    def enter_quantity_Poodle_MalePuppyPoodle(self, qty):
        self.driver.find_element_by_name(self.quantity_Poodle_MalePuppyPoodle_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Poodle_MalePuppyPoodle_textbox_name).send_keys(qty)

    # Dalmation Portion

    def enter_quantity_Dalmation_SpotlessMalePuppyDalmation(self, qty):
        self.driver.find_element_by_name(self.quantity_Dalmation_SpotlessMalePuppyDalmation_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Dalmation_SpotlessMalePuppyDalmation_textbox_name).send_keys(qty)

    def enter_quantity_Dalmation_SpottedAdultFemaleDalmation(self, qty):
        self.driver.find_element_by_name(self.quantity_Dalmation_SpottedAdultFemaleDalmation_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Dalmation_SpottedAdultFemaleDalmation_textbox_name).send_keys(qty)

    # Golden Retriever Portion

    def enter_quantity_Goldfish_Adult_Male_Goldfish(self, qty):
        self.driver.find_element_by_name(self.quantity_GoldenRetriever_AdultFemaleGoldenRetriever_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_GoldenRetriever_AdultFemaleGoldenRetriever_textbox_name).send_keys(qty)
        
    # Labrador Retriever Portion

    def enter_quantity_LabradorRetriever_AdultMaleLabradorRetriever1(self, qty):
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultMaleLabradorRetriever1_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultMaleLabradorRetriever1_textbox_name).send_keys(qty)

    def enter_quantity_LabradorRetriever_AdultFemaleLabradorRetriever1(self, qty):
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever1_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever1_textbox_name).send_keys(qty)
    
    def enter_quantity_LabradorRetriever_AdultMaleLabradorRetriever2(self, qty):
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultMaleLabradorRetriever2_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultMaleLabradorRetriever2_textbox_name).send_keys(qty)
    
    def enter_quantity_LabradorRetriever_AdultFemaleLabradorRetriever2(self, qty):
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever2_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_LabradorRetriever_AdultFemaleLabradorRetriever2_textbox_name).send_keys(qty)

    # Chihuahua Portion

    def enter_quantity_Chihuahua_AdultMaleChihuahua(self, qty):
        self.driver.find_element_by_name(self.quantity_Chihuahua_AdultMaleChihuahua_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Chihuahua_AdultMaleChihuahua_textbox_name).send_keys(qty)
    
    def enter_quantity_Chihuahua_AdultFemaleChihuahua(self, qty):
        self.driver.find_element_by_name(self.quantity_Chihuahua_AdultFemaleChihuahua_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Chihuahua_AdultFemaleChihuahua_textbox_name).send_keys(qty)
        
    # Update Cart
    
    def click_updatecart(self):
        self.driver.find_element_by_name(self.update_textbox_name).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath( "//a[@href='/actions/Order.action?newOrderForm=']").click()


