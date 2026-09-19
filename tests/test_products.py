import re
import pytest
from playwright.sync_api import expect
from utils.logger import get_logger



logger = get_logger(__name__)



@pytest.mark.regression 
@pytest.mark.smoke
def test_products_link_navigates_to_products_page(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    # products_page.page.pause()
    #products_page.page.wait_for_timeout(5000)
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    logger.info("Verifying roducts list first is visible")
    expect(products_page.products_list.first).to_be_visible()




@pytest.mark.regression 
@pytest.mark.smoke
def test_verify_product_detail_is_visible(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    #products_page.page.wait_for_timeout(500000)
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    logger.info("Verifying roducts list first is visible") 
    expect(products_page.products_list.first).to_be_visible()
    products_page.click_view_product_link()
    logger.info("Verifying product name attribute is visible")
    expect(products_page.product_name_attribute).to_have_text(re.compile(r".+"))
    logger.info("Verifying category attribute is visible")
    expect(products_page.product_category_attribute).to_be_visible()
    logger.info("Verifying availability attribute is visible")
    expect(products_page.product_availability_attribute).to_be_visible()
    logger.info("Verifying condition attribute is visible")
    expect(products_page.product_condition_attribute).to_be_visible()
    logger.info("Verifying brand attribute is visible")
    expect(products_page.product_brand_attribute).to_be_visible()
    logger.info("Verifying price attribute is visible")
    expect(products_page.product_price_attribute).to_be_visible()
    logger.info("Verifying page to have 'product_details' url")
    expect(products_page.page).to_have_url(
        re.compile(r".*/product_details/\d+"))



@pytest.mark.regression 
@pytest.mark.smoke
def test_search_particular_product(products_page, test_data):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.fill_search_field(test_data["products"])
    products_page.click_search_button()
    logger.info("Verifying searched product text is visible")
    expect(products_page.searched_product_text).to_be_visible()
    logger.info("Verifying searched certain product text is visible")
    expect(products_page.searched_product).to_have_text(
        test_data["products"]["search_item_name"])



@pytest.mark.regression 
@pytest.mark.smoke
def test_add_products_in_cart(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.add_first_item_to_cart()
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_continue_shopping_button()
    products_page.add_second_item_to_cart()
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_view_cart()
    logger.info("Verifying shopping cart breadcrumb text is visible")
    expect(products_page.shopping_cart_breadcrumb_text).to_be_visible()
    logger.info("Verifying cart product quantity")
    expect(products_page.cart_product_quantity).to_have_count(2)




@pytest.mark.regression 
@pytest.mark.smoke
def test_verify_product_quantity_in_cart(products_page, test_data: dict):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.click_view_product_link()
    logger.info("Verifying product name attribute is visible")
    expect(products_page.product_name_attribute).to_have_text(re.compile(r".+"))
    products_page.increase_quantity(test_data["products"])
    products_page.add_to_cart_for_increased_quantity_item()
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_view_cart()
    logger.info("Verifying shopping cart breadcrumb text is visible")
    expect(products_page.shopping_cart_breadcrumb_text).to_be_visible()
    logger.info("Verifying cart quantity to have certain text")
    expect(products_page.cart_quantity).to_have_text(
        test_data["products"]["quantity_field"])

    


@pytest.mark.regression 
@pytest.mark.smoke
def test_place_order_register_while_checkout(products_page, signup_page, test_data: dict):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.add_first_item_to_cart()
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_view_cart()
    logger.info("Verifying shopping cart breadcrumb text is visible")
    expect(products_page.shopping_cart_breadcrumb_text).to_be_visible()
    products_page.click_proceed_to_checkout_button()
    logger.info("Verifying to proceed on checkout text is visible")
    expect(products_page.to_proceed_on_checkout_text).to_be_visible()
    products_page.click_register_login_to_proceed_checkout_link()
    logger.info("Verifying new user signup text is visible")
    expect(products_page.new_user_signup_text).to_be_visible()

    signup_page.open_signup_form(test_data["valid_user"])
    logger.info("Verifying enter account information text is visible")
    expect(signup_page.enter_account_information_text).to_have_text(
        re.compile("Enter Account Information"))
    signup_page.enter_account_info(test_data["valid_user"])
    signup_page.check_signup_for_newsletter_checkbox()
    signup_page.enter_address_info(test_data["valid_user"])
    signup_page.click_create_account_button()
    logger.info("Verifying account created text is visible")
    expect(signup_page.account_created_text).to_have_text(
        re.compile("Account Created!"))

    products_page.click_continue_button()
    logger.info("Verifying logged in user name text is visible")
    expect(products_page.logged_in_user_name_text).to_have_text(
        re.compile(" Logged in as user12"))
    products_page.click_cart_link()
    products_page.click_proceed_to_checkout_button()
    logger.info("Verifying breadcrumb checkout text is visible") 
    expect(products_page.breadcrumb_checkout).to_be_visible()

    address = test_data["valid_user"]
    for value in ["first_name", "last_name", "company", "address", "city", "country"]:
        logger.info("Verifying your delivery address to contain certain text") 
        expect(products_page.your_delivery_address).to_contain_text(address[value])

    logger.info("Verifying cart info product name is visible")
    expect(products_page.cart_info_product_name).to_contain_text(
        products_page.product_name_attribute_at_checkout_cart.text_content()) # inner_text()

    products_page.input_comment_for_order(test_data["products"])
    products_page.place_order()

    products_page.fill_payment_card_fields(test_data["product_payment_details"])
    products_page.click_pay_and_confirm_order_button()
    logger.info("Verifying order placed text is visible")
    expect(products_page.order_placed_text).to_be_visible()



@pytest.mark.regression 
@pytest.mark.smoke
def test_remove_products_from_cart(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.add_first_item_to_cart()
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_continue_shopping_button()
    products_page.add_second_item_to_cart() 
    logger.info("Verifying product added text is visible")
    expect(products_page.product_added_text).to_be_visible()
    products_page.click_view_cart()
    logger.info("Verifying shopping cart breadcrumb text is visible")
    expect(products_page.shopping_cart_breadcrumb_text).to_be_visible()
    logger.info("Counting added cart products rows")
    expect(products_page.added_cart_products_rows).to_have_count(2)
    products_page.click_cart_delete_icon()
    logger.info("Counting added cart products rows")
    expect(products_page.added_cart_products_rows).to_have_count(1)



@pytest.mark.regression 
@pytest.mark.smoke
def test_verify_category_section_filters_properly(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    logger.info("Verifying category section text is visible")
    expect(products_page.category_section_text).to_be_visible()
    products_page.filter_women_subcategory_item()
    logger.info("Verifying women dress products text is visible")
    expect(products_page.women_dress_products_text).to_be_visible()
    products_page.filter_men_subcategory_item()
    logger.info("Verifying men tshirts products text is visible")
    expect(products_page.men_tshirts_products_text).to_be_visible()
    products_page.filter_kids_subcategory_item()
    logger.info("Verifying kids dress products text is visible")
    expect(products_page.kids_dress_products_text).to_be_visible()



@pytest.mark.regression 
@pytest.mark.smoke
def test_verify_brand_page_shows_products(products_page):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    logger.info("Verifying brands text is visible")
    expect(products_page.brands_text).to_be_visible()
    products_page.filter_items_by_brand_polo()
    logger.info("Verifying brand Polo products text is visible") 
    expect(products_page.brand_polo_products_text).to_be_visible()
    assert products_page.number_of_items_shown_polo() > 0
    products_page.filter_items_by_brand_babyhug()
    logger.info("Verifying brand Babyhug products text is visible") 
    expect(products_page.brand_babyhug_products_text).to_be_visible()
    assert products_page.number_of_items_shown_babyhug() > 0



@pytest.mark.regression 
@pytest.mark.smoke
def test_add_review_on_product(products_page, test_data: dict):
    products_page.open_base_url()
    logger.info("Verifying that the 'Home' link is visible")
    expect(products_page.home_page_link_text).to_be_visible()
    products_page.click_products_link()
    products_page.click_close_popup()
    logger.info("Verifying 'All products'text is visible")
    expect(products_page.all_products_text).to_be_visible()
    products_page.click_view_product_link()
    logger.info("Verifying write your review text is visible")
    expect(products_page.write_your_review_text).to_be_visible()
    products_page.fill_review_form(test_data["review_inputs"])
    products_page.click_review_submit_button()
    logger.info("Verifying review success message is visible")
    expect(products_page.review_success_message).to_be_visible()




