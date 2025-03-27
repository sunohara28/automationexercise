import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="Chrome", help="my option: Chrome, Firefox, Edge")

@pytest.fixture(scope="class")
def Setup_driver(request):

    global driver
    url = "https://www.automationexercise.com/"
    browser = request.config.getoption("--browser")

    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Edge':
        driver = webdriver.Edge()

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
