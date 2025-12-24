from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browser_utils import BrowserUtils


class CheckoutConfirmation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")
        self.item_quantity = (By.XPATH, "//input[@id='exampleInputEmail1']")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, country_name):
        self.driver.find_element(*self.country_input).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        success_text = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_text



    def adjust_item_quantity(self):
        def parse_amount(text: str) -> int:
            return int(text.replace("₹.", "").strip())

        amount = self.driver.find_element(*self.item_quantity)
        curr_qty_element = self.driver.find_element(By.XPATH, "//td[@class='col-sm-1 col-md-1 text-center'][1]//strong")
        curr_sum_element = self.driver.find_element(By.XPATH, "//td[@class='col-sm-1 col-md-1 text-center'][2]//strong")
        for qty in ["20", "1", "3", "100"]:
            amount.clear()
            amount.send_keys(qty)
            curr_qty = int(amount.get_attribute("value"))
            curr_price = parse_amount(curr_qty_element.text)
            curr_sum = parse_amount(curr_sum_element.text)
            assert curr_qty == int(qty) and curr_qty * curr_price == curr_sum

    def delete_item(self, item_name):
        basket_items = self.driver.find_elements(By.XPATH, "//h4[@class='media-heading']")
        for i in range(0, len(basket_items)):
            if basket_items[i].text == item_name:
                self.driver.find_element(By.XPATH, f"//tbody/tr[{i+1}]/td[5]/button[1]").click()

        assert int(self.driver.find_element(By.XPATH, "//td[@class='text-right']//strong").text.replace("₹.", "").strip()) == 0
