import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url, "Login failed - inventory page not loaded"

    def test_invalid_password(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "wrongpassword")
        error = page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, driver):
        page = LoginPage(driver)
        page.login("", "secret_sauce")
        error = page.get_error_message()
        assert "Username is required" in error

    def test_empty_password(self, driver):
        page = LoginPage(driver)
        page.login("standard_user", "")
        error = page.get_error_message()
        assert "Password is required" in error

    def test_locked_out_user(self, driver):
        page = LoginPage(driver)
        page.login("locked_out_user", "secret_sauce")
        error = page.get_error_message()
        assert "locked out" in error