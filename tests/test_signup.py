import re
import pytest
from playwright.sync_api import expect
from utils.logger import get_logger



logger = get_logger(__name__)





@pytest.mark.regression
@pytest.mark.smoke
def test_fill_new_user_signup_form_with_valid_credentials(signup_page, test_data):    #fixture used
    
    signup_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(signup_page.home_page_link_text).to_be_visible()
    signup_page.click_new_user_sign_up_link()
    logger.info("Verifying new user signup text is visible")
    expect(signup_page.new_user_signup_text).to_have_text(re.compile("New User Signup!"))
    signup_page.fill_new_user_signup_form(test_data["valid_user"])
    signup_page.click_new_user_sign_up_button()
    logger.info("Verifying enter account information text is visible")
    expect(signup_page.enter_account_information_text).to_have_text(re.compile("Enter Account Information"))


@pytest.mark.regression
def test_fill_new_user_signup_form_with_invalid_email_format(signup_page, test_data):
    signup_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(signup_page.home_page_link_text).to_be_visible()
    signup_page.click_new_user_sign_up_link() 
    logger.info("Verifying new user signup text is visible") 
    expect(signup_page.new_user_signup_text).to_have_text(re.compile("New User Signup!"))
    signup_page.fill_new_user_signup_form_with_ivalid_email_format(test_data["invalid_user"])
    signup_page.click_new_user_sign_up_button()
    # error message is browser generated and not in the DOM, 
    # so we can't assert it with Playwright, but we can check the validity state of the email input field.

    email_field = signup_page.email_address_field
    validity = email_field.evaluate("el => ({ valid: el.validity.valid, typeMismatch: el.validity.typeMismatch, message: el.validationMessage })")
       
    assert validity["valid"] is False
    assert validity["typeMismatch"] is True
    assert validity["message"] != "" 



@pytest.mark.regression
@pytest.mark.smoke
def test_valid_user_signup_form_submission(signup_page, test_data):     #fixture used
    
    signup_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(signup_page.home_page_link_text).to_be_visible()
    signup_page.click_new_user_sign_up_link()
    logger.info("Verifying new user signup text is visible")
    expect(signup_page.new_user_signup_text).to_have_text(re.compile("New User Signup!"))
    signup_page.open_signup_form(test_data["valid_user"])
    logger.info("Verifying enter account information text is visible")
    expect(signup_page.enter_account_information_text).to_have_text(re.compile("Enter Account Information"))
    signup_page.enter_account_info(test_data["valid_user"])
    signup_page.check_signup_for_newsletter_checkbox()
    signup_page.enter_address_info(test_data["valid_user"])
    signup_page.click_create_account_button()
    logger.info("Verifying account created text is visible")
    expect(signup_page.account_created_text).to_have_text(re.compile("Account Created!"))
    signup_page.click_continue_button()
    logger.info("Verifying logged in user name text is visible")
    expect(signup_page.logged_in_user_name_text).to_be_visible()
    signup_page.click_delete_account_link()
    logger.info("Verifying account deleted text is visible")
    expect(signup_page.account_deleted_text).to_be_visible()
    signup_page.click_continue_button_on_deleted_account_page()
    logger.info("Verifying home page link text is visible")
    expect(signup_page.home_page_link_text).to_be_visible()



@pytest.mark.regression
def test_signup_with_existing_email(signup_page, test_data, registered_user):
    signup_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(signup_page.home_page_link_text).to_be_visible()
    signup_page.click_new_user_sign_up_link()
    logger.info("Verifying new user signup text is visible")
    expect(signup_page.new_user_signup_text).to_have_text(re.compile("New User Signup!"))
    signup_page.fill_new_user_signup_form(registered_user)
    signup_page.click_new_user_sign_up_button()
    logger.info("Verifying email address exists error message is visible")
    expect(signup_page.email_address_exists_error_message).to_be_visible()










    

  







