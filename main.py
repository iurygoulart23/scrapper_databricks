from myFunctions.navegador import navegador_firefox
import ssl
from selenium import webdriver

class Scrapper:
	
    def __init__(self, url, headless=False):
	
        ssl._create_default_https_context = ssl._create_unverified_context
	
        self.headless = headless
        self.url = url
        self.firefox_options = webdriver.FirefoxOptions()
        if self.headless:
            self.firefox_options.add_argument("--headless")
        self.firefox_options.add_argument("--no-sandbox")
        self.firefox_options.add_argument("--disable-dev-shm-usage")
        self.firefox_options.add_argument("--disable-gpu")

        firefox_binary_path = '/usr/bin/firefox'

        self.firefox_options.binary_location = firefox_binary_path

        # Configure preferences for downloads
        download_directory = "./download/"
        self.firefox_options.set_preference("browser.download.folderList", 2)  # Use the custom download directory
        self.firefox_options.set_preference("browser.download.dir", download_directory)
        self.firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")


        self.driver = navegador_firefox(headless=self.headless, firefox_options=self.firefox_options)


if __name__ == "__main__":

    link = "https://www.google.com"

    driver = Scrapper(link, headless=True)

