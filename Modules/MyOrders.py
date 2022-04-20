from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class MyOrders:
    """Class that has "My Orders" related element functions"""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def order_reference_first_in_row(self):
        return self.driver.find_element(By.XPATH, "//tr[@class='first_item ']/td/a")

    def order_date_first(self):
        return self.driver.find_element(By.XPATH, "//tr[@class='first_item ']/td[2]")

    def order_price_first(self):
        return self.driver.find_element(By.XPATH, "//tr[@class='first_item ']/td[3]/span")

    def order_payment_method(self):
        return self.driver.find_element(By.XPATH, "//tr[@class='first_item ']/td[4]")
