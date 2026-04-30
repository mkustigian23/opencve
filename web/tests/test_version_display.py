# tests for first group issue 655 by Matt Kustigian
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")  # runs without opening a window
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_version_visible_in_sidebar(browser):
    # Step 1 - go to login page
    browser.get("http://localhost:80/accounts/login/")

    # Step 2 - log in
    browser.find_element(By.NAME, "login").send_keys("your_username")
    browser.find_element(By.NAME, "password").send_keys("your_password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 3 - check the version is visible in the sidebar
    sidebar_footer = browser.find_element(By.CLASS_NAME, "sidebar-footer")
    assert "v" in sidebar_footer.text, "Version number not found in sidebar"
    print(f"Version found: {sidebar_footer.text}")