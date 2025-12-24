import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection"
    )


@pytest.fixture(scope="function")
def browser_instance(request):
    global driver
    browser_name = request.config.getoption("--browser_name")
    service_obj = Service()

    if browser_name == "chrome":
        options = Options()
        # Disable pop-ups and password manager
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            # disable leak detection
            "profile.password_manager_leak_detection": False,
            # disable auto-suggestions
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        # Disable notifications
        options.add_argument("--disable-notifications")

        # options.add_argument("--headless")

        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.implicitly_wait(4)
    else:
        raise ValueError(f"Unknown browser: {browser_name}")

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(4)
    yield driver
    driver.close()


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra
