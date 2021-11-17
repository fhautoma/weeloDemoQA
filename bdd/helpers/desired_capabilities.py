from bdd.config import global_configuration as gc


def get_desired_capability(context):
    if 'use.Windows.10.Chrome.95.browserstack' == context.browserstack_desired_capabilities_tag:
        return {
            "os": "Windows",
            "os_version": "10",
            "browser": "Chrome",
            "browser_version": "95.0",
            "browserstack.local": "false",
            "browserstack.selenium_version": f"{gc.SELENIUM_VERSION}",
            'name': "Test",
            'browserstack.networkLogs': True,
            'build': gc.BROWSERSTACK_BUILD_ID
        }

