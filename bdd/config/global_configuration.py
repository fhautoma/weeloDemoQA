import os

MOCKAROO_URL = 'https://my.api.mockaroo.com/'
MOCKAROO_API_PATH = 'usermockdata.json'
MOCKAROO_API_KEY = 'cbb86130'

BROWSERSTACK_URL = 'https://felipehenao2:AEcZzcuK1nvH1QxSUnjR@hub-cloud.browserstack.com/wd/hub'
BROWSERSTACK_EXECUTION_BASE_URL = 'https://automate.browserstack.com/dashboard/v2/builds'
BROWSERSTACK_BUILD_ID = 'uTest'
BROWSER_STACK_REST_API_BUILDS_URL = 'https://api.browserstack.com/automate/builds.json'
BROWSER_STACK_REST_API_CREDENTIAL_USER = os.getenv('BROWSERSTACK_USERNAME')
BROWSER_STACK_REST_API_CREDENTIAL_PASSWORD = os.getenv('BROWSERSTACK_ACCESS_KEY')
SELENIUM_VERSION = '3.14.0'

#  Constants:
GLOBAL_TIMEOUT = 30
IMAGE_PATH = r"C:\Users\user\Desktop\student-plan-landing.png"
HOBBIES_LIST = ['Sports', 'Reading', 'Music']
