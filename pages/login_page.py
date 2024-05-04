from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://development.sumawealth.io/login"

    def open(self):
        self.driver.get(self.url)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(By.XPATH, "//button[.//span[text()='Sign In']]")
        sign_in_button.click()

    def is_logged_in(self):
        current_url = self.driver.current_url
        return current_url == "https://development.sumawealth.io/homepage"
    


