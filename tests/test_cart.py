import pytest
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCart:

    def test_add_item_to_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert cart_badge.text == "1"

    def test_remove_item_from_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
        )
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0

    def test_cart_icon_navigates_to_cart(self, driver):
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
        assert "cart" in driver.current_url

    def test_multiple_items_in_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "1")
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "2")
        )
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "2"