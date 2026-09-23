from playwright.sync_api import Locator
from pages.base_page import BasePage
from utils.config import PASSWORD 



class SignupPage(BasePage):

    # Locators

    @property
    def home_page_link_text(self) -> Locator:
        return self.page.get_by_role("link", name=" Home")

    @property
    def new_user_sign_up_link(self) -> Locator:
        return self.page.get_by_role("link", name=" Signup / Login")

    @property
    def new_user_signup_text(self) -> Locator:
        return self.page.get_by_role("heading", name="New User Signup!")

    @property
    def name_field(self) -> Locator:
        return self.page.get_by_placeholder("Name")

    @property
    def email_address_field(self) -> Locator:
        return self.page.locator('[data-qa="signup-email"]')

    @property
    def signup_button(self) -> Locator:
        return self.page.get_by_role("button", name="Signup")

    @property
    def enter_account_information_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Enter Account Information")

    @property
    def radio_button_Mrs(self) -> Locator:
        return self.page.locator("#id_gender2")

    @property
    def name_field_signup_page(self) -> Locator:
        return self.page.locator("#name")

    @property
    def email_field_signup_page(self) -> Locator:
        return self.page.locator('#email')

    @property
    def password_field_signup_page(self) -> Locator:
        return self.page.locator("#password")

    @property
    def select_day_of_birth(self) -> Locator:
        return self.page.locator("#days")

    @property
    def select_month_of_birth(self) -> Locator:
        return self.page.locator("#months")

    @property
    def select_year_of_birth(self) -> Locator:
        return self.page.locator("#years")

    @property
    def checkbox_sign_up_for_our_newsletter(self) -> Locator:
        return self.page.locator("#newsletter")

    @property
    def first_name_field(self) -> Locator:
        return self.page.locator("#first_name")

    @property
    def last_name_field(self) -> Locator:
        return self.page.locator("#last_name")

    @property
    def company_field(self) -> Locator:
        return self.page.locator("#company")

    @property
    def address_field(self) -> Locator:
        return self.page.locator("#address1")

    @property
    def select_country(self) -> Locator:
        return self.page.locator("#country")

    @property
    def state_field(self) -> Locator:
        return self.page.locator("#state")

    @property
    def city_field(self) -> Locator:
        return self.page.locator("#city")

    @property
    def zipcode_field(self) -> Locator:
        return self.page.locator("#zipcode")

    @property
    def mobile_number_field(self) -> Locator:
        return self.page.locator("#mobile_number")

    @property
    def create_account_button(self) -> Locator:
        return self.page.get_by_role("button", name="Create Account")

    @property
    def account_created_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Account Created!")


    @property
    def continue_button(self) -> Locator:
        return self.page.get_by_text("Continue")


    @property
    def logged_in_user_name_text(self) -> Locator:
        return self.page.get_by_text(" Logged in as user12")


    @property
    def email_address_exists_error_message(self) -> Locator:
        return self.page.get_by_text("Email Address already exist!")
        # return self.page.locator("//form[@action='/signup']//p[text() = 'Email Address already exist!']")

    @property
    def delete_account_link(self) -> Locator:
        return self.page.get_by_text(" Delete Account")


    @property
    def account_deleted_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Account Deleted!")


    @property
    def continue_button_in_deleted_account_page(self) -> Locator:
        return self.page.locator("//a[@data-qa='continue-button']")
    











    # Actions


    def click_new_user_sign_up_link(self) -> None:
        #self.logger.info("Clicking new user signup link: %s", self.new_user_sign_up_link)
        self.click(self.new_user_sign_up_link, "'Signup' link")


    def fill_new_user_signup_form(self, registered_user: dict) -> None:
        self.logger.info("Filling new user signup form")
        self.fill(self.name_field, "'Name' field", registered_user["name"])
        self.fill(self.email_address_field, "'Email address' field", registered_user["email"])


    def fill_new_user_signup_form_with_ivalid_email_format(self, test_data: dict) -> None:
        self.logger.info("Filling new user signup form with ivalid email format") 
        self.fill(self.name_field, "'Name' field", test_data["name"])
        self.fill(self.email_address_field, "'Email address' field", test_data["invalid_email"])
        

    def click_new_user_sign_up_button(self) -> None:
        #self.logger.info("Clicking new user Signup button: %s", self.signup_button)
        self.click(self.signup_button, "'Signup' button")

 
    def open_signup_form(self, test_data: dict) -> None: 
        self.logger.info("Filling new user signup form") 
        self.fill_new_user_signup_form(test_data)
        self.click_new_user_sign_up_button()


    def enter_account_info(self, test_data: dict) -> None:  # test_data is a fixture which is in conftest.py file
        self.logger.info("Entering account info") 
        self.radio_button_Mrs.check()
        self.fill(self.password_field_signup_page, "'Password' field", PASSWORD) 
        self.select_day_of_birth.select_option(test_data["day_of_birth"]) 
        self.select_month_of_birth.select_option(test_data["month_of_birth"])
        self.select_year_of_birth.select_option(test_data["year_of_birth"])


    def check_signup_for_newsletter_checkbox(self) -> None:
        self.logger.info("Clicking new user Signup button")
        self.checkbox_sign_up_for_our_newsletter.check()


    def enter_address_info(self, test_data: dict) -> None:
        self.logger.info("Entering address info") 
        self.fill(self.first_name_field, "'First name' field", test_data["first_name"])
        self.fill(self.last_name_field, "'Last name' field", test_data["last_name"])
        self.fill(self.company_field, "'Company' field", test_data["company"])
        self.fill(self.address_field, "'Address' field", test_data["address"])
        self.select_country.select_option(test_data["country"])
        self.fill(self.state_field, "'State' field", test_data["state"])
        self.fill(self.city_field, "'City' field", test_data["city"])
        self.fill(self.zipcode_field, "'Zip code' field", test_data["zip_code"])
        self.fill(self.mobile_number_field, "'Mobile number' field", test_data["mobile_number"]) 

 
    def click_create_account_button(self) -> None:
        #self.logger.info("Clicking 'Create account' button: %s", self.create_account_button)
        self.click(self.create_account_button, "'Create account' field")


    def click_continue_button(self) -> None:
        #self.logger.info("Clicking 'Continue' button: %s", self.continue_button)
        self.click(self.continue_button, "'Continue' button")


    def click_delete_account_link(self) -> None:
        #self.logger.info("Clicking 'Delete account' button: %s", self.delete_account_link)
        self.click(self.delete_account_link, "'Delete account' link")


    def click_continue_button_on_deleted_account_page(self) -> None:
        #self.logger.info("Clicking 'Continue' button on deleted account page: %s", self.continue_button_in_deleted_account_page)
        self.click(self.continue_button_in_deleted_account_page, "'Continue' button")



   
