import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import page
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("Set up")
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")  # Deshabilita notificaciones emergentes
        chrome_options.add_argument("--no-default-browser-check")  # Evita la ventana emergente de seleccionar buscador
        chrome_options.add_argument("--no-first-run")  # Evita ventanas emergentes de la primera vez
        chrome_options.add_argument("--disable-popup-blocking") 
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chromedriver_path = f"C:/Program Files (x86)/chromedriver.exe"
        self.driver = webdriver.Chrome(service = Service(chromedriver_path), options = chrome_options)
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    # TC01_part1 - Register user
    def test_is_user_registered(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        # steps
        # //*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/text()
        assert mainPage.is_user_registered()
    
    # TC01_part2 - Delete user
    def test_is_user_deleted(self):
        mainPage = page.MainPage(self.driver)
        time.sleep(5)
        # steps
        assert mainPage.is_user_deleted()

if __name__ == "__main__":
    unittest.main()