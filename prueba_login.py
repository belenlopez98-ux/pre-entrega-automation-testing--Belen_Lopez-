from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# --- TEST AUTOMATIZADO DE LOGIN ---
def test_login_exitoso():
 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    # Ingresar usuario
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    # Ingresar contraseña
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click en botón Login
    driver.find_element(By.ID, "login-button").click()

    assert '/inventory.html'


    driver.quit()