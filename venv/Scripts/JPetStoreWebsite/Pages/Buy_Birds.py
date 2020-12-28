from selenium.webdriver.support.ui import Select


class buybirdpage():
    def __init__(self, driver):
        self.driver = driver
        # Amazon Parrot Portion
        self.quantity_AmazonParrot_AdultMaleAmazonParrot_textbox_name = "EST-18"
        # Finch Portion
        self.quantity_Finch_AdultMaleFinch_textbox_name = "EST-19"
        # Update Cart
        self.update_textbox_name = "updateCartQuantities"

    # Catalog

    def click_birds(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=BIRDS']").click()

    # View Category
    # Amazon Parrot Portion

    def click_AmazonParrot(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=AV-CB-01']").click()

    # Finch Portion

    def click_Finch(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=AV-SB-02']").click()

    # view Product
    # Amazon Parrot Portion

    def click_AmazonParrot_AdultMaleAmazonParrot(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-18']").click()

    # Finch Portion

    def click_Finch_AdultMaleFinch(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-19']").click()

    # In view Item  click Add to cart
    ########################################################

    def click_add_to_cart(self):
        self.driver.find_element_by_link_text("Add to Cart").click()

    ########################################################

    # add Item To Cart
    # Manx Portion

    def enter_quantity_AmazonParrot_AdultMaleAmazonParrot(self, qty):
        self.driver.find_element_by_name(self.quantity_AmazonParrot_AdultMaleAmazonParrot_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_AmazonParrot_AdultMaleAmazonParrot_textbox_name).send_keys(qty)

    # Persian Portion

    def enter_quantity_Finch_AdultMaleFinch(self, qty):
        self.driver.find_element_by_name(self.quantity_Persian_AdultFemalePersian_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Finch_AdultMaleFinch_textbox_name).send_keys(qty)

    # Update Cart

    def click_updatecart(self):
        self.driver.find_element_by_name(self.update_textbox_name).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Order.action?newOrderForm=']").click()


