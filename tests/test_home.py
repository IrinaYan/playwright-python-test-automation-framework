import allure
from playwright.sync_api import expect
from utils.logger import get_logger



logger = get_logger(__name__)


@allure.epic("Home Page")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Add product to the cart successfully")
def test_add_to_cart_from_recommended_products(home_page):
    home_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(home_page.home_page_link_text).to_be_visible()
    home_page.scroll_to_buttom_of_the_page()
    logger.info("Verifying reconmended product text is visible")
    expect(home_page.reconmended_product_text).to_be_visible()
    home_page.click_add_to_cart_recommended_product_button()
    home_page.click_view_cart()
    logger.info("Verifying shopping cart breadcrumb text is visible")
    expect(home_page.shopping_cart_breadcrumb_text).to_be_visible()
    logger.info("Verifying added product from cart page is visible")
    expect(home_page.added_product_from_cart_page).to_be_visible()




@allure.epic("Home Page")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Verify newsletter subscription on the Home page")
def test_verify_subscribtion_in_home_page(home_page, test_data: dict):
    home_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(home_page.home_page_link_text).to_be_visible()
    home_page.scroll_to_buttom_of_the_page()
    logger.info("Verifying subscribtion text is visible")
    expect(home_page.subscribtion_text).to_be_visible()
    home_page.input_email_in_subscribtion_field(test_data["subscribtion_email"])
    home_page.click_subscribtion_arrow_button()
    logger.info("Verifying alert success message is visible")
    expect(home_page.alert_success_message).to_be_visible()


@allure.epic("Home Page")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Verify scroll up arrow button works successfully")
def test_verify_scroll_up_arrow_button_functionality(home_page):
    home_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(home_page.home_page_link_text).to_be_visible()
    home_page.scroll_to_buttom_of_the_page()
    logger.info("Verifying subscribtion text is visible")
    expect(home_page.subscribtion_text).to_be_visible()  
    home_page.click_scrollup_arrow_button()
    #home_page.page.wait_for_timeout(500000)
    home_page.click_close_popup()
    logger.info("Verifying full fedged practice website text is visible")
    expect(home_page.full_fedged_practice_website_text).to_be_visible()



@allure.epic("Home Page")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Verify scroll-to-top functionality without using the arrow button")
def test_verify_scroll_up_without_Arrow_button(home_page):
    home_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(home_page.home_page_link_text).to_be_visible()
    home_page.scroll_to_buttom_of_the_page()
    logger.info("Verifying subscribtion text is visible")
    expect(home_page.subscribtion_text).to_be_visible()  
    home_page.page.evaluate("window.scrollTo(0, 0)")
    logger.info("Verifying full fedged practice website text is visible")
    expect(home_page.full_fedged_practice_website_text).to_be_visible()





