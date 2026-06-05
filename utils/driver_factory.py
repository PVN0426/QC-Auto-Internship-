from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:
    @staticmethod
    def get_chrome_driver():
        chrome_options = Options()
        
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=SafeBrowsing")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        return driver
