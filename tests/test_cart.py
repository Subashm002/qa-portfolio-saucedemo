import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCart:

    def test_add_item_to_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_button.click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", "Cart badge should show 1"

    def test_remove_item_from_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart should be empty"

    def test_cart_icon_navigates_to_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "cart" in driver.current_url, "Should navigate to cart page"

    def test_multiple_items_in_cart(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "2", "Cart badge should show 2"
