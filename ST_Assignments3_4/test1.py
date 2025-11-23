import os
from selenium import webdriver
from browsers import get_caps

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

if not USERNAME or not ACCESS_KEY:
    raise Exception("BrowserStack credentials not found in environment variables!")

def run_test(browser):

    caps = get_caps(browser, USERNAME, ACCESS_KEY, f"Test1 - {browser}")

    if browser == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
    else:
        raise Exception("Unknown browser!")

    options.set_capability('bstack:options', caps["bstack:options"])
    options.set_capability('browserName', caps["browserName"])
    options.set_capability('browserVersion', caps["browserVersion"])

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://www.example.com")
    print(browser, "Title:", driver.title)
    driver.quit()


if __name__ == "__main__":
    run_test("Chrome")
    run_test("Firefox")
    run_test("Edge")
