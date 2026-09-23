from playwright.sync_api import Page, Locator
from utils.config import BASE_URL
from utils.logger import get_logger



class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
    


    def open_base_url(self):
        self.logger.info("Navigating to base url: %s", BASE_URL)
        self.page.goto(BASE_URL)
        

    def click(self, locator: Locator, element_name: str):
        self.logger.info("Clicking element: %s", element_name)
        locator.click()


    def hover(self, locator: Locator, element_name: str):
        self.logger.info("Hovering over the element: %s", element_name)
        locator.hover()

      
    def fill(self, locator: Locator, element_name: str, text: str):
        self.logger.info("Filling a field: %s", element_name)
        locator.fill(text)


    def scroll(self, locator: Locator, element_name: str):
        self.logger.info("Scrolling the page: %s", element_name)
        locator.scroll_into_view_if_needed()


    def upload_file(self, locator: Locator, element_name: str, file_path: str):
        self.logger.info("Uploading the file: %s", element_name)
        locator.set_input_files(file_path)


