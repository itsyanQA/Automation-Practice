from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Homepage:
    """Homepage related element functions"""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def sign_in(self):
        return self.driver.find_element(By.LINK_TEXT, 'Sign in')

    def account_name_when_logged_in(self):
        return self.driver.find_element(By.XPATH, "//div/a[@class='account']/span")

    def my_order(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Order history and details']")

    def wishlist(self):
        return self.driver.find_element(By.XPATH, "//span[text()='My wishlists']")

    def wishlist_collection(self):
        return self.driver.find_element(By.XPATH, '//td[@style="width:200px;"]/a')

    def item_name_in_wishlist(self):
        return self.driver.find_element(By.ID, "s_title")

    def header_banner(self):
        return self.driver.find_element(By.XPATH, "//a/img[@src='http://automationpractice.com/"
                                                  "modules/blockbanner/img/sale70.png']")

    def site_logo(self):
        return self.driver.find_element(By.XPATH, "//div[@id='header_logo']/a/img")

    def women(self):
        return self.driver.find_element(By.XPATH, "(//a[text()='Women'])[1]")

    def dresses(self):
        return self.driver.find_element(By.XPATH, '(//a[@href="http://automationpractice.com/index.php?id_category'
                                                  '=8&controller=category"])[2]')

    def t_shirts(self):
        return self.driver.find_element(By.XPATH, "(//a[text()='T-shirts'])[2]")

    # =============================== Contact Us Section ===========================

    def contact_us_nav(self):
        return self.driver.find_element(By.LINK_TEXT, "Contact us")

    def subject_heading(self, heading):
        subject_element = self.driver.find_element(By.ID, "id_contact")
        select_subject = Select(subject_element)
        return select_subject.select_by_visible_text(heading)

    def email_address(self):
        return self.driver.find_element(By.ID, 'email')

    def order_reference(self):
        return self.driver.find_element(By.ID, 'id_order')

    def attach_file(self):
        return self.driver.find_element(By.ID, 'fileUpload')

    def message(self):
        return self.driver.find_element(By.ID, 'message')

    def send_button(self):
        return self.driver.find_element(By.ID, "submitMessage")

    def contact_us_successful(self):
        return self.driver.find_element(By.XPATH, '//div[@id="center_column"]/p')

    def contact_us_errors(self):
        return self.driver.find_element(By.XPATH, "//ol/li")

    def contact_us_flow(self, heading, email, order, file_path, msg):
        self.subject_heading(heading)
        self.email_address().send_keys(email)
        self.order_reference().send_keys(order)
        self.attach_file().send_keys(file_path)
        self.message().send_keys(msg)
        self.send_button().click()

    def search_bar(self):
        return self.driver.find_element(By.ID, "search_query_top")

    def search_bar_flow(self, keys):
        self.search_bar().send_keys(keys)
        self.search_bar().send_keys(Keys.ENTER)

    def search_bar_error_element(self):
        return self.driver.find_element(By.XPATH, '//p[@class="alert alert-warning"]')
