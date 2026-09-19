import pytest
import json
import uuid
import os
import re
import allure
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.base_page import BasePage
from pages.contact_us_page import ContactUs
from pages.products_page import ProductsPage
from pages.home_page import HomePage
from playwright.sync_api import expect
from utils.allure_environment import create_environment_file





# Returns object
@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

# Returns object
@pytest.fixture
def home_page(page: Page):
    return HomePage(page)

# Returns object
@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

# Returns object
@pytest.fixture
def signup_page(page: Page):
    return SignupPage(page)

# Returns object
@pytest.fixture
def contact_us_page(page: Page):
    return ContactUs(page)

# Returns object
@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)




@pytest.fixture 
def test_data():
    with open("test_data/test_data.json", encoding="utf-8") as file:
        data = json.load(file)
    # Generate a unique email address for the valid user to avoid conflicts during testing
    data["valid_user"]["email"] = f"user_{uuid.uuid4().hex[:8]}@gmail.com"
    return data




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    yield

    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = request.node.name.replace("[", "_").replace("]", "_")

        screenshot_path = f"screenshots/{screenshot_name}.png"

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        # Attach screenshot to Allure report
        with open(screenshot_path, "rb") as screenshot:
            allure.attach(
                screenshot.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture
def registered_user(signup_page, login_page, test_data):
    signup_page.open_base_url()
    expect(signup_page.home_page_link_text).to_be_visible()
    signup_page.click_new_user_sign_up_link()
    expect(signup_page.new_user_signup_text).to_have_text(re.compile("New User Signup!"))
    signup_page.open_signup_form(test_data["valid_user"])
    expect(signup_page.enter_account_information_text).to_have_text(re.compile("Enter Account Information"))
    signup_page.enter_account_info(test_data["valid_user"])
    signup_page.check_signup_for_newsletter_checkbox()
    signup_page.enter_address_info(test_data["valid_user"])
    signup_page.click_create_account_button()
    expect(signup_page.account_created_text).to_have_text(re.compile("Account Created!"))
    signup_page.click_continue_button()
    expect(signup_page.logged_in_user_name_text).to_be_visible()
    login_page.click_logout_link()
    expect(login_page.login_to_your_account_text).to_have_text(
                re.compile("Login to your account"))

    return test_data["valid_user"] 
  
    

@pytest.fixture(autouse=True)
def allure_browser_info(browser_name):
    allure.dynamic.parameter("Browser", browser_name)
  


@pytest.fixture(scope="session", autouse=True)
def allure_environment(browser):
    create_environment_file(browser)


