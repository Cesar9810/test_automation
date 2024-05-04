from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()  
    context.login_page = LoginPage(context.driver)  
    context.login_page.open()

@when('I enter my email and password')
def step_impl(context):
    context.login_page.enter_email("Cesarcalderon+56@sumawealth.com")
    context.login_page.enter_password("/Upp3rR00m")

@when('I click on the Sign In button')
def step_impl(context):
    context.login_page.click_sign_in()
    # Esperar a que la página de inicio de sesión se cargue completamente
    WebDriverWait(context.driver, 10).until(
        EC.url_matches("https://development.sumawealth.io/homepage")
    )

@then('I should be logged in successfully')
def step_impl(context):
    assert context.login_page.is_logged_in(), "Login failed"
