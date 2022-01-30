import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

def pytest_generate_tests(metafunc):
    if ("language") in metafunc.fixturenames:
        metafunc.parametrize("language", (metafunc.config.getoption("language"),))
    if ("email") in metafunc.fixturenames:
        with open('Data/payload.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            test_cases = ()
            for row in reader:
                test_cases = test_cases + (row["email"], )
        if not reader:
            raise ValueError("Test cases not loaded")
        metafunc.parametrize("email", test_cases)
