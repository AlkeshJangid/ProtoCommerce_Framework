import pytest
from selenium import webdriver
from utilities.Logger import GenerateLogs

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        print("Opening in Chrome Mode")
        GenerateLogs.LogGen().info("Opening in Chrome Mode")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Opening in Firefox Mode")
        GenerateLogs.LogGen().info("Opening in Firefox Mode")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Opening in Edge Mode")
        GenerateLogs.LogGen().info("Opening in Edge Mode")
        driver = webdriver.Edge()
    else:
        print('Headless Mode On')
        GenerateLogs.LogGen().info('Headless Mode On')
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)
    # yield
    # driver.close()
    return driver



