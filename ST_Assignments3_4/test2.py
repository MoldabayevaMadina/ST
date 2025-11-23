import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from browsers import get_caps

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

if not USERNAME or not ACCESS_KEY:
    raise Exception("BrowserStack credentials not found.")

def run_test(browser):
    caps = get_caps(browser, USERNAME, ACCESS_KEY, f"Test2 - {browser}")

    if browser == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
    else:
        options = webdriver.EdgeOptions()

    options.set_capability('bstack:options', caps["bstack:options"])
    options.set_capability('browserName', browser)
    options.set_capability('browserVersion', "latest")

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://www.wikipedia.org")

    russian = driver.find_element(By.ID, "js-link-box-ru")

    russian.click()

    print(browser, "Russian Wikipedia title:", driver.title)

    assert "Википедия" in driver.title, "Ошибка — переход на русскую Википедию не выполнен!"

    driver.quit()

if __name__ == "__main__":
    run_test("Chrome")
    run_test("Firefox")
    run_test("Edge")
