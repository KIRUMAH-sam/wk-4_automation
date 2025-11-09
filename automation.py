# Importing libraries
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure your test target
BASE_URL = "http://127.0.0.1:5000/login"  

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def do_login(driver, username, password):
    driver.get(BASE_URL)
    # Update selectors to match the page
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(1)
    return driver.page_source

def test_login_valid(driver):
    page = do_login(driver, "valid_user", "valid_pass")
    # Adjust assertion to application behavior 
    assert "Dashboard" in page or "Logout" in page

def test_login_invalid(driver):
    page = do_login(driver, "invalid_user", "wrong_pass")
    # Adjust to the application's error message
    assert "Invalid credentials" in page or "login failed" in page.lower()
