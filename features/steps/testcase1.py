from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class LoginTest:
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options = chrome_options)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 10)
        chrome_options.add_argument("--disable-notifications")

    def login_page(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def credentials(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click(self,button_xpath):
        wait = WebDriverWait(self.driver, 10)
        element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        element_to_click.click()

    def title(self):
        return self.driver.title

    def screenshot(self, filename, path):
        time.sleep(5)
        if path:
            os.makedirs(path, exist_ok =True)
            full_path = os.path.join(path, filename)
        self.driver.save_screenshot(full_path)

    def element_present(self,locator,value):
        by_locator = getattr(By, locator)
        value = str(value)
        return self.wait.until(EC.presence_of_element_located((by_locator, value)))

    def element_visible(self,locator, value):
        by_locator = getattr(By, locator)
        value = str(value)
        return self.wait.until(EC.visibility_of_element_located((by_locator, value)))

    def text_present(self,locator, value, expected_text):
        by_locator = getattr(By, locator)
        value = str(value)
        return self.wait.until(EC.text_to_be_present_in_element((by_locator, value), expected_text))

    def element_selected(self,locator, value):
        by_locator = getattr(By, locator)
        value = str(value)
        element = self.wait.until(EC.presence_of_element_located((by_locator, value)))
        return element.is_selected()

    def selection(self, locator, value):
        by_locator = getattr(By, locator)
        value =str(value)
        self.driver.find_element(by_locator, value).click()

    def driver_quit(self):
        self.driver.quit()


    def credentials_swaglabs(self,username, password):
        self.driver.find_element(By.NAME, "user-name").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)