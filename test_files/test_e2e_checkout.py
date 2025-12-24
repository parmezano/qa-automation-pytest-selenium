import json
import os.path
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObject.login import LoginPage

test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance, test_list_item):
    driver = browser_instance

    login_page = LoginPage(driver)
    print(login_page.getTitle())
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page.go_to_cart()

    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()
