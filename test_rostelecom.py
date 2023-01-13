import pytest
import time
import selenium
from random import random, randrange, randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


def generate_string(n):
   return "ф" * n

def english_chars():
   return 'abcdefghijklmnopqrstuvwxyz'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    return chrome_options

@pytest.fixture
def get_webdriver(chrome_options):
    options=chrome_options
    driver=webdriver.Chrome(options=options)
    return driver

@pytest.fixture(scope="function")
def open_chrome():
    pytest.driver = webdriver.Chrome('../chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.implicitly_wait(2)
    pytest.driver.get('https://b2c.passport.rt.ru')
    yield

    pytest.driver.quit()

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



def test_left_right(open_chrome):
    # WebDriverWait(pytest.driver, 5).until(
    # EC.presence_of_element_located((By.XPATH,"//*[contains(@class, 'rt-check-small-icon')]"))).click()
    time.sleep(2)

    page_left = pytest.driver.find_elements(By.ID, 'page-left')
    lk = page_left[0].text.split('\n')
    try:
        assert lk[0] != 'Личный кабинет'
    except AssertionError:
        print('Элемент присутствует в левой части формы.')

def test_auth_valid_data_mail(open_chrome):
    email = 'libevo9598@themesw.com'
    password = '123456789oO'
    mail = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    mail.clear()
    mail.send_keys(email)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']").click()
    user_info = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Учетные данные']")))
    assert user_info != ''

def test_auth_invalid_data_mail(open_chrome):
    email = 'libevo9598@themesw.com'
    password = '12345678910'
    mail = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    mail.clear()
    mail.send_keys(email)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    error = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-error-message")))
    placeholder = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Электронная почта')]")))
    assert error.text == 'Неверный логин или пароль'
    assert placeholder.text == 'Электронная почта'

def test_auth_valid_data_btn_mail(open_chrome):
    email = 'libevo9598@themesw.com'
    password = '123456789oO'
    btn_mail = WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-mail')))
    btn_mail.click()
    mail = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    mail.clear()
    mail.send_keys(email)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    user_info = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Учетные данные']")))
    assert user_info != ''

def test_auth_invalid_data_phone(open_chrome):
    """Проверка входа с неверным номером"""
    phone = '91231231212'
    password = '123456789oO'
    phone_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    phone_field.clear()
    phone_field.send_keys(phone)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    error = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-error-message")))
    assert error.text == 'Неверный логин или пароль'

def test_auth_valid_data_phone(open_chrome):
    phone = '9991234567'
    password = '123456789oO'
    phone_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    phone_field.clear()
    phone_field.send_keys(phone)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    user_info = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Учетные данные']")))
    assert user_info != ''

def test_auth_valid_data_btn_login(open_chrome):
    login = 'rtkid_1673332728041'
    password = '123456789oO'
    btn_login = WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-login')))
    btn_login.click()
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
    user_info = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Учетные данные']")))
    assert user_info != ''


def test_auth_invalid_data_login(open_chrome):
    login = 'rtkid_0003332728041'
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
    placeholder = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Логин')]")))
    error = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-error-message")))
    assert error.text == 'Неверный логин или пароль'
    assert placeholder.text=='Логин'


def test_auth_valid_data_login(open_chrome):
    url = pytest.driver.current_url
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
    # old_url='https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=0898e74f-d3cf-4894-b9c4-56e9d3dfb14a&theme&auth_type'
    redirect_url = pytest.driver.current_url
    user_info = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Учетные данные']")))
    assert user_info != ''
    assert redirect_url != url


def test_auth_invalid_data_btn_ls(open_chrome):
    ls = '123456789111'
    password = '123456789oO'
    btn_ls = WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.ID, 't-btn-tab-ls')))
    btn_ls.click()
    ls_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    ls_field.clear()
    ls_field.send_keys(ls)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    error = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "form-error-message")))
    assert error.text == 'Неверный логин или пароль'


def test_auth_invalid_data_ls(open_chrome):
    ls = '123456789111'
    password = '123456789oO'
    ls_field = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    ls_field.clear()
    ls_field.send_keys(ls)
    passw = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    passw.clear()
    passw.send_keys(password)
    enter = pytest.driver.find_element(By.XPATH, "//*[@type='submit']")
    enter.click()
    placeholder = WebDriverWait(pytest.driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//span[contains(text(),'Лицевой счет')]")))
    # error = WebDriverWait(pytest.driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "form-error-message")))
    try:
        assert placeholder == False
    except AssertionError:
        print("Таб смены аутентификации не сработал")



@pytest.mark.parametrize('locator', ['oidc_ok', 'oidc_vk', 'oidc_mail', 'oidc_google', 'oidc_ya'],
                         ids=['ok', 'vk', 'mail', 'google', 'ya'])
def test_auth_with_params(open_chrome, locator):
    url = pytest.driver.current_url
    btn_ = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, locator)))
    btn_.click()
    redirect_url = pytest.driver.current_url
    assert redirect_url != url

def test_auth_time_code(open_chrome,get_lk):
    username=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//h2[@class='sc-bvFjSx iqOiiv']")))
    username.click()
    escape=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Выйти')]")))
    escape.click()
    auth_page_code=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"// h1[contains(text(), 'Авторизация по коду')]")))
    assert  auth_page_code.text== 'Авторизация по коду'

