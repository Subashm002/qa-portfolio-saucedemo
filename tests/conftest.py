import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture(scope="function")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Edge(
        service=Service("drivers/msedgedriver.exe"),
        options=options
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()