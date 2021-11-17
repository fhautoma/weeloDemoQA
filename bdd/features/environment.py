from behave import use_fixture
from bdd.fixtures.fixtures import use_chrome_browser, use_browser_stack, close_browser


def before_tag(context, tag):
    if 'use.chrome.browser' in tag:
        use_fixture(use_chrome_browser, context)
    if tag.endswith('.browserstack'):
        context.browserstack_desired_capabilities_tag = tag
        use_fixture(use_browser_stack, context)


def after_scenario(context, scenario):
    use_fixture(close_browser, context)
