class SearchBar():
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox_name = "keyword"
        self.search_btn_name="searchProducts"

    def enter_search(self, search):
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(search)
    def click_searchbutton(self):
        self.driver.find_element_by_name(self.search_btn_name).click()
