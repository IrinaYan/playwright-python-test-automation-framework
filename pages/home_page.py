from playwright.sync_api import Locator, FrameLocator
from pages.base_page import BasePage



class HomePage(BasePage):

    # LOCATORS

    @property
    def home_page_link_text(self) -> Locator:
        return self.page.get_by_role("link", name=" Home")

    @property
    def reconmended_product_text(self) -> Locator:
        return self.page.get_by_role("heading", name="recommended items")

    @property
    def add_to_cart_recommended_product_button(self) -> Locator:
        return self.page.locator("//img[@src='get_product_picture/5']/following-sibling::*[3]")

    @property
    def added_product_from_cart_page(self) -> Locator:
        return self.page.locator("//a[@href='/product_details/5']")

    @property
    def footer_bottom(self) -> Locator:
        return self.page.locator("#footer")

    @property
    def view_cart_link(self) -> Locator:
        return self.page.get_by_role("link", name='View Cart')

    @property
    def shopping_cart_breadcrumb_text(self) -> Locator:
        return self.page.get_by_text("Shopping Cart")
    

    @property
    def subscribtion_text(self) -> Locator:
        return self.page.get_by_role("heading", name = 'Subscription')

    @property
    def subscribtion_email_field(self) -> Locator:
        return self.page.locator('#susbscribe_email')

    @property
    def subscribtion_arrow_button(self) -> Locator:
        return self.page.locator('#subscribe')

    @property
    def alert_success_message(self) -> Locator:
        return self.page.locator("//div[text()= 'You have been successfully subscribed!']")

    
    @property
    def scrollup_arrow_button(self) -> Locator:
        return self.page.locator("#scrollUp")

    @property
    def full_fedged_practice_website_text(self) -> Locator:
        return self.page.locator("//div[@id='slider-carousel']//div[@class='carousel-inner']/div[1]//h2")
    

    @property
    def ad_frame(self) -> FrameLocator:
        return self.page.frame_locator("//iframe[@name = 'aswift_3']")


    @property
    def close_popup(self) -> Locator:
        return self.ad_frame.locator("//div[@id = 'dismiss-button-element']/div")


    



    
    


    # ACTIONS

    
    def click_add_to_cart_recommended_product_button(self) -> None:
        self.click(self.add_to_cart_recommended_product_button, "'Add to cart' button")

    def scroll_to_buttom_of_the_page(self) -> None:
        self.scroll(self.footer_bottom, "Footer area")

    def click_view_cart(self) -> None:
        self.click(self.view_cart_link, "'View cart' link")

    def input_email_in_subscribtion_field(self, test_data: dict) -> None:
        self.fill(self.subscribtion_email_field, "'Email' field", test_data["email"])

    def click_subscribtion_arrow_button(self) -> None:
        self.click(self.subscribtion_arrow_button, "'Arrow' button")

    def click_scrollup_arrow_button(self) -> None:
        self.click(self.scrollup_arrow_button, "Scrollup 'Arrow' button")


    def click_close_popup(self) -> None:
        if self.page.locator("//div[@id = 'dismiss-button-element']/div").count() > 0:
            if self.close_popup.is_visible():
                self.click(self.close_popup, "'Close' icon popup")
        







