import re
from playwright.sync_api import expect
from utils.logger import get_logger


logger = get_logger(__name__)


def test_contact_us_form(contact_us_page, test_data):  # fixture used

    contact_us_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(contact_us_page.home_page_link_text).to_be_visible()
    contact_us_page.click_contact_us_link()
    logger.info("Verifying that 'Get In Touch' text is visible")
    expect(contact_us_page.get_in_touch_text).to_be_visible()
    contact_us_page.fill_contact_us_form(test_data["contact_us"])
    contact_us_page.page.wait_for_timeout(5000)
    contact_us_page.upload_file_for_contact_us_form()
    contact_us_page.accept_dialog_popup()
    contact_us_page.click_submit_button()
    # contact_us_page.page.wait_for_timeout(5000)
    logger.info("Verifying that contact us success message is visible")
    expect(contact_us_page.contact_us_success_message).to_have_text(
        re.compile("Success! Your details have been submitted successfully."))
    contact_us_page.click_home_button()
    logger.info("Verifying that 'Home' link is visible")
    expect(contact_us_page.home_page_link_text).to_be_visible()
