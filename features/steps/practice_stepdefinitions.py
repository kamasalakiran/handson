from behave import *


@given("the login page is opened")
def given_given(context):
    context.kiran = "kiran kumar kamasala"
    pass

@given('the one uses "{username}" and "{password}"')
def login(context, username, password):
    kiran = context.kiran
    print(username, password, kiran)

@then('the two and "{age}"')
def age(context,age):
    print(age)
    pass

@then("habibi")
def habibi(context):
    pass
