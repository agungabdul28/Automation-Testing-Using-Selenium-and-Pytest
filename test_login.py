
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
options.headless = True
options.add_argument('--windows-size=1920,1080')


# Data Invalid Credential
Key = [
    ("User","pas4321"),     #Not match username and password
    ("Admin",""),           #Password is Empty
    ("","popo"),            #Username is Empty
    ("","")                 #Username and Password Is Empty
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@pytest.mark.positivetest
def test_login_success(setup):
    setup.find_element(By.ID, "txtUsername").send_keys("Admin")
    setup.find_element(By.ID, "txtPassword").send_keys("admin123")
    setup.find_element(By.ID, "btnLogin").click()

    dashMessage = setup.find_element(By.ID, "welcome").text

    if dashMessage == "Welcome Berney":   
        assert dashMessage == "Welcome Berney"
    elif dashMessage == "Welcome Abishek":
        assert dashMessage == "Welcome Abishek"

@pytest.mark.negativetest
@pytest.mark.parametrize('username,password',Key)
def test_invalid_login(setup,username,password):
    setup.find_element(By.ID, "txtUsername").send_keys(username)
    setup.find_element(By.ID, "txtPassword").send_keys(password)
    setup.find_element(By.ID, "btnLogin").click()
    time.sleep(4)

    invalidMsg = setup.find_element(By.ID, "spanMessage").text
    # assert invalidMsg == "Password cannot be empty"
    if invalidMsg == "Invalid credentials":
        assert invalidMsg == "Invalid credentials"
    elif invalidMsg == "Password cannot be empty":
        assert invalidMsg == "Password cannot be empty"
    elif invalidMsg == "Username cannot be empty":
        assert invalidMsg == "Username cannot be empty"



