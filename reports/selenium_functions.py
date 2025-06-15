from  selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, os, requests

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
        self.driver.maximize_window()

    def get_back(self):
        self.driver.back()

    def download_files(self, url, file_xpath):
        # ✅ Preferred download directory
        # location = r"C:\Users\kkira\Downloads\MyTestDownloads"
        # os.makedirs(location, exist_ok=True)
        location = os.getcwd()
        preferences = {"download.default_directory":location}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome(options=ops)
        self.driver.get(url)
        self.driver.maximize_window()
        download_file = self.driver.find_element(By.XPATH, file_xpath)
        download_file.click()

    def upload_file(self,url, file_xpath, **kwargs):
        self.driver.get(url)
        upload_file = self.driver.find_element(By.XPATH, file_xpath)
        upload_file.send_keys(r"C:\Users\kkira\OneDrive\Pictures\zoJV9ow-supercars-hd-wallpapers.jpg")

    def upload_multiple_files(self, url, file_xpath, files):
        self.driver.get(url)
        upload_files_path = self.driver.find_element(By.XPATH, file_xpath)
        upload_files_path.send_keys("\n".join(files))
        self.driver.find_element(By.XPATH, '//*[@id="multipleFilesForm"]/button').click()

    def dynamic_buttons(self,xpath):
        self.driver.implicitly_wait(5)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        pre_click_btn = self.driver.find_element(By.XPATH, xpath)
        pre_click_btn.get_attribute("class")
        pre_click_btn.click()
        post_click_btn = self.driver.find_element(By.XPATH, xpath)
        post_click_btn.get_attribute("class")

    def alerts(self, xpath):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, xpath).click()
        alert_text = self.driver.switch_to.alert
        print(alert_text.text)

    def alerts_wait(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(5)
        alert_text = self.driver.switch_to.alert
        print(alert_text)

    def alert_wait_text(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        alert_text = self.driver.switch_to.alert
        print(alert_text)
        alert_text.accept()

    def alert_enter_name(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        alert_text = self.driver.switch_to.alert
        alert_text.send_keys("kiran")
        print(alert_text)
        time.sleep(5)
        alert_text.accept()

    def frames(self, frame_button, frame1_xpath, input):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, frame_button)
        frame_1 = self.driver.find_element(By.ID, frame1_xpath)
        self.driver.switch_to.frame(frame_1)
        self.driver.find_element(By.XPATH, input).send_keys("back again, great stay Hard")
        time.sleep(5)

    def nested_frames(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
        outer_frame = self.driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')  # we captured Outer frame button
        self.driver.switch_to.frame(outer_frame)  # we entered Outer frame

        inner_frame = self.driver.find_element(By.XPATH,
                                          '/html/body/section/div/div/iframe')  # we now captured inner frame button
        self.driver.switch_to.frame(inner_frame)
        self.driver.find_element(By.XPATH, '/html/body/section/div/div/div/input').send_keys("Great Keep going, you will win")
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        time.sleep(5)

    def slider(self):
        slider = self.driver.find_element(By.XPATH, '//*[@id="sliderContainer"]/div[1]/span/input')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(slider, 15, 100).perform()
        time.sleep(5)
        return slider.location

    def progress_bar(self, target_percent):
        self.driver.implicitly_wait(5)
        target_percent = int(target_percent)
        self.driver.find_element(By.ID, "startStopButton").click()
        while True:
            progress_bar_info = self.driver.find_element(By.XPATH, '//*[@id="progressBar"]/div')
            current_progress = progress_bar_info.get_attribute("aria-valuenow")
            current_progress= int(current_progress)
            if current_progress == target_percent:
                self.driver.find_element(By.ID, "startStopButton").click()
                time.sleep(5)
                break


    def scroll_approach_1(self):
        self.driver.execute_script("window.scroll(1000,45000)", "")
        value = self.driver.execute_script("return window.pageYOffset;")
        return value

    def scroll_approach_2(self):
        element_locator = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/ul[2]/li[104]')
        self.driver.execute_script("arguments[0].scrollIntoView()", element_locator)
        time.sleep(5)
        self.driver.execute_script("return window.pageYOffset;")

    def scroll_approach_3(self):
        self.driver.execute_script("window.scroll(0, document.body.scrollHeight)")

    def scroll_approach_4(self):
        self.driver.execute_script("window.scroll(0,-document.body.scrollHeight)")

    def drag_and_drop(self):
        draggable = self.driver.find_element(By.XPATH, '//*[@id="draggable"]')
        droppable = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable).perform()
        not_draggable = self.driver.find_element(By.XPATH, '//*[@id="notAcceptable"]')
        not_droppable = self.driver.find_element(By.XPATH)
        time.sleep(5)

    def drag_and_drop_revert(self):
        revert_draggable= self.driver.find_element(By.XPATH, '//*[@id="revertable"]')
        droppable = self.driver.find_element(By.XPATH, '//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.click_and_hold(revert_draggable).move_to_element(droppable).release().perform()
        time.sleep(5)

    def selectable(self):
        elements = ["Cras justo odio", "Dapibus ac facilisis in", "Morbi leo risus", "Porta ac consectetur ac"]
        self.driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="verticalListContainer"]/li[2]').click()
        #button = Select(button)



    def resize_box(self):
        # Locate the resize handle (bottom-right corner)
        handle = self.driver.find_element(By.CSS_SELECTOR, '#resizable .react-resizable-handle')

        # Scroll handle into view (optional but good practice)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", handle)

        # Create the ActionChains object
        action = ActionChains(self.driver)

        # Click, hold, move by offset, and release to resize
        action.click_and_hold(handle).move_by_offset(150, 100).release().perform()


    def sortable_list(self):
        two_button = self.driver.find_element(By.CSS_SELECTOR, '#demo-tabpane-list > div > div:nth-child(2)')
        six_button = self.driver.find_element(By.CSS_SELECTOR, '#demo-tabpane-list > div > div:nth-child(6)')
        self.driver.execute_script("arguments[0].scrollIntoView(true)", six_button)
        ActionChains(self.driver).click_and_hold(two_button).move_to_element(six_button).release().perform()
        time.sleep(5)

    def sortable_grid(self):
        five = self.driver.find_element(By.CSS_SELECTOR, '#demo-tabpane-grid > div > div > div:nth-child(1)')
        nine = self.driver.find_element(By.CSS_SELECTOR, '#demo-tabpane-grid > div > div > div:nth-child(9)')
        ActionChains(self.driver).click_and_hold(five).move_to_element(nine).release().perform()

    def auto_complete(self):
        #input = self.wait.until(EC.presence_of_element_located(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]'))
        input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="autoCompleteMultipleInput"]')))
        for color in ["Red", "yellow", "purple"]:
            input_box.send_keys(color)
            time.sleep(1)
            input_box.send_keys(Keys.ENTER)
            time.sleep(0.5)

    def window_handles(self):
        what_tab = self.driver.find_element(By.XPATH, '//*[@id="demo-tab-what"]')
        origin = self.driver.find_element(By.XPATH, '//*[@id="demo-tab-what"]')
        use = self.driver.find_element(By.XPATH, '//*[@id="demo-tab-use"]')
        windows = self.driver.window_handles

    def hover_actions(self):
        option = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
        sub_option = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
        sub_sub_option = self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')

        ActionChains(self.driver).move_to_element(option).move_to_element(sub_option).move_to_element(sub_sub_option).click().perform()
        time.sleep(5)

    def select_multiple_options(self):

        arrow = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[2]')))
        time.sleep(4)
        arrow.click()
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", arrow)
        time.sleep(5)
        input = self.driver.find_element(By.XPATH, '//*[@id="react-select-4-input"]')
        input.click()
        for color in ["Green", "Blue", "Black", "Red"]:
            option = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f'//div[contains(@class,"react-select__option") and text()="{color}"]')))
            option.click()
            time.sleep(0.5)
        time.sleep(5)

    def tables(self):
       rows = self.driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr')
       columns = self.driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr/th')
       assert len(rows) == 7 and len(columns) == 4, "incorrect values reported"
       time.sleep(1)
       specific_data = self.driver.find_element(By.XPATH, '//table[@name="BookTable"]//tr[2]/td[2]')
       print(specific_data)
       no_of_rows = len(rows)
       no_of_columns = len(columns)
       for row in range(2, no_of_rows+1):
           for column in range(1, no_of_columns+1):
            data = self.driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[" + str(column) + "]").text
            print(data)

       author_names = ["Amit", "Mukesh", "Animesh", "Mukesh", "Amod", "Amit"]
       for row in range(2, no_of_rows):
           for column in range(1, no_of_columns):
               data = self.driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+ str(row) +"]/td["+str(column)+"]").text
               if data in author_names:
                   bookName = self.driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td[1]").text
                   price = self.driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(row)+"]/td[4]").text
                   print(data, bookName, price, end="")

    def dynamic_tables(self):
        rows = self.driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr")
        columns = self.driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr/th")
        no_of_rows = len(rows)
        no_of_columns = len(columns)
        assert no_of_rows == 4 and no_of_columns == 5, "error error"
        print(no_of_rows, no_of_columns)

        headers = [header.text.strip() for header in self.driver.find_elements(By.XPATH, "//table[@id='taskTable']/thead/tr/th")]
        network = headers.index("Network (Mbps)")

        rows = self.driver.find_elements(By.XPATH, "//table[@id='taskTable']/tbody/tr")
        print("length of rows", len(rows))

        target_network = self.driver.find_element(By.XPATH, "//*[@id='displayValues']/p[3]/strong").text.strip()

        for i, row in enumerate(rows, start=1):
            cells = row.find_elements(By.TAG_NAME, "td")
            network_speed = cells[network].text.strip()
            print(f"Row {i} speed: {network_speed}")

            if network_speed == target_network:
                print(f"Match found at row {i}")

    def broken_links(self):
        url = "http://www.deadlinkcity.com/"
        self.driver.get(url)
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        count=0
        for link in links:
            url =link.get_attribute("href")
            url_response = requests.head(url)
            if url_response.status_code >= 400:
                print("its a broken link")
                count+=1
            else:
                print("its a valid link")
        print("count of broken links is:", count)

