import pytest
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    return chrome_options
@pytest.fixture
def get_webdriver(chrome_options):
    options=chrome_options
    driver=webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope='session')
def setup(request,get_webdriver):
    driver=get_webdriver
    url=''
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def get_lk(open_chrome):
    login = 'rtkid_1673332728041'
    password = '123456789oO'
    login_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    login_field.clear()
    login_field.send_keys(login)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    lk=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'lk-btn')))
    lk.click()
    yield
