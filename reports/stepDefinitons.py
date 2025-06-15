from behave import *
from reports.testcase1 import LoginTest
from reports.selenium_functions import SeleniumCommands
import time, json


@given("the login page is open")
def login_page(context):
    context.app = LoginTest()
    context.app.login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when("user enter username and password")
def credentials(context):
    context.app.credentials("Admin", "admin123")
    print("user entered credentials")

@when("user clicks on login button")
def submits(context):
    context.app.click("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    print("clicked on login button")

@then("homepage should be opened and user verifies title")
def title_capture(context):
    expected_title = "OrangeHRM"
    actual_title = context.app.title()
    assert expected_title in actual_title, "Title mismatch"
    print("title is captured", context.app.title())

@then("takes screenshot")
def screenshot(context):
    screenshot_folder = "screenshots"
    context.app.screenshot("title.png", screenshot_folder)
    print("user takes screenshot successfully")

@given("the Orangehrm page is open")
def page_opened(context):
    context.app = LoginTest()
    context.app.login_page("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then("I wait for username and password locators to be present")
def element_should_present(context):
    element_username = context.app.element_present('NAME', 'username')
    element_password = context.app.element_present('NAME', 'password')
    assert element_username is not None, "username not found"
    print(f"element is {element_username}")
    assert element_password is not None, "password not found"
    print(f"element is {element_password}")

@then("user open another website")
def open_other_url(context):
    context.app = LoginTest()
    context.app.login_page("https://testautomationpractice.blogspot.com/")

@then("user selects male option")
def radio_button(context):
    context.app.selection("CLASS_NAME", "form-check-label" )

@then("user verifies element visibility, text presence and radio buttons selection")
def visibility_textPresence_selected(context):
    assert context.app.element_present("ID", "phone"), "visibility not reported"
    assert context.app.text_present("XPATH", '//*[@id="alertBtn"]', 'Simple Alert'), "text not reported"
    assert context.app.element_selected("ID", "male"), "radio button didn't selected"

@then("User closes the browser")
def close(context):
    context.app.driver_quit()

@when("user opens login page")
def logindemo_page(context):
    context.app = LoginTest()
    context.app.login_page("https://www.saucedemo.com/")

@when('user enters "{username}" and "{password}"')
def credentials_swaglabs(context, username, password):
    context.app.credentials_swaglabs(username, password)

@when("user clicks on submit button")
def submit_button(context):
    context.app.click('//*[@id="login-button"]')

@then("Homepage opens and title gets verified")
def title_verification(context):
    expected_title = "Swag Labs"
    actual_title = context.app.title()
    assert expected_title in actual_title, "title mismatch"

@then("screenshot taken")
def screenshot_swaglabs(context):
    screenshot_folder = "screenshots"
    context.app.screenshot("swaglabs.png", screenshot_folder)

@given("the form is open")
def qa_form(context):
    context.app = LoginTest()
    context.app.login_page("https://demoqa.com/automation-practice-form")

@then('user enter {firstname} and {lastname} and {mobile} and {email}')
def details(context, firstname, lastname, mobile, email):
    context.firstname = firstname
    context.lastname = lastname
    context.app.details_qa_form(firstname, lastname, mobile, email)

@then("user selects gender")
def gender(context):
    context.app.click('//*[@id="genterWrapper"]/div[2]/div[1]/label')

@then("user submits the page and close the browser")
def submit(context):
    context.app.click('//*[@id="submit"]')
    time.sleep(3)
    screenshot_folder = "screenshots"
    filename = f"{context.firstname}_{context.lastname}.png"
    context.app.screenshot(filename, screenshot_folder)
    context.app.driver_quit()

@given("the user submits following details")
def json_details(context):
    user_data = json.loads(context.text)
    context.user_data = user_data
    print(user_data)

@then("user process the data")
def json_more_data(context):
    data = context.user_data
    name = data["name"]
    age = data["age"]
    email = data["email"]
    print(f"name is {name}, age is {age}, email is {email}")

@given("user opens automation demo page")
def automation_page(context):
    context.auto_app = SeleniumCommands()
    context.auto_app.url_open("https://testautomationpractice.blogspot.com/")

@then("user selects all checkboxes and quit")
def select_checkboxes(context):
    sunday = context.auto_app.checkbox_selection("ID", "sunday")
    monday = context.auto_app.checkbox_selection("ID", "monday")
    if sunday.is_selected() and monday.is_selected():
        print("both checkboxes are selected")
    else:
        print("selection didn't happen")
    context.auto_app.browser_quit()

@then("user clicks dropdown and selects country using Select command")
def dropdown(context):
    context.auto_app.dropdown_selection("ID", "country", text = "India")
    context.auto_app.dropdown_selection("XPATH", '//*[@id="country"]', ivalue = "canada" )
    context.auto_app.dropdown_selection("ID", "country", index = 4)

@then("user quits the browser")
def quit_browser(context):
    context.auto_app.browser_quit()


@then("user selects the date")
def date_picker(context):
    context.auto_app.click('//*[@id="datepicker"]')
    selected_date = context.auto_app.date_picker("XPATH", "//span[@class='ui-datepicker-month']",
                                                 "XPATH", "//span[@class='ui-datepicker-year']",
                                                 "//*[@id='ui-datepicker-div']/div/a[2]/span",
                                                 "//table[@class='ui-datepicker-calendar']//a",
                                                 "June","2026", "3")
    print("✅ Selected date is:", selected_date)
    assert selected_date != "", "❌ Date was not populated in the input field!"
    time.sleep(3)

@then("user opts date")
def date_picker_dropdown(context):
    context.auto_app.click('//*[@id="txtDate"]')
    context.auto_app.date_picker_dropdown("XPATH", "//*[@id='ui-datepicker-div']/div/div/select[1]", "XPATH", "//*[@id='ui-datepicker-div']/div/div/select[2]",
                                          "//table[@class='ui-datepicker-calendar']//tr/td/a", "25", "Jun", "2026")
    time.sleep(5)

@then("user selects datepicker range")
def date_picker_range(context):
    context.auto_app.range_datepicker()

@given("new qa form is opened")
def new_qa_page_open(context):
    context.auto_app = SeleniumCommands()
    context.auto_app.url_open("https://demoqa.com/")

@then("user selects checkboxes")
def user_selects_checkboxes(context):
    """context.auto_app.click('//*[@id="app"]/div/div/div[2]/div/div[1]/div')
    context.auto_app.click('//*[@id="item-1"]')
    context.auto_app.click('//*[@id="tree-node"]/ol/li/span/button')
    context.auto_app.click('//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
    context.auto_app.click('//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]')
    time.sleep(5)"""

@then("user performs operations on buttons")
def user_performs_operations_buttons(context):
    """context.auto_app.get_back()
    context.auto_app.click('//*[@id="item-4"]/span')
    context.auto_app.operations_buttons('//*[@id="doubleClickBtn"]', '//*[@id="rightClickBtn"]')
    time.sleep(5)"""

@then("user download a file and save it his preferred location")
def file_download_and_save(context):
    context.auto_app.download_files('https://www.sample-videos.com/download-sample-doc-file.php', '/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a')
    time.sleep(5)

@then("user upload a file")
def upload_file(context):
    context.auto_app.upload_file('https://demoqa.com/upload-download', '//*[@id="uploadFile"]')
    time.sleep(5)

@then("user also upload multiple files")
def upload_files(context):
    files = [
        r"C:\Users\kkira\OneDrive\Pictures\zoJV9ow-supercars-hd-wallpapers.jpg",
        r"C:\Users\kkira\OneDrive\Desktop\Family\PRADEEP\Budget Preparation - 2023-24 Andhra  pradeep.xlsx",
        r"C:\Users\kkira\OneDrive\Desktop\Family\PRADEEP\PRADEEP\Srinivasa electronics and home appliances- April CD WORKING.pdf.xlsx"
    ]
    context.auto_app.upload_multiple_files('https://testautomationpractice.blogspot.com/','//*[@id="multipleFilesInput"]', files)
    time.sleep(5)

@then("user plays with dynamic buttons")
def dynamic_buttons(context):
    context.auto_app = SeleniumCommands()
    context.auto_app.dynamic_buttons('//*[@id="HTML5"]/div[1]/button')
    time.sleep(5)

@then("user plays with alerts")
def alerts(context):
    context.auto_app.get_url("https://demoqa.com/alerts")
    # context.auto_app.alerts('//*[@id="alertButton"]')
    # context.auto_app.alerts_wait('//*[@id="timerAlertButton"]')
    #context.auto_app.alert_wait_text('//*[@id="confirmButton"]')
    context.auto_app.alert_enter_name('//*[@id="promtButton"]')
    time.sleep(5)

@then("user plays with frame")
def frames(context):
    """context.auto_app = SeleniumCommands()
    context.auto_app.get_url("https://demo.automationtesting.in/Frames.html")
    context.auto_app.frames('/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a',
                                    'singleframe',  '/html/body/section/div/div/div/input')
    """

@then("user plays with nested frames")
def nested_frames(context):
    """context.auto_app.get_url("https://demo.automationtesting.in/Frames.html")
    context.auto_app.nested_frames()"""

@then('user plays with slider')
def slider(context):
    """context.auto_app.get_url('https://demoqa.com/slider')
    location = context.auto_app.slider()
    print(location)"""

@then('user plays with scroll button')
def scrolling(context):
    context.auto_app = SeleniumCommands()
    """context.auto_app.get_url("https://flagpedia.net/index")
    #context.auto_app.scroll_approach_1()
    context.auto_app.scroll_approach_2()
    context.auto_app.scroll_approach_3()
    context.auto_app.scroll_approach_4()
    time.sleep(5)"""

@then("user plays with progress bar")
def progress_bar(context):
   """ context.auto_app.get_url('https://demoqa.com/progress-bar')
    context.auto_app.progress_bar("75")"""

@then("user plays with drag and drop")
def drag_and_drop(context):
    context.auto_app = SeleniumCommands()
    """context.auto_app.get_url("https://demoqa.com/droppable")
    context.auto_app.drag_and_drop()
    context.auto_app.click('//*[@id="droppableExample-tab-accept"]')"""

@then("user plays with revert")
def revert_drag_and_drop(context):
    """context.auto_app.get_url('https://demoqa.com/droppable')
    context.auto_app.click('//*[@id="droppableExample-tab-revertable"]')
    context.auto_app.drag_and_drop_revert()"""

@then("user plays with selectable")
def selectable(context):
    """context.auto_app.get_url('https://demoqa.com/selectable')
    context.auto_app.click('//*[@id="demo-tab-list"]')
    context.auto_app.selectable()
    time.sleep(10)"""

@then("user plays resizable")
def resizable(context):
    #context.auto_app.get_url("https://demoqa.com/resizable")
    #context.auto_app.resizable()
    #context.auto_app.resize_box()
    #context.auto_app.get_url("https://demoqa.com/sortable")
    #context.auto_app.click('//*[@id="demo-tabpane-list"]/div/div[6]')
    #context.auto_app.click('//*[@id="demo-tab-grid"]')
    #context.auto_app.get_url("https://demoqa.com/auto-complete")
    #context.auto_app.sortable_list()
    #context.auto_app.auto_complete()
    context.auto_app.get_url("https://demoqa.com/select-menu")
    context.auto_app.select_multiple_options()
    time.sleep(5)

@then('user plays with tables')
def tables(context):
    context.auto_app = SeleniumCommands()
    context.auto_app.get_url("https://testautomationpractice.blogspot.com/")
    #context.auto_app.tables()
    context.auto_app.dynamic_tables()

@then('user plays with broken links')
def broken_links(context):
    context.auto_app = SeleniumCommands()
    context.auto_app.broken_links()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filename = os.path.join(os.getcwd(), "image_{timestamp}.png"}

driver.save_screenshot(filename)





