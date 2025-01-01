from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    

class MainPage(BasePage):

    # TC01_part1 - Register user
    def is_user_registered(self):
        creation_confirmed = self.driver.find_element(By.XPATH, '//span[contains(text(),"English")]').text # modify
        return "ACCOUNT CREATED!" in creation_confirmed
    
    # TC01_part2 - Delete user
    def is_user_deleted(self):
        deleted_confirmed = self.driver.find_element(By.XPATH, '//span[contains(text(),"English")]').text # modify
        return "ACCOUNT DELETED!" in deleted_confirmed