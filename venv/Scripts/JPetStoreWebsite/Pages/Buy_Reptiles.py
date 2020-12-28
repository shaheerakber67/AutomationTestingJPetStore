from selenium.webdriver.support.ui import Select

class buyreptilespage():
    def __init__(self, driver):
        self.driver = driver
        # Rattlesnake Portion
        self.quantity_Rattlesnake_VenomlessRattlesnake_textbox_name = "EST-11"
        self.quantity_Rattlesnake_RattlelessRattlesnake_textbox_name = "EST-12"
        # Iguana Portion
        self.quantity_Iguana_GreenAdultIguana_textbox_name = "EST-13"
        # Update Cart
        self.update_textbox_name = "updateCartQuantities"

    # Catalog
    def click_reptiles(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewCategory=&categoryId=REPTILES']").click()

    # View Category

    # Rattlesnake Portion
    def click_Rattlesnake(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=RP-SN-01']").click()

    # Iguana Portion

    def click_Iguana(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=RP-LI-02']").click()

    # view Product
    # Rattlesnake Portion
    def click_Rattlesnake_VenomlessRattlesnake(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-11']").click()

    def click_Rattlesnake_RattlelessRattlesnake(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-12']").click()

    # Iguana Portion

    def click_Iguana_GreenAdultIguana(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-13']").click()

    # In view Item  click Add to cart
    # Rattlesnake Portion

    def click_add_to_cart_Rattlesnake_VenomlessRattlesnake(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-11']").click()

    def click_add_to_cart_Rattlesnake_RattlelessRattlesnake(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-12']").click()

    # Iguana Portion

    def click_add_to_cart_Iguana_GreenAdultIguana(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-13']").click()
        
    ########################################################
    
    def click_add_to_cart(self):
        self.driver.find_element_by_link_text("Add to Cart").click()

    ########################################################
    
    # add Item To Cart
    # Rattlesnake Portion

    def enter_quantity_Rattlesnake_VenomlessRattlesnake(self, qty):
        self.driver.find_element_by_name(self.quantity_Rattlesnake_VenomlessRattlesnake_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Rattlesnake_VenomlessRattlesnake_textbox_name).send_keys(qty)

    def enter_quantity_Rattlesnake_RattlelessRattlesnake(self, qty):
        self.driver.find_element_by_name(self.quantity_Rattlesnake_RattlelessRattlesnake_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Rattlesnake_RattlelessRattlesnake_textbox_name).send_keys(qty)

    # Iguana Portion

    def enter_quantity_Iguana_GreenAdultIguana(self, qty):
        self.driver.find_element_by_name(self.quantity_Iguana_GreenAdultIguana_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Iguana_GreenAdultIguana_textbox_name).send_keys(qty)

    # Update Cart

    def click_updatecart(self):
        self.driver.find_element_by_name(self.update_textbox_name).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Order.action?newOrderForm=']").click()


