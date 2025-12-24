Pytest Selenium UI Automation Framework

Portfolio UI test automation project built with Python 3.11, pytest, and Selenium WebDriver.

The project demonstrates how to design and implement a maintainable UI automation framework using Page Object Model (POM) and data-driven testing on a publicly available practice website.

⚠️ Important
The application under test is not owned by the author.
This repository contains only automated tests, created for learning and portfolio purposes.

⸻

Application Under Test

Practice website for QA automation:

https://rahulshettyacademy.com/loginpagePractise/

The application includes:
	•	Login form
	•	Product catalog
	•	Cart (basket)
	•	Checkout page

⸻

Test Coverage

Login
	•	Positive login
	•	Negative login (invalid credentials)
	•	Empty fields validation

Cart / Shop
	•	Adding products to the cart
	•	Verifying cart items

Checkout
	•	End-to-end checkout flow

End-to-End Scenarios
	•	Full flow: Login → Shop → Cart → Checkout

⸻

Tech Stack

Python 3.11
pytest
Selenium WebDriver
Page Object Model (POM)
JSON test data
pytest fixtures
pytest-html (HTML reports)


⸻

Project Structure
```text
QA_Automation/
├── data/          # Test data (JSON)
├── pageObject/    # Page Object Model
├── test_files/    # Tests and fixtures
├── utils/         # Helpers
├── pytest.ini
└── README.md
```

⸻

Test Execution

Install dependencies:
```text
pip install -r requirements.txt
```
Run tests from the test_files directory:
```
pytest
```

⸻

Browser Configuration

Tests run in Google Chrome.

Browser selection is implemented via pytest option:
```text
pytest --browser_name=chrome
```
Currently supported browsers:
	•	Chrome (default)

The option is implemented for future extensibility, although only Chrome is configured at the moment.

⸻

HTML Reports

HTML reports are generated manually using pytest-html:
```text
pytest --html=reports/report.html
```
Notes:
	•	Reports are generated locally
	•	The reports/ directory is created automatically on first run
	•	Only the report file is updated on subsequent runs

⸻

Purpose of the Project:

This is a portfolio project created after completing QA Automation training.

Project goals:
	•	Practice UI automation on a real, ready-made application
	•	Demonstrate clean automation architecture
	•	Apply Page Object Model and data-driven testing
	•	Showcase automation skills for CV and technical interviews

