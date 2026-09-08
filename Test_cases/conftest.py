import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys, os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        options = Options()
        options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from selenium.webdriver.edge.options import Options as EdgeOptions
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "OpenCart Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name : OpenCart Test Report",
        "Module Name : Login Module",
        "Tester Name : Yash Mahadik"
    ])

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\Report\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"
