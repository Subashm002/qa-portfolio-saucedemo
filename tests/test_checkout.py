import pytest
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckout:

    def setup_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart")
        )
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        driver.find_element(By.ID, "checkout").click()
        WebDriverWait(driver, 15).until(
            EC.url_contains("checkout-step-one")
        )

    def test_checkout_with_valid_details(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "input[data-test='firstName']").send_keys("Subash")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='lastName']").send_keys("Mahato")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys("44600")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='finish']"))
        )
        driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()
        confirmation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "Thank you" in confirmation.text

    def test_checkout_empty_firstname(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "input[data-test='lastName']").send_keys("Mahato")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys("44600")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "First Name is required" in error.text

    def test_checkout_empty_lastname(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "input[data-test='firstName']").send_keys("Subash")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys("44600")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Last Name is required" in error.text

    def test_checkout_empty_zipcode(self, driver):
        self.setup_cart(driver)
        driver.find_element(By.CSS_SELECTOR, "input[data-test='firstName']").send_keys("Subash")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='lastName']").send_keys("Mahato")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Postal Code is required" in error.text
