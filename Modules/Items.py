from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class Items:
    """Class that has item related element functions"""
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def wait_pop_up_msg(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="layer_cart'
                                                                           '_cart col-xs-12 col-md-6"]')))

    def click_continue_shopping(self):
        button = self.driver.find_element(By.XPATH, '//span[@class="continue btn btn-default'
                                                    ' button exclusive-medium"]/span')
        return button.click()

    def list_view(self):
        return self.driver.find_element(By.CSS_SELECTOR, "i[class='icon-th-list']")

    def item_selection(self, index):
        items = self.driver.find_elements(By.XPATH, "//h5[@itemprop='name']/a[@class='product-name']")
        li = [i for i in items]
        return li[index]

    def add_to_cart(self):
        return self.driver.find_element(By.XPATH, "//p/button/span[text()='Add to cart']")

    def quantity(self):
        return self.driver.find_element(By.ID, 'quantity_wanted')

    def quantity_selection_by_text(self):
        qty = self.driver.find_element(By.ID, 'quantity_wanted')
        qty.clear()
        return qty

    def quantity_minus(self):
        return self.driver.find_element(By.XPATH, "//span/i[@class='icon-minus']")

    def quantity_plus(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="btn btn-default button-plus product_quantity_up"]')

    def size_selection(self, size):
        size_menu_element = self.driver.find_element(By.ID, 'group_1')
        size_select = Select(size_menu_element)
        return size_select.select_by_visible_text(size)

    def colors(self, color):
        colors = self.driver.find_elements(By.XPATH, "//div[@class='attribute_list']/ul/li/a")
        for i in colors:
            if i.accessible_name == color:
                return i
        else:
            return None

    def total_products_in_section(self):
        ele = self.driver.find_element(By.CSS_SELECTOR, 'span[class="heading-counter"]')
        for i in ele.text:
            if i.isnumeric():
                return i
            else:
                pass
        else:
            return None

    def raw_total_items(self):
        items = self.driver.find_elements(By.XPATH, "//h5[@itemprop='name']/a[@class='product-name']")
        return str(len(items))

    def slider_left(self, x, y):
        slider_element_left = self.driver.find_element(By.XPATH,
                                                       '(//a[@class="ui-slider-handle ui-state-default ui-corner-'
                                                       'all"])[1]')
        sliding = self.action.drag_and_drop_by_offset(slider_element_left, x, y).perform()
        return sliding

    def slider_right(self, x, y):
        slider_element_right = self.driver.find_element(By.XPATH, '(//a[@class="ui-slider-handle ui-state-default ui-'
                                                                  'corner-all"])[1]')
        self.action.drag_and_drop_by_offset(slider_element_right, x, y).perform()

    def explicit_wait_for_filters_pop(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "enabled_filters")))

    def sort_items(self, sort_type):
        sort_element = self.driver.find_element(By.ID, "selectProductSort")
        sort_select = Select(sort_element)
        return sort_select.select_by_visible_text(sort_type)

    def item_prices(self):
        a = self.driver.find_elements(By.XPATH, '//div[@class="content_price col-xs-5 col-md-12"]'
                                                '/span[@class="price product-price"]')
        prices = [i.text[1:] for i in a]
        return prices

    def sort_by_lowest_first_calculation(self):
        price_list = self.item_prices()
        return sorted(price_list)

    def cheapest_item(self):
        a = self.driver.find_elements(By.XPATH, '//div[@class="content_price col-xs-5 col-md-12"]'
                                                '/span[@class="price product-price"]')
        prices = [i.text[1:] for i in a]
        return min(prices)

    def most_expensive_item(self):
        a = self.driver.find_elements(By.XPATH, '//div[@class="content_price col-xs-5 col-md-12"]'
                                                '/span[@class="price product-price"]')
        prices = [i.text[1:] for i in a]
        return max(prices)

    def item_names(self):
        a = self.driver.find_elements(By.CSS_SELECTOR, 'h5[itemprop="name"]>a')
        names = [i.text for i in a]
        return names

    def item_names_individual(self, index):
        a = self.driver.find_elements(By.CSS_SELECTOR, 'h5[itemprop="name"]>a')
        return a[index]

    def item_names_sorted_a_to_z(self):
        return sorted(self.item_names())

    def item_names_sorted_z_to_a(self):
        sorted_names_reversed = self.item_names_sorted_a_to_z()
        sorted_names_reversed.sort(reverse=True)
        return sorted_names_reversed

    def add_to_wishlist_from_catalog(self, index):
        items = self.driver.find_elements(By.CLASS_NAME, "addToWishlist")
        return items[index]

    def close_pop_up_wishlist(self):
        return self.driver.find_element(By.CLASS_NAME, "fancybox-close")

    @staticmethod
    def raw_wait(seconds):
        return sleep(seconds)
