class viewcartpage():
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox_name = "keyword"
        self.search_btn_name="searchProducts"

    def click_viewcart(self):
        self.driver.find_element_by_xpath(
            "//a[@href='/actions/Cart.action?viewCart=']").click()