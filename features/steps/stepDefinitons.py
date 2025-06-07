from behave import *
from features.steps.testcase1 import LoginTest
import time


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




