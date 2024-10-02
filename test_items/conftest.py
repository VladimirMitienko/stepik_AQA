import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Выберите язык страницы")

@pytest.fixture(scope="class")
def locale(request):
    language = request.config.getoption('--language')
    return language

@pytest.fixture(scope="function")
def browser(request, locale):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': locale})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

