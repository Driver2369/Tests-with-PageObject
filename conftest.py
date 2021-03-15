import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=" + browser_language)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()