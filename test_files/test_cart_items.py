import json
import os.path
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObject.login import LoginPage

test_data_path = '../data/test_basketItems.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.basket
@pytest.mark.parametrize("test_list_item", test_list)
def test_add_item_to_cart(browser_instance, test_list_item):
    driver = browser_instance

    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["item"])
    shop_page.go_to_cart()


@pytest.mark.basket
@pytest.mark.parametrize("test_list_item", test_list)
def test_adjust_item_quantity_and_remove(browser_instance, test_list_item):
    driver = browser_instance

    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["item"])

    checkout_page = shop_page.go_to_cart()
    checkout_page.adjust_item_quantity()
    checkout_page.delete_item(test_list_item["item"])