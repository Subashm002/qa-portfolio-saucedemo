import pytest
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    browser = os.environ.get("BROWSER", "edge")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Edge(
            service=EdgeService("drivers/msedgedriver.exe"),
            options=options
        )
    
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

