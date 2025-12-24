import time
import json
import os.path
import sys
import pytest
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObject.login import LoginPage

test_data_path = '../data/test_login_negative.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_invalid_list = test_data["data"]
    test_empty_list = test_data["empty_data"]

ERROR_MESSAGE = (By.XPATH, "//div[@class='alert alert-danger col-md-12']//strong")


@pytest.mark.login
@pytest.mark.parametrize("test_list_item", test_invalid_list)
def test_login_with_invalid_credentials(browser_instance, test_list_item):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(test_list_item["user_login"],test_list_item["user_password"])
    time.sleep(3)

    error_message = driver.find_element(*ERROR_MESSAGE)

    assert "Incorrect" in error_message.text

@pytest.mark.login
@pytest.mark.parametrize("test_empty_fields_list", test_empty_list)
def test_login_empty(browser_instance, test_empty_fields_list):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(test_empty_fields_list["user_login"], test_empty_fields_list["user_password"])

    error_message = driver.find_element(*ERROR_MESSAGE)

    assert "Empty" in error_message.text