from playwright.sync_api import Locator, FrameLocator
from pages.base_page import BasePage
import re




class ProductsPage(BasePage):

    # LOCATORS

    @property
    def home_page_link_text(self) -> Locator:
        return self.page.get_by_role("link", name=" Home")

    @property
    def products_link(self) -> Locator:
        return self.page.get_by_role("link", name=" Products")

    @property
    def all_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name=re.compile("^All Products$"))

    @property
    def products_list(self) -> Locator:
        return self.page.locator('[class="product-image-wrapper"]')

    @property
    def view_product_link(self) -> Locator:
        return self.page.locator("//a[@href='/product_details/1' and text() = 'View Product']")



    @property
    def product_name_attribute(self) -> Locator:
        return self.page.locator("//div[@class='product-information']//h2")

    @property
    def product_category_attribute(self) -> Locator:
       return self.page.locator("p").filter(has_text="Category:")
    
    @property
    def product_availability_attribute(self) -> Locator:
       return self.page.locator("p").filter(has_text="Availability:")

    @property
    def product_condition_attribute(self) -> Locator:
        return self.page.locator("p").filter(has_text="Condition:")

    @property
    def product_brand_attribute(self) -> Locator:
        return self.page.locator("p").filter(has_text="Brand:")

    @property
    def product_price_attribute(self) -> Locator:
        return self.page.locator("//div[@class='product-information']//span/span")
    

    @property
    def ad_frame(self) -> FrameLocator:
        return self.page.frame_locator("#aswift_3")
  
    @property
    def close_popup(self) -> Locator:
        return self.ad_frame.get_by_text("Close", exact=True)


    @property
    def search_field(self) -> Locator:
        return self.page.get_by_placeholder("Search Product")

    
    @property
    def search_button(self) -> Locator:
        return self.page.locator("//input[@placeholder='Search Product']/following-sibling::button")

    
    @property
    def searched_product_text(self) -> Locator:
        return self.page.get_by_role("heading", name='Searched Products')

    @property
    def searched_product(self) -> Locator:
        return self.page.locator("//div[@class='overlay-content']//p[text() = 'Sleeveless Dress']")

    @property
    def first_item_cart(self) -> Locator:
        return self.page.locator("//div[@class='productinfo text-center']//a[@data-product-id='1']/ancestor::div[@class='col-sm-4']")

    @property
    def add_to_cart_button_first_item(self) -> Locator:
        return self.page.locator("//div[@class='overlay-content']//a[@data-product-id='1' and text() = 'Add to cart']")

    @property
    def product_added_text(self) -> Locator:
        return self.page.locator("//div[@id = 'cartModal']//h4[text() = 'Added!']")

    @property
    def continue_shopping_button(self) -> Locator:
        return self.page.get_by_role("button", name='Continue Shopping')

    @property
    def second_item_cart(self) -> Locator:
        return self.page.locator("//div[@class='productinfo text-center']//a[@data-product-id='2']/ancestor::div[@class='col-sm-4']")


    @property
    def add_to_cart_button_second_item(self) -> Locator:
        return self.page.locator("//div[@class='overlay-content']//a[@data-product-id='2' and text() = 'Add to cart']")


    
    @property
    def view_cart_link(self) -> Locator:
        return self.page.get_by_role("link", name='View Cart')

    @property
    def shopping_cart_breadcrumb_text(self) -> Locator:
        return self.page.get_by_text("Shopping Cart")


    @property
    def cart_product_quantity(self) -> Locator:
        return self.page.locator("#cart_info_table tbody tr#product-1, #cart_info_table tbody tr#product-2")


    @property
    def quantity_field(self) -> Locator:
        return self.page.locator("//input[@name='quantity']")


    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.get_by_role("button", name="Add to cart")

    @property
    def cart_quantity(self) -> Locator:
        return self.page.locator("//td[@class='cart_quantity']/button[text()='4']")


    @property
    def proceed_to_checkout_button(self) -> Locator:
        #return self.page.get_by_role("link", name="Proceed To Checkout")
        return self.page.get_by_text("Proceed To Checkout", exact=True)

    @property
    def to_proceed_on_checkout_text(self) -> Locator:
        return self.page.get_by_text("Register / Login account to proceed on checkout.")


    @property
    def register_login_to_proceed_checkout_link(self) -> Locator:
        return self.page.get_by_role("link", name="Register / Login")

    @property
    def new_user_signup_text(self) -> Locator:
        return self.page.get_by_role("heading", name="New User Signup!")


    @property
    def continue_button(self) -> Locator:
        return self.page.locator("//a[@data-qa = 'continue-button']")


    @property
    def cart_link(self) -> Locator:
        return self.page.get_by_role("link", name=' Cart')

    @property
    def breadcrumb_checkout(self) -> Locator:
        return self.page.locator("//ol[@class = 'breadcrumb']//li[text() = 'Checkout']")


    @property
    def your_delivery_address(self) -> Locator:
        return self.page.locator("//ul[@id = 'address_delivery']")

    @property
    def cart_info_product_name(self) -> Locator:
        return self.page.locator("//div[@id = 'cart_info']//a[text()='Blue Top']")

    @property
    def comment_about_order(self) -> Locator:
        return self.page.locator("//div[@id='ordermsg']//textarea")

    @property
    def place_order_button(self) -> Locator:
        return self.page.get_by_role("link", name='Place Order')


    @property
    def name_on_card_field(self) -> Locator:
        return self.page.locator("//input[@data-qa = 'name-on-card']")

    
    @property
    def card_number_field(self) -> Locator:
        return self.page.locator("//input[@data-qa = 'card-number']")

    @property
    def cvc_field(self) -> Locator:
        return self.page.locator("//input[@data-qa = 'cvc']")
    
    @property
    def expiration_MM_field(self) -> Locator:
        return self.page.locator("//input[@data-qa = 'expiry-month']")

    @property
    def expiration_YYYY_field(self) -> Locator:
        return self.page.locator("//input[@data-qa = 'expiry-year']")

    @property
    def pay_and_confirm_order_button(self) -> Locator:
        return self.page.locator("//button[@data-qa = 'pay-button']")

    @property
    def order_placed_text(self) -> Locator:
        return self.page.get_by_text("Congratulations! Your order has been confirmed!")

    @property 
    def logged_in_user_name_text(self) -> Locator:
        return self.page.get_by_text("Logged in as user12")

    @property
    def product_name_attribute_at_checkout_cart(self) -> Locator:
        return self.page.get_by_role("link", name="Blue Top")

    @property
    def cart_delete_icon(self) -> Locator:
        return self.page.locator("//td[@class='cart_delete']/a[@data-product-id='1']")

    @property
    def added_cart_products_rows(self) -> Locator:
        return self.page.locator("//tbody/tr")



    

    @property
    def category_section_text(self) -> Locator:
        return self.page.get_by_role('heading', name='Category')

    @property
    def women_category_plus_icon(self) -> Locator:
        return self.page.locator("//a[@href='#Women']/span")

    @property
    def women_category_dress(self) -> Locator:
        return self.page.locator("//div[@id='Women']//a[text()='Dress ']")

    @property
    def women_dress_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name='Women - Dress Products')

    @property
    def men_category_plus_icon(self) -> Locator:
        return self.page.locator("//a[@href='#Men']/span")

    @property
    def men_category_tshirts(self) -> Locator:
        return self.page.locator("//div[@id='Men']//a[text()='Tshirts ']")

    @property
    def men_tshirts_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Men - Tshirts Products")

    
    @property
    def kids_category_plus_icon(self) -> Locator:
        return self.page.locator("//a[@href='#Kids']/span")

    @property
    def kids_category_dress(self) -> Locator:
        return self.page.locator("//div[@id='Kids']//a[text()='Dress ']")

    @property
    def kids_dress_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Kids - Dress Products")

    
    @property
    def brands_text(self) -> Locator:
        return self.page.locator("//div[@class='brands_products']/h2[text()='Brands']")

    @property
    def brand_name_polo(self) -> Locator:
        return self.page.get_by_role("link", name='Polo')

    @property
    def brand_polo_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name='Brand - Polo Products')

    @property
    def brand_items_count_polo(self) -> Locator:
        return self.page.locator("//div[@class = 'features_items']//div[@class='col-sm-4']") 

   

    @property
    def brand_name_babyhug(self) -> Locator:
        return self.page.get_by_role("link", name='Babyhug')

    @property
    def brand_babyhug_products_text(self) -> Locator:
        return self.page.get_by_role("heading", name='Brand - Babyhug Products')
    
    @property
    def brand_items_count_babyhug(self) -> Locator:
        return self.page.locator("//div[@class = 'features_items']//div[@class='col-sm-4']")


    

    @property
    def write_your_review_text(self) -> Locator:
        return self.page.get_by_role("link", name='Write Your Review')

    @property
    def review_name_field(self) -> Locator:
        return self.page.get_by_placeholder('Your Name')

    
    @property
    def review_email_field(self) -> Locator:
        return self.page.locator('#email')

        
    @property
    def review_field(self) -> Locator:
        return self.page.get_by_placeholder('Add Review Here!')
    

    @property
    def review_submit_button(self) -> Locator:
        return self.page.locator("#button-review")

    @property
    def review_success_message(self) -> Locator:
        return self.page.locator("//span[text() = 'Thank you for your review.']")








    # ACTIONS

    def click_products_link(self) -> None:
        self.click(self.products_link, "'Products' link") 
        

    def click_view_product_link(self) -> None:
        self.click(self.view_product_link, "'View product' link")


    def click_close_popup(self) -> None:
        if self.page.locator('iframe[id="aswift_3"]').count() > 0:
            if self.close_popup.is_visible():
                self.click(self.close_popup, "'Close' popup icon")

    def fill_search_field(self, test_data: dict) -> None:
        self.fill(self.search_field, "'Search' field", test_data["search_item_name"])


    def click_search_button(self) -> None:
        self.click(self.search_button, "'Search' button")




    def add_first_item_to_cart(self) -> None:
        self.logger.info("Adding first item to cart")
        self.hover(self.first_item_cart, "First item cart")
        self.click(self.add_to_cart_button_first_item, "'Add to cart' button")

    def click_continue_shopping_button(self) -> Locator:
        self.click(self.continue_shopping_button, "'Continue shopping' button")


    def add_second_item_to_cart(self) -> None:
        self.logger.info("Adding second item to cart")
        self.hover(self.second_item_cart, "Second item cart")
        self.click(self.add_to_cart_button_second_item, "'Add to cart' button")

 
    def click_view_cart(self) -> None:
        self.click(self.view_cart_link, "'View cart' link")


    def increase_quantity(self, test_data: dict) -> None:
        self.fill(self.quantity_field, "Quantity field", test_data["quantity_field"])


    def add_to_cart_for_increased_quantity_item(self) -> None:
        self.click(self.add_to_cart_button, "'Add to cart' button")

    def click_proceed_to_checkout_button(self) -> None:
        self.click(self.proceed_to_checkout_button, "'Proceed to checkout' button")


    def click_register_login_to_proceed_checkout_link(self) -> None:
        self.click(self.register_login_to_proceed_checkout_link, "'Login to proceed to checkout' button")

    def click_continue_button(self) -> None:
        self.click(self.continue_button, "'Continure' button")


    def click_cart_link(self) -> None:
        self.click(self.cart_link, "'Cart' link")


    def input_comment_for_order(self, test_data: dict) -> None:
        self.fill(self.comment_about_order, "Comment about order", test_data["comment_for_prodcut"])

    def place_order(self) -> None:
        self.click(self.place_order_button, "'Place order' button")


    def fill_payment_card_fields(self, test_data: dict) -> None:
        self.logger.info("Filling payment card fields")
        self.fill(self.name_on_card_field, "'Name on card' field", test_data["name_on_card"])
        self.fill(self.card_number_field, "'Card number' field", test_data["card_number"])
        self.fill(self.cvc_field, "'CVC' field", test_data["cvc"])
        self.fill(self.expiration_MM_field, "'Expiration month' field", test_data["expiration_MM"])
        self.fill(self.expiration_YYYY_field, "'Expiration year' field", test_data["expiration_YYYY"])


    def click_pay_and_confirm_order_button(self) -> None:
        self.click(self.pay_and_confirm_order_button, "'Pay and Confirm order' buton")


    def click_cart_delete_icon(self) -> None:
        self.click(self.cart_delete_icon, "'Cart Delete' icon")


    def count_added_cart_products_rows(self) -> int:
        self.logger.info("Counting added cart products rows")
        return self.added_cart_products_rows.count()


    def filter_women_subcategory_item(self) -> None:
        self.logger.info("Filtering women subcategory item")
        self.click(self.women_category_plus_icon, "'Women category plus' icon")
        self.click(self.women_category_dress, "Women category dress")

    def filter_men_subcategory_item(self) -> None:
        self.logger.info("Filtering men subcategory item")
        self.click(self.men_category_plus_icon, "'Men category plus' icon")
        self.click(self.men_category_tshirts, "Men category tshirts")
        

    def filter_kids_subcategory_item(self) -> None:
        self.logger.info("Filtering kids subcategory item")
        self.click(self.kids_category_plus_icon, "'Kids category plus' icon")
        self.click(self.kids_category_dress, "Kids category dress")




    def filter_items_by_brand_polo(self) -> None:
        self.click(self.brand_name_polo, "Brand name Polo")


    def number_of_items_shown_polo(self) -> int:
        self.logger.info("Counting number of items for brand Polo")
        return self.brand_items_count_polo.count()


    def filter_items_by_brand_babyhug(self) -> None:
        self.click(self.brand_name_babyhug, "Brand name Babyhug")
        

    def number_of_items_shown_babyhug(self) -> int:
        self.logger.info("Counting number of items for brand Babyhug")
        return self.brand_items_count_babyhug.count()


    def fill_review_form(self, test_data: dict) -> None:
        self.logger.info("Filling review form")
        self.fill(self.review_name_field, "'Review name' field", test_data["name"])
        self.fill(self.review_email_field, "Review email' field", test_data["email"])
        self.fill(self.review_field, "'Review' field", test_data["review_message"])

    def click_review_submit_button(self) -> None:
        self.click(self.review_submit_button, "'Subbmit' button")
      


   

    
        