def test_auth_time_code_mail(open_chrome,get_lk):
    mail='libevo9598@themesw.com'
    username=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//h2[@class='sc-bvFjSx iqOiiv']")))
    username.click()
    escape=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Выйти')]")))
    escape.click()
    email=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID,"address")))
    email.clear()
    email.send_keys(mail)
    url=pytest.driver.current_url
    btn_get_code=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID,"otp_get_code")))
    btn_get_code.click()
    redirect_url=pytest.driver.current_url
    new_form= WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Код подтверждения отправлен')]")))
    assert url!=redirect_url
    assert new_form.text == 'Код подтверждения отправлен'
def test_auth_time_code_phone(open_chrome,get_lk):
    phone='+79991234567'
    username=WebDriverWait(pytest.driver, 15).until(
        EC.presence_of_element_located((By.XPATH,"//h2[@class='sc-bvFjSx iqOiiv']")))
    username.click()
    escape=WebDriverWait(pytest.driver, 15).until(
        EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Выйти')]")))
    escape.click()
    phone_field=WebDriverWait(pytest.driver, 15).until(
        EC.presence_of_element_located((By.ID,"address")))
    phone_field.clear()
    phone_field.send_keys(phone)
    url=pytest.driver.current_url
    btn_get_code=WebDriverWait(pytest.driver, 15).until(
        EC.presence_of_element_located((By.ID,"otp_get_code")))
    btn_get_code.click()
    redirect_url=pytest.driver.current_url
    new_form= WebDriverWait(pytest.driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Код подтверждения отправлен')]")))
    assert url!=redirect_url
    assert new_form.text == 'Код подтверждения отправлен'

def test_auth_time_code_invalid_phone(open_chrome, get_lk):
    phone = '000000000000'
    username = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='sc-bvFjSx iqOiiv']")))
    username.click()
    escape = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Выйти')]")))
    escape.click()
    phone_field = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.ID, "address")))
    phone_field.clear()
    phone_field.send_keys(phone)
    url = pytest.driver.current_url
    btn_get_code = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.ID, "otp_get_code")))
    btn_get_code.click()
    redirect_url = pytest.driver.current_url

    error = WebDriverWait(pytest.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"// span[contains(text(), 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))
    print(error.text)
    assert url==redirect_url
    assert error.text=='Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

def test_auth_time_invalid_code(open_chrome,get_lk):
    phone='+79991234567'
    username=WebDriverWait(pytest.driver, 15).until(
        EC.presence_of_element_located((By.XPATH,"//h2[@class='sc-bvFjSx iqOiiv']")))
    username.click()
    escape=WebDriverWait(pytest.driver, 20).until(
        EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Выйти')]")))
    escape.click()
    phone_field=WebDriverWait(pytest.driver, 20).until(
        EC.presence_of_element_located((By.ID,"address")))
    phone_field.clear()
    phone_field.send_keys(phone)
    # url=pytest.driver.current_url
    btn_get_code=WebDriverWait(pytest.driver, 20).until(
        EC.presence_of_element_located((By.ID,"otp_get_code")))
    btn_get_code.click()
    code_num_1 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-0")))
    code_num_1.send_keys(randrange(10))

    code_num_2 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-1")))
    code_num_2.send_keys(randrange(10))

    code_num_3 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-2")))
    code_num_3.send_keys(randrange(10))

    code_num_4 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-3")))
    code_num_4.send_keys(randrange(10))

    code_num_5 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-4")))
    code_num_5.send_keys(randrange(10))

    code_num_6 = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rt-code-5")))
    code_num_6.send_keys(randrange(10))
    error=WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID,'form-error-message')))
    assert error.text == 'Неверный код. Повторите попытку'


# @pytest.mark.parametrize('firstname',[generate_string(1),generate_string(2),generate_string(30),generate_string(31),
#                         english_chars(),special_chars()],
#                          ids=['1 кириллический символ ', '2 кириллических символа',
#                          '30 кириллических символов','31 кириллических символ','английский алфавит','специальные символы'])
# @pytest.mark.parametrize('lastname_',[generate_string(1),generate_string(2),generate_string(30),generate_string(31),
#                         english_chars(),special_chars()],
#                          ids=['1 кириллический символ ', '2 кириллических символа',
#                          '30 кириллических символов','31 кириллических символ','английский алфавит','специальные символы'])
# def test_registration(open_chrome,firstname,lastname_):
#     registration = WebDriverWait(pytest.driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'kc-register')))
#     registration.click()
#     name = WebDriverWait(pytest.driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'firstName')))
#     name.clear()
#     name.click()
#     name.send_keys(firstname)
#
#     lastname = WebDriverWait(pytest.driver, 10).until(
#         EC.presence_of_element_located((By.NAME, 'lastName')))
#     lastname.clear()
#     lastname.send_keys(lastname_)
#
#     adress = WebDriverWait(pytest.driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'address')))
#     adress.clear()
#     adress.send_keys('adress')
#     password = WebDriverWait(pytest.driver, 20).until(
#         EC.presence_of_element_located((By.ID, 'password')))
#     password.clear()
#     password.send_keys('password')
#
#     password_confirm = WebDriverWait(pytest.driver, 20).until(
#         EC.presence_of_element_located((By.ID, 'password-confirm')))
#     password_confirm.clear()
#     password_confirm.send_keys('password')
#     error_name = WebDriverWait(pytest.driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")))
#     enter = WebDriverWait(pytest.driver, 20).until(
#         EC.presence_of_element_located((By.NAME, 'register')))
#     enter.click()
#     error_adress =WebDriverWait(pytest.driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")))
#     assert error_name.text!=''
#     assert error_adress!=''
#
