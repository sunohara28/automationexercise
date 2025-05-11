import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="Chrome", help="my option: Chrome, Firefox, Edge")
    parser.addoption("--headless", action="store", default="Yes", help="my option: Yes, No")

@pytest.fixture(scope="class")
def Setup_driver(request):

    global driver
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")


    url = "https://www.automationexercise.com/"

    if headless == 'Yes':
        driver = webdriver.Chrome(options=options)
    elif headless == 'No':
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
