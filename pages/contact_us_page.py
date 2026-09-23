from playwright.sync_api import Locator
from pages.base_page import BasePage



class ContactUs(BasePage):


    # LOCATORS

    @property
    def home_page_link_text(self) -> Locator:
        return self.page.get_by_role("link", name=" Home")

    @property
    def contact_us_link(self) -> Locator:
        return self.page.get_by_text(" Contact us")

    @property
    def get_in_touch_text(self) -> Locator:
        return self.page.get_by_role("heading", name="Get In Touch")

    @property
    def name_field(self) -> Locator:
        return self.page.get_by_placeholder("Name")

    @property
    def email_field(self) -> Locator:
        return self.page.locator('[data-qa="email"]')

    @property
    def subject_field(self) -> Locator:
        return self.page.get_by_placeholder("Subject")

    @property
    def message_field(self) -> Locator:
        return self.page.get_by_placeholder("Your Message Here")

    @property
    def upload_file_button(self) -> Locator:
        return self.page.locator('[name="upload_file"]')

    @property
    def submit_button(self) -> Locator:
        return self.page.locator('[data-qa="submit-button"]')


    @property
    def contact_us_success_message(self) -> Locator:
        return self.page.locator("//div[@class='contact-form']//div[text() = 'Success! Your details have been submitted successfully.']")


    @property
    def home_button(self) -> Locator:
        return self.page.locator("//div[@id='form-section']//span[text() = ' Home']")

   




    # ACTIONS

    def click_contact_us_link(self) -> None:
        # self.logger.info("Clicking element: %s", self.contact_us_link)
        # self.click(self.contact_us_link)
        self.click(self.contact_us_link, "'Contact Us' link")


    def fill_contact_us_form(self, test_data: dict) -> None:
        self.logger.info("Filling contact us form")
        self.fill(self.name_field, "'Name' field", test_data["name"])
        self.fill(self.email_field, "'Email' field", test_data["email"])
        self.fill(self.subject_field, "'Subject' field", test_data["subject"])
        self.fill(self.message_field, "'Message' field", test_data["message"])

    def upload_file_for_contact_us_form(self) -> None:
        self.logger.info("Uploading file for contact us form")
        self.upload_file(self.upload_file_button, "'Upload file' button", "test_data/test_file.txt")

    def click_submit_button(self) -> None:
        self.logger.info("Clicking submit button in contact us form")
        self.click(self.submit_button, "'Submit' button")

    def accept_dialog_popup(self) -> None:
        self.logger.info("Accepting dialog popup form in contact us page")
        self.page.on("dialog", lambda dialog: dialog.accept())

    def click_home_button(self) -> None:
        self.logger.info("Clicking home button")
        self.click(self.home_button, "'Home' button")





 