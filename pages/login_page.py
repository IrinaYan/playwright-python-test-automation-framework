from playwright.sync_api import Locator
from pages.base_page import BasePage
from utils.config import PASSWORD




class LoginPage(BasePage):

    # Locators

    @property
    def home_page_link_text(self) -> Locator:
        return self.page.get_by_role("link", name=" Home")

    @property
    def login_link(self) -> Locator:
        return self.page.get_by_role("link", name=" Signup / Login")

    @property
    def login_to_your_account_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Login to your account")

    @property
    def login_email_address_field(self) -> Locator:
        return self.page.locator("[data-qa='login-email']")

    @property
    def login_password_field(self) -> Locator:
        return self.page.locator("[data-qa='login-password']")

    @property
    def login_button(self) -> Locator:
        return self.page.get_by_role("button", name="Login")

    @property 
    def logged_in_user_name_text(self) -> Locator:
        return self.page.get_by_text("Logged in as user12")

    @property
    def login_error_message(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    @property
    def logout_link(self) -> Locator:
        return self.page.get_by_text(" Logout")
        # return self.page.locator("//a[@href = '/logout']")

    






    # Actions

    def click_signup_login_link(self) -> None:
        self.click(self.login_link, "'Login' link")

            
    def fill_login_form(self, email) -> None:
        self.logger.info("Filling login form with valid credentials")
        self.fill(self.login_email_address_field, "'Email address' field", email)
        self.fill(self.login_password_field, "'Password' field", PASSWORD) 


    def fill_login_form_with_invalid_email_format(self, test_data: dict) -> None:
        self.logger.info("Filling login form with invalid email format")
        self.fill(self.login_email_address_field, "'Email address' field", test_data["invalid_email"])
        self.fill(self.login_password_field, "'Passord' field", PASSWORD) 

    def click_login_button(self) -> None:
        self.click(self.login_button, "'Login' button")    

    def click_logout_link(self) -> None:
        self.click(self.logout_link, "'Logout' link")




 
     