from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class CartIcon:
    """This Class covers the cart icon elements + checkout"""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def hover_cart(self):
        hover = self.driver.find_element(By.XPATH, "(//a[@href='http://automationpractice.com/"
                                                   "index.php?controller=order'])[1]")
        self.action.move_to_element(hover).perform()

    def wait_for_cart_to_show_up(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="cart-prices-line last-line"]')))

    def item_color_in_cart(self, color):
        colors = self.driver.find_elements(By.XPATH, '//dt/div/div[@class="product-atributes"]')
        for i in colors:
            if color in i.text:
                return True
            else:
                pass
        else:
            return False

    def item_size_in_cart(self, size):
        sizes = self.driver.find_elements(By.XPATH, '//dt/div/div[@class="product-atributes"]')
        for i in sizes:
            if size == i.text[-1]:
                return True
            else:
                pass
        else:
            return False

    def checkout_button(self):
        self.hover_cart()
        return self.driver.find_element(By.CSS_SELECTOR, 'a[id="button_order_cart"]>span>i')

    def summary_and_address_proceed(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Proceed to checkout']")

    def shipping_proceed(self):
        return self.driver.find_element(By.XPATH, '(//span/i[@class="icon-chevron-right right"])[3]')

    def proceed_flow_invalid(self):
        self.summary_and_address_proceed().click()
        self.summary_and_address_proceed().click()
        self.shipping_proceed().click()

    def proceed_flow_valid(self):
        self.summary_and_address_proceed().click()
        self.summary_and_address_proceed().click()
        self.shipping_terms_checkbox().click()
        self.shipping_proceed().click()

    def shipping_terms_checkbox(self):
        return self.driver.find_element(By.ID, 'cgv')

    def shipping_terms_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div[class="fancybox-inner"]>p')

    def wait_for_terms_pop_up(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="fancybox-inner"]>p')))

    def pay_by_bank_wire(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="bankwire"]')

    def pay_by_check(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="cheque"]')

    def confirm_order_element(self):
        return self.driver.find_element(By.XPATH, "//span[text()='I confirm my order']")

    def order_complete_bank_wire(self):
        return self.driver.find_element(By.XPATH, "//strong[text()='Your order on My Store is complete.']")

    def order_complete_check(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'p[class="alert alert-success"]')

    def take_reference_from_order_completion(self):
        ref = self.driver.find_element(By.XPATH, "//div[@class='box']")
        p = ref.text
        for word in p.split():
            if word.isupper() and len(word) == 9:
                return word
            else:
                pass
        else:
            return 'Not Found'

    def take_total_from_order_completion(self):
        total = self.driver.find_element(By.XPATH, "//div[@class='box']")
        p = total.text
        for word in p.split():
            if word[0] == '$':
                return word
            else:
                pass
        else:
            return 'Not Found'

    def take_payment_method_from_order_completion(self):
        method = self.driver.find_element(By.XPATH, "//div[@class='box']")
        p = method.text
        if 'bank wire' in p:
            return 'Bank wire'
        elif 'pay by check.' in p:
            return 'Payment By Check'
        else:
            return 'Not Found'

    def wait_for_order_completion(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='box']")))
