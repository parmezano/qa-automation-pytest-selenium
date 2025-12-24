import time
import json
import os.path
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pageObject.login import LoginPage

test_data_path = '../data/test_login_positive.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.login
@pytest.mark.parametrize("test_list_item", test_list)
def test_login_with_valid_credentials(browser_instance, test_list_item):
    driver = browser_instance
    login_page = LoginPage(driver)
    login_page.login(test_list_item["user_login"],test_list_item["user_password"])
    time.sleep(4)

    assert "shop" in driver.current_url.lower()
