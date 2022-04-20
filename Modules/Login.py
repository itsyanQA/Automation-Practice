from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Login:
    """Login related element functions"""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def create_an_account_button(self):
        return self.driver.find_element(By.ID, 'SubmitCreate')

    def create_account_email_field(self):
        return self.driver.find_element(By.ID, 'email_create')

    def create_an_account_flow(self, email):
        self.create_account_email_field().send_keys(email)
        self.create_an_account_button().click()

    def create_an_account_flow_err_msgs(self):
        return self.driver.find_element(By.XPATH, '//ol/li')

    def title(self, index):
        titles = self.driver.find_elements(By.CSS_SELECTOR, 'input[name="id_gender"]')
        return titles[index]

    def firstname(self):
        return self.driver.find_element(By.ID, 'customer_firstname')

    def lastname(self):
        return self.driver.find_element(By.ID, 'customer_lastname')

    def email(self):
        return self.driver.find_element(By.ID, 'email')

    def password(self):
        return self.driver.find_element(By.ID, 'passwd')

    def day(self, day):
        day_element = self.driver.find_element(By.ID, 'days')
        select_day = Select(day_element)
        return select_day.select_by_value(day)

    def month(self, month):
        day_element = self.driver.find_element(By.ID, 'months')
        select_day = Select(day_element)
        return select_day.select_by_value(month)

    def year(self, year):
        day_element = self.driver.find_element(By.ID, 'years')
        select_day = Select(day_element)
        return select_day.select_by_value(year)

    def newsletter_checkbox(self):
        return self.driver.find_element(By.ID, 'newsletter')

    def receive_offer(self):
        return self.driver.find_element(By.ID, 'optin')

    def address(self):
        return self.driver.find_element(By.ID, 'address1')

    def city(self):
        return self.driver.find_element(By.ID, 'city')

    def state(self, state):
        state_element = self.driver.find_element(By.ID, 'id_state')
        select_state = Select(state_element)
        return select_state.select_by_visible_text(state)

    def zip(self):
        return self.driver.find_element(By.ID, 'postcode')

    def country(self, country):
        country_element = self.driver.find_element(By.ID, 'id_country')
        select_country = Select(country_element)
        return select_country.select_by_visible_text(country)

    def mobile_phone(self):
        return self.driver.find_element(By.ID, 'phone_mobile')

    def alias(self):
        return self.driver.find_element(By.ID, 'alias')

    def register_button(self):
        return self.driver.find_element(By.ID, 'submitAccount')

    def dob_flow(self, day, month, year):
        self.day(day)
        self.month(month)
        self.year(year)

    def account_creation_flow(self, title, firstname, lastname, email, password,
                              day, month, year, address, city, state, zip, country,
                              phone, alias):
        self.title(title).click()
        self.firstname().clear()
        self.firstname().send_keys(firstname)
        self.lastname().clear()
        self.lastname().send_keys(lastname)
        self.email().clear()
        self.email().send_keys(email)
        self.password().send_keys(password)
        self.dob_flow(day, month, year)
        self.address().clear()
        self.address().send_keys(address)
        self.city().send_keys(city)
        self.state(state)
        self.zip().send_keys(zip)
        self.country(country)
        self.mobile_phone().send_keys(phone)
        self.alias().clear()
        self.alias().send_keys(alias)
        self.register_button().click()

    def account_creation_error_bar(self):
        return self.driver.find_element(By.XPATH, "//ol/li")

    def sign_in_email(self):
        return self.driver.find_element(By.ID, 'email')

    def sign_in_password(self):
        return self.driver.find_element(By.ID, 'passwd')

    def sign_in_button(self):
        return self.driver.find_element(By.ID, 'SubmitLogin')

    def sign_in_flow(self, email, password):
        self.sign_in_email().send_keys(email)
        self.sign_in_password().send_keys(password)
        self.sign_in_button().click()

    def error_alert(self):
        return self.driver.find_element(By.XPATH, '//ol/li')
