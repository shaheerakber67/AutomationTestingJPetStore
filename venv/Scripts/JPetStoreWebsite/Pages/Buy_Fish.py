from selenium.webdriver.support.ui import Select
class buyfishpage():
    def __init__(self, driver):
        self.driver = driver
        # Angelfish Portion
        self.quantity_Angelfish_Large_Angelfish_textbox_name = "EST-1"
        self.quantity_Angelfish_Small_Angelfish_textbox_name = "EST-2"
        # TigerShark Portion
        self.quantity_TigerShark_Toothless_TigerShark_textbox_name = "EST-3"
        # Koi Portion
        self.quantity_Koi_Spotted_Koi_textbox_name = "EST-4"
        self.quantity_Koi_Spotless_Koi_textbox_name = "EST-5"
        # Goldfish Portion
        self.quantity_Goldfish_Adult_Male_Goldfish_textbox_name = "EST-20"
        self.quantity_Goldfish_Adult_Female_Goldfish_textbox_name = "EST-21"
        #Update Cart
        self.update_textbox_name="updateCartQuantities"

   # #Catalog
    def click_fish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewCategory=&categoryId=FISH']").click()

    # #View Category

    # #Angelfish Portion
    def click_Angelfish(self):
       self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewProduct=&productId=FI-SW-01']").click()

    #TigerShark Portion

    def click_TigerShark(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=FI-SW-02']").click()

    #Koi Portion

    def click_Koi(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=FI-FW-01']").click()

    #Goldfish Portion

    def click_Goldfish(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Catalog.action?viewProduct=&productId=FI-FW-02']").click()

    #view Product
    #Angelfish Portion
    def click_Angelfish_Large_Angelfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-1']").click()

    def click_Angelfish_Small_Angelfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-2']").click()

    #TigerShark Portion

    def click_TigerShark_Toothless_TigerShark(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-3']").click()

    #Koi Portion


    def click_Koi_Spotted_Koi(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-4']").click()

    def click_Koi_Spotless_Koi(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-5']").click()


    #Goldfish Portion

    def click_Goldfish_Adult_Male_Goldfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-20']").click()

    def click_Goldfish_Adult_Female_Goldfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Catalog.action?viewItem=&itemId=EST-21']").click()

    #In view Item  click Add to cart
     #Angelfish Portion
    def click_add_to_cart_Angelfish_Large_Angelfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-1']").click()

    def click_add_to_cart_Angelfish_Small_Angelfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-2']").click()

    #TigerShark Portion

    def click_add_to_cart_TigerShark_Toothless_TigerShark(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-3']").click()

    #Koi Portion
    def click_add_to_cart_Koi_Spotted_Koi(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-4']").click()

    def click_add_to_cart_Koi_Spotless_Koi(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-5']").click()

    #Goldfish Portion

    def click_add_to_cart_Goldfish_Adult_Male_Goldfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-20']").click()

    def click_add_to_cart_Goldfish_Adult_Female_Goldfish(self):
        self.driver.find_element_by_xpath("//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-21']").click()

    #add Item To Cart
    #Angelfish Portion

    def enter_quantity_Angelfish_Large_Angelfish(self,qty):
        self.driver.find_element_by_name(self.quantity_Angelfish_Large_Angelfish_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Angelfish_Large_Angelfish_textbox_name).send_keys(qty)

    def enter_quantity_Angelfish_Small_Angelfish(self,qty):
        self.driver.find_element_by_name(self.quantity_Angelfish_Small_Angelfish_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Angelfish_Small_Angelfish_textbox_name).send_keys(qty)

    # TigerShark Portion

    def enter_quantity_TigerShark_Toothless_TigerShark(self, qty):
        self.driver.find_element_by_name(self.quantity_TigerShark_Toothless_TigerShark_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_TigerShark_Toothless_TigerShark_textbox_name).send_keys(qty)

    #Koi Portion

    def enter_quantity_Koi_Spotted_Koi(self, qty):
        self.driver.find_element_by_name(self.quantity_Koi_Spotted_Koi_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Koi_Spotted_Koi_textbox_name).send_keys(qty)

    def enter_quantity_Koi_Spotless_Koi(self, qty):
        self.driver.find_element_by_name(self.quantity_Koi_Spotless_Koi_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Koi_Spotless_Koi_textbox_name).send_keys(qty)

    #Goldfish Portion

    def enter_quantity_Goldfish_Adult_Male_Goldfish(self, qty):
        self.driver.find_element_by_name(self.quantity_Goldfish_Adult_Male_Goldfish_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Goldfish_Adult_Male_Goldfish_textbox_name).send_keys(qty)

    def enter_quantity_Goldfish_Adult_Female_Goldfish(self, qty):
        self.driver.find_element_by_name(self.quantity_Goldfish_Adult_Female_Goldfish_textbox_name).clear()
        self.driver.find_element_by_name(self.quantity_Goldfish_Adult_Female_Goldfish_textbox_name).send_keys(qty)

    # # Update Cart
    def click_updatecart(self):
        self.driver.find_element_by_name(self.update_textbox_name).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath( "//a[@href='/actions/Order.action?newOrderForm=']").click()