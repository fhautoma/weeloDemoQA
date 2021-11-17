from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bdd.helpers.desired_capabilities import get_desired_capability
import bdd.config.global_configuration as gc


def use_chrome_browser(context, **kwargs):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()


def use_browser_stack(context, **kwargs):
    assert hasattr(context, 'browserstack_desired_capabilities_tag'), \
        'context.browserstack_desired_capabilities_tag is not defined'

    context.browserstack_desired_capabilities = get_desired_capability(context)
    context.browser = webdriver.Remote(
        command_executor=gc.BROWSERSTACK_EXECUTION_BASE_URL,
        desired_capabilities=context.browserstack_desired_capabilities,
    )
    if 'device' not in context.browserstack_desired_capabilities:
        context.browser.maximize_window()
    context.browserstackSessionId = context.browser.session_id


def close_browser(context):
    context.browser.quit()
