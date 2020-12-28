from selenium.webdriver.support.ui import Select


class buycatpage():
    def __init__(self, driver):
        self.driver = driver
        # Manx Portion
        self.quantity_Manx_TaillessManx_textbox_name = "EST-14"
        self.quantity__Manx_WithtailManx_textbox_name = "EST-15"
        # Persian Portion
        self.quantity_Persian_AdultFemalePersian_textbox_name = "EST-16"
        self.quantity_Persian_AdultMalePersian_textbox_name = "EST-17"
        # Update Cart
        self.update_textbox_name = "updateCartQuantities"

    # Catalog
    def click_cat(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=CATS']").click()

    # View Category
    # Manx Portion
    def click_Manx(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=FL-DSH-01']").click()

    # Persian Portion

    def click_Persian(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=FL-DLH-02']").click()

    # view Product
    # Manx Portion
    def click_Manx_TaillessManx(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-14']").click()

    def click_Manx_WithtailManx(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-15']").click()

    # Persian Portion

    def click_Persian_AdultFemalePersian(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-16']").click()

    def click_Persian_AdultMalePersian(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-17']").click()

    # In view Item  click Add to cart
    ########################################################

    def click_add_to_cart(self):
        self.driver.find_element_by_link_text("Add to Cart").click()

    ########################################################

    # add Item To Cart
    # Manx Portion

    def enter_quantity_Manx_TaillessManx(self, qty):
        self.driver.find_element_by_name(self.quantity_Manx_TaillessManx_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Manx_TaillessManx_textbox_name).send_keys(qty)

    def enter_quantity_Manx_WithtailManx(self, qty):
        self.driver.find_element_by_name(self.quantity__Manx_WithtailManx_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity__Manx_WithtailManx_textbox_name).send_keys(qty)

    # Persian Portion

    def enter_quantity_Persian_AdultFemalePersian(self, qty):
        self.driver.find_element_by_name(self.quantity_Persian_AdultFemalePersian_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Persian_AdultFemalePersian_textbox_name).send_keys(qty)
        
    def enter_quantity_Persian_AdultMalePersian(self, qty):
        self.driver.find_element_by_name(self.quantity_Persian_AdultMalePersian_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Persian_AdultMalePersian_textbox_name).send_keys(qty)

    # Update Cart

    def click_updatecart(self):
        self.driver.find_element_by_name(self.update_textbox_name).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Order.action?newOrderForm=']").click()


