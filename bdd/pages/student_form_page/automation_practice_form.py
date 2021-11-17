import random
from bdd.helpers.mockaroo_api_call import get_user_form_data_from_api
from bdd.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from bdd.config.global_configuration import MOCKAROO_URL, MOCKAROO_API_PATH, MOCKAROO_API_KEY, GLOBAL_TIMEOUT, \
    IMAGE_PATH, HOBBIES_LIST
from bdd.config.global_configuration import GLOBAL_TIMEOUT
from selenium.webdriver.common.keys import Keys


class StudentRegistrationFormPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, 'firstName')
    LAST_NAME_FIELD = (By.ID, 'lastName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    MOBILE_PHONE_FIELD = (By.ID, 'userNumber')
    BIRTH_FIELD = (By.ID, 'dateOfBirthInput')
    SUBJECTS_FIELD = (By.ID, 'subjectsInput')
    UPLOAD_PICTURE_BUTTON = (By.ID, 'uploadPicture')
    CURRENT_ADDRESS_FIELD = (By.ID, 'currentAddress')
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='submit']")

    def __init__(self, context):
        BasePage.__init__(self, context=context)

    def open_url(self, url):
        self.context.browser.get(url)

    def wait_until_page_load(self):
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT).until(ec.visibility_of_element_located(self.FIRST_NAME_FIELD))

    def fill_student_from_fields(self):

        data = get_user_form_data_from_api(f"{MOCKAROO_URL}{MOCKAROO_API_PATH}?key={MOCKAROO_API_KEY}")
        if data:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            birthdate = data['birthdate']
            phone_number = data['phone_number']
            gender = data['gender']
            address = data['address']
        else:
            first_name = 'Andres'
            last_name = 'Henao'
            email = 'fhautomata@gmal.com'
            birthdate = '11/26/1993'
            phone_number = '1252987414'
            gender = 'Male'
            address = 'Test Street 123'

        # Fill first name
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)

        # Fill last name
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.LAST_NAME_FIELD)).send_keys(last_name)

        # Fill email
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.EMAIL_FIELD)).send_keys(email)

        # Click gender radio
        radio_gender = self.context.browser.\
            find_elements_by_xpath("//*[@class='custom-control custom-radio custom-control-inline']")

        for i in range(len(radio_gender)-1):
            if radio_gender[i].text == gender:
                radio_gender[i].click()

        # Fill phone number
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.MOBILE_PHONE_FIELD)).send_keys(phone_number)

        # Select Hobby
        check_box_hobby = self.context.browser. \
            find_elements_by_xpath("//*[@class='custom-control custom-checkbox custom-control-inline']")
        for i in range(len(check_box_hobby)-1):
            if check_box_hobby[i].text == random.choice(HOBBIES_LIST):
                check_box_hobby[i].click()

        # Fill birthdate
        birthdate_element = self.context.browser.find_element_by_id('dateOfBirthInput')
        birthdate_element.click()
        self.context.browser.execute_script("document.getElementById('dateOfBirthInput').value = '';")
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.BIRTH_FIELD)).send_keys(birthdate)

        # Subjects submits
        subjects_element = self.context.browser.find_element_by_id('subjectsInput')
        subjects_element.send_keys('Computer Science')
        subjects_element.send_keys(Keys.ENTER)

        # Upload Image
        self.context.browser.find_element_by_id("uploadPicture").send_keys(IMAGE_PATH)

        # Fill address
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT). \
            until(ec.presence_of_element_located(self.CURRENT_ADDRESS_FIELD)).send_keys(address)

    def click_in_submit_button(self):
        self.context.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        WebDriverWait(self.context.browser, GLOBAL_TIMEOUT).until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
