import re
import pytest
import allure
from playwright.sync_api import expect
from utils.logger import get_logger



logger = get_logger(__name__)



@allure.epic("Login Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that the user can log in with valid email and password")

@pytest.mark.regression 
@pytest.mark.smoke
def test_login_with_correct_email_and_password(login_page, registered_user):  # fixture used

    login_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(login_page.home_page_link_text).to_be_visible()
    login_page.click_signup_login_link()
    logger.info("Verifying login to your account text is visible")
    expect(login_page.login_to_your_account_text).to_have_text(
        re.compile("Login to your account"))
    login_page.fill_login_form(registered_user["email"])
    login_page.click_login_button()
    logger.info("Verifying loggED in username text is visible")
    expect(login_page.logged_in_user_name_text).to_have_text(
        re.compile(" Logged in as user12"))



@allure.epic("Login Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that the user can not log invalid email")

@pytest.mark.regression
def test_login_with_incorrect_email(login_page, test_data):  # fixture used

    login_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(login_page.home_page_link_text).to_be_visible()
    login_page.click_signup_login_link()
    logger.info("Verifying login to your account text is visible")
    expect(login_page.login_to_your_account_text).to_have_text(
        re.compile("Login to your account"))
    login_page.fill_login_form(test_data["invalid_user"]["email"])
    login_page.click_login_button()
    logger.info("Verifying login error message is visible")
    expect(login_page.login_error_message).to_be_visible()

   


@allure.epic("Login Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that the user can not log in with invalid email format")

@pytest.mark.regression
def test_login_with_incorrect_email_format(login_page, test_data):  # fixture used

    login_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(login_page.home_page_link_text).to_be_visible()
    login_page.click_signup_login_link()
    logger.info("Verifying login to your account text is visible")
    expect(login_page.login_to_your_account_text).to_have_text(
        re.compile("Login to your account"))
    login_page.fill_login_form_with_invalid_email_format(test_data["invalid_user"])
    login_page.click_login_button()
    # error message is browser generated and not in the DOM, 
    # so we can't assert it with Playwright, but we can check the validity state of the email input field.
    
    email_field = login_page.login_email_address_field
    validity = email_field.evaluate(
        "el => ({ valid: el.validity.valid, typeMismatch: el.validity.typeMismatch, message: el.validationMessage })"
    )
   
    assert validity["valid"] is False
    assert validity["typeMismatch"] is True
    assert validity["message"] != ""



@allure.epic("Login Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify that the user can log out successfully")

@pytest.mark.regression
@pytest.mark.smoke
def test_logout_user(login_page, registered_user):  # fixture used
    login_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(login_page.home_page_link_text).to_be_visible()
    login_page.click_signup_login_link()
    logger.info("Verifying login to your account text is visible")
    expect(login_page.login_to_your_account_text).to_have_text(
            re.compile("Login to your account"))
    login_page.fill_login_form(registered_user["email"])
    login_page.click_login_button()
    logger.info("Verifying loggED in username text is visible")
    expect(login_page.logged_in_user_name_text).to_have_text(
            re.compile(" Logged in as user12"))
    login_page.click_logout_link()
    logger.info("Verifying login to your account text is visible")
    expect(login_page.login_to_your_account_text).to_have_text(
            re.compile("Login to your account"))
    
   