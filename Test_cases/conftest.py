import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                      help="Browser to run tests against: chrome | firefox | edge")
    parser.addoption("--headless", action="store_true", default=False,
                      help="Run the browser headless (required on CI agents with no display)")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser, request):
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        else:
            options.add_experimental_option("detach", True)
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    if not headless:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "OpenCart Test Report"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name : OpenCart Test Report",
        "Module Name : Login Module",
        "Tester Name : Yash Mahadik",
    ])


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not config.option.htmlpath:
        report_dir = os.path.join(PROJECT_ROOT, "Report")
        os.makedirs(report_dir, exist_ok=True)
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".html"
        config.option.htmlpath = os.path.join(report_dir, filename)
