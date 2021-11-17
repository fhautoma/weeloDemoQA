from behave import Given, When, Then
from bdd.pages.student_form_page.automation_practice_form import StudentRegistrationFormPage


@Given('a browser is used to load the URL "{url}"')
def step_def(context, url):
    context.current_page = StudentRegistrationFormPage(context)
    context.current_page.open_url(url)


@When('I fill student registration form')
def step_def(context):
    context.current_page.fill_student_from_fields()


@When('I click submit button')
def step_def(context):
    context.current_page.click_in_submit_button()


@Then('I see a table with new student information')
def step_def(context):
    context.current_page.validate_if_data_table_is_visible()
    expected = False
    assert(context.current_page.validate_if_data_table_is_visible() == expected, "No data table visible")
