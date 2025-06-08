from  selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, os

class SeleniumCommands():
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def url_open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()

    def screenshot(self, filename, path):
        time.sleep(5)
        if path:
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)
        self.driver.save_screenshot(full_path)

    def checkbox_selection(self, locator, value):
        locator = getattr(By, locator)
        value = str(value)
        button = self.driver.find_element(locator, value)
        button.click()
        time.sleep(3)
        return button

    def dropdown_selection(self, locator, value, **kwargs):
        locator = getattr(By, locator)
        value = str(value)
        element =   self.driver.find_element(locator, value)
        self.wait.until(EC.presence_of_element_located((locator, value)))
        select = Select(element)

        if "text" in kwargs:
            select.select_by_visible_text(kwargs["text"])
        elif "index" in kwargs:
            select.select_by_index(int(kwargs["index"]))
        elif "ivalue" in kwargs:
            select.select_by_value(kwargs["ivalue"])
        else:
            raise ValueError("text or index or value is not given")
        time.sleep(3)

    def click(self,button_xpath):
        wait = WebDriverWait(self.driver, 10)
        element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to_click)
        time.sleep(0.5)
        element_to_click.click()

    def switch_to_single_frame(self):
        self.driver.switch_to.frame(0)

    def date_picker(self, month_locator,
                    month_value, year_locator, year_value, next_arrow_xpath, date_table_xpath,
                    exp_month, exp_year, exp_date):
        self.driver.implicitly_wait(5)
        month_locator = getattr(By, month_locator)
        year_locator = getattr(By, year_locator)

        while True:
            month = self.driver.find_element(month_locator, month_value).text
            year = self.driver.find_element(year_locator, year_value).text
            if month == exp_month and year == exp_year:
                break
            else:
                self.driver.find_element(By.XPATH, next_arrow_xpath).click()

        dates = self.driver.find_elements(By.XPATH, date_table_xpath)
        for date in dates:
            if date.text == exp_date:
                date.click()
                break

        date_input_value = self.driver.find_element(By.ID, "datepicker").get_attribute("value")
        print("DEBUG: Selected value in input field:", date_input_value)
        return date_input_value

    def date_picker_dropdown(self, month_locator, month_value, year_locator, year_value, date_xpath,
                             exp_date, exp_month, exp_year):
        month_by_locator= getattr(By, month_locator)
        year_by_locator = getattr(By, year_locator)
        month = self.driver.find_element(month_by_locator, month_value)
        year = self.driver.find_element(year_by_locator, year_value)
        month = Select(month)
        year = Select(year)
        month.select_by_visible_text(exp_month)
        year.select_by_visible_text(exp_year)
        all_dates = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, date_xpath)))

        for date in all_dates:
            if date.text == exp_date:
                date.click()
                break

    def range_datepicker(self):
        self.driver.find_element(By.XPATH, "//*[@id='start-date']").click()
        time.sleep(5)

    def operations_buttons(self, double_xpath, right_xpath):
        self.driver.implicitly_wait(5)
        action = ActionChains(self.driver)

        #double_click
        double_button = self. driver.find_element(By.XPATH, double_xpath)
        action.double_click(double_button).perform()

        #right_click
        right_button = self.driver.find_element(By.XPATH, right_xpath)
        action.context_click(right_button).perform()


    def get_url(self,url):
        self.driver.get(url)

    def get_back(self):
        self.driver.back()

    def download_files(self, url, file_xpath):
        location = os.getcwd()
        preferences = {"download.default_directory":location}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs", preferences)
        self.driver.get(url)
        self.driver.maximize_window()
        download_file = self.driver.find_element(By.XPATH, file_xpath)
        download_file.click()









