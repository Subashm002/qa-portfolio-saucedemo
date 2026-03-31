import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout:

    def setup_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

    def test_checkout_with_valid_details(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.ID, "first-name").send_keys("Subash")
        driver.find_element(By.ID, "last-name").send_keys("Mahato")
        driver.find_element(By.ID, "postal-code").send_keys("44600")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()
        confirmation = driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you" in confirmation.text

    def test_checkout_empty_firstname(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.ID, "last-name").send_keys("Mahato")
        driver.find_element(By.ID, "postal-code").send_keys("44600")
        driver.find_element(By.ID, "continue").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "First Name is required" in error.text

    def test_checkout_empty_lastname(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.ID, "first-name").send_keys("Subash")
        driver.find_element(By.ID, "postal-code").send_keys("44600")
        driver.find_element(By.ID, "continue").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "Last Name is required" in error.text

    def test_checkout_empty_zipcode(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.ID, "first-name").send_keys("Subash")
        driver.find_element(By.ID, "last-name").send_keys("Mahato")
        driver.find_element(By.ID, "continue").click()
        error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        assert "Postal Code is required" in error.text
