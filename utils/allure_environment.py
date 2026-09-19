import platform
import sys
import os
import importlib.metadata


def create_environment_file(browser):
    os.makedirs("allure-results", exist_ok=True)

    with open("allure-results/environment.properties", "w") as file:
        file.write(f"Python={sys.version.split()[0]}\n")
        file.write(f"OS={platform.system()}\n")
        file.write(f"OS Version={platform.release()}\n")
        file.write(f"Playwright={importlib.metadata.version('playwright')}\n")
        #file.write("Browser=Chromium\n")
        file.write(f"Browser={browser.browser_type.name.capitalize()}\n")
        file.write(f"Environment={os.getenv('ENVIRONMENT')}\n")






