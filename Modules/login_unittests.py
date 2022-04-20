from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Homepage import Homepage
from Login import Login
from Items import Items
from Cart_Icon import CartIcon
from MyOrders import MyOrders
from datetime import date


class Practice(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.home = Homepage(self.driver)
        self.login = Login(self.driver)
        self.item = Items(self.driver)
        self.cart_icon = CartIcon(self.driver)
        self.my_orders = MyOrders(self.driver)
        self.today = date.today()
        self.today_format = self.today.strftime("%m/%d/%Y")

    # ===================== Testing email field for account creation purpose ========================
    def test_email_already_in_use(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('yantesting@testing.com')
        # Assert that we get a msg that email is already taken
        self.assertEqual(self.login.create_an_account_flow_err_msgs().text, 'An account using this email address has '
                                                                            'already been registered. Please enter a'
                                                                            ' valid password or request a new one.')

    def test_email_blank(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('')
        # Assert that we get a msg that email is invalid
        self.assertEqual(self.login.create_an_account_flow_err_msgs().text, 'Invalid email address.')

    # ================================================================================================

    # ======================= Testing Account Creation Valid + Invalid Cases =========================

    def test_account_creation_valid(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('123456@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', '123456@testing.com',
                                         '123321ya', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Asserting that 'yan nay' is logged in by comparing the name to the result
        self.assertEqual(self.home.account_name_when_logged_in().text, 'yan nay')

    def test_account_creation_firstname_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlfength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, '', 'nay', 'pwlefngth@testing.com',
                                         '1233', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Asserting that 'yan nay' is logged in by comparing the name to the result
        self.assertEqual(self.login.account_creation_error_bar().text, 'firstname is required.')

    def test_account_creation_lastname_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlfength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'firstname', '', 'pwlfength@testing.com',
                                         '1233', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'lastname is required.')

    def test_account_creation_email_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlfength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'firstname', 'nay', '',
                                         '1233', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'email is required.')

    def test_account_creation_invalid_password_length(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwlefngth@testing.com',
                                         '1233', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'passwd is invalid.')

    def test_account_creation_address1_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwlfength@testing.com',
                                         '1233321fds', '7', '8', '1956',
                                         '', 'city',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'address1 is required.')

    def test_account_creation_city_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwlfength@testing.com',
                                         '1233765gh', '7', '8', '1956',
                                         'random address', '',
                                         'Hawaii', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'city is required.')

    def test_account_creation_state_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwflength@testing.com',
                                         '1233543gfd', '7', '8', '1956',
                                         'gfdg', 'city',
                                         '-', '12345', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, 'This country requires you to choose a State.')

    def test_account_creation_zip_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwflength@testing.com',
                                         '1233fd65', '7', '8', '1956',
                                         'gfdg', 'city',
                                         'Hawaii', '', 'United States', '12345', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, "The Zip/Postal code you've entered is invalid. "
                                                                       "It must follow this format: 00000")

    def test_account_creation_country_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('pwlength@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'pwflength@testing.com',
                                         '123354gf', '7', '8', '1956',
                                         'gfdg', 'city',
                                         'Hawaii', '12345', '-', '12345', 'alias')
        # Check that the error message is precise
        self.assertIn(self.login.account_creation_error_bar().text, "id_country is required.")

    def test_account_creation_phone_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('yftesting@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'yfftesting@testing.com',
                                         '123321ya', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, "You must register at least one phone number.")

    def test_account_creation_phone_non_numeric(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('yftesting@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'yfftesting@testing.com',
                                         '123321ya', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', 'hfhgf', 'alias')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, "phone_mobile is invalid.")

    def test_account_creation_alias_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email
        self.login.create_an_account_flow('yftesting@testing.com')
        # Start user-creation flow
        self.login.account_creation_flow(0, 'yan', 'nay', 'yfftesting@testing.com',
                                         '123321ya', '7', '8', '1956',
                                         'random address', 'city',
                                         'Hawaii', '12345', 'United States', '050473836', '')
        # Check that the error message is precise
        self.assertEqual(self.login.account_creation_error_bar().text, "alias is required.")

    # =======================================================================================================

    # ==========================================Login testing================================================

    def test_login_valid_credentials(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@69.com', '123321ya')
        # Assert that url is proceeding to a different one
        self.assertEqual(self.driver.current_url, 'http://automationpractice.com/index.php?controller=my-account')

    def test_login_invalid_email(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@87878.com', '123321ya')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'Authentication failed.')

    def test_login_invalid_password(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@69.com', '123321')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'Authentication failed.')

    def test_login_invalid_4_char_password(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@69.com', '1233')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'Invalid password.')

    def test_login_invalid_email_no_abbreviation(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@69', '123321ay')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'Invalid email address.')

    def test_login_email_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('', '123321ya')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'An email address required.')

    def test_login_password_null(self):
        # Click sign in inside the home page
        self.home.sign_in().click()
        # Enter email and password, and click on log-in
        self.login.sign_in_flow('1@69.com', '')
        # Assert that error message is correct
        self.assertEqual(self.login.error_alert().text, 'Password is required.')

    # =======================================================================================================

    def test_logo_click_proceeds_to_homepage(self):
        """Testing that a click on the logo leads us to the home page"""
        # Go to women section
        self.home.women().click()
        # Click on the logo picture
        self.home.site_logo().click()
        # Assert that we are in the home page by checking the url
        self.assertEqual(self.driver.current_url, 'http://automationpractice.com/index.php')

    def test_category_nav(self):
        """Testing every section in the nav bar"""
        # Click on women section
        self.home.women().click()
        # Assert that we are in women page
        self.assertEqual(self.driver.current_url, 'http://automationpractice.com/index.php?id_category=3&controller='
                                                  'category')
        # Go back to home page
        self.driver.back()
        # Click on dresses section
        self.home.dresses().click()
        # Assert that we are in dresses page
        self.assertEqual(self.driver.current_url, 'http://automationpractice.com/index.php?id_category=8&controller='
                                                  'category')
        # Go back to home page
        self.driver.back()
        # Click on t-shirts section
        self.home.t_shirts().click()
        # Assert that we are in t_shirts page
        self.assertEqual(self.driver.current_url, 'http://automationpractice.com/index.php?id_category=5&controller='
                                                  'category')

    # ================================ Testing Contact Us Cases ================================

    def test_contact_us_valid(self):
        # Click on contact us
        self.home.contact_us_nav().click()
        # Go over the contact us flow
        self.home.contact_us_flow('Customer service', '1@1.com', '123', 'C:\\random.png', 'testing')
        # Assert that the message went through
        self.assertEqual(self.home.contact_us_successful().text, 'Your message has been successfully sent to our team.')

    def test_contact_us_no_header(self):
        # Click on contact us
        self.home.contact_us_nav().click()
        # Fill the contact us flow without choosing an header
        self.home.contact_us_flow('-- Choose --', '1@1.com', '123', 'C:\\random.png', 'testing')
        # Assert that the text error is as we expect
        self.assertEqual(self.home.contact_us_errors().text, 'Please select a subject from the list provided.')

    def test_contact_us_email_null(self):
        # Click on contact us
        self.home.contact_us_nav().click()
        # Fill the contact us flow without choosing an header
        self.home.contact_us_flow('Webmaster', '', '123', 'C:\\random.png', 'testing')
        # Assert that the text error is as we expect
        self.assertEqual(self.home.contact_us_errors().text, 'Invalid email address.')

    def test_contact_message_null(self):
        # Click on contact us
        self.home.contact_us_nav().click()
        # Fill the contact us flow without choosing an header
        self.home.contact_us_flow('Webmaster', '1@1.com', '123', 'C:\\random.png', '')
        # Assert that the text error is as we expect
        self.assertEqual(self.home.contact_us_errors().text, 'The message cannot be blank.')

    # ===================================================================================================

    def test_items_quantity(self):
        # Click on women category
        self.home.women().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the first item
        self.item.item_selection(0).click()
        # Clear the quantity bar
        self.item.quantity().clear()
        # Click plus
        self.item.quantity_plus().click()
        # Click plus
        self.item.quantity_plus().click()
        # Capture screenshot of the bug
        self.driver.get_screenshot_as_file('Quantity Bug.png')
        # Check that quantity is 2
        self.assertEqual(self.item.quantity().get_attribute('value'), '2')
        # BUG FOUND, When qty is null, clicking on + will set qty to 100000000000

    def test_items_quantity_workaround(self):
        # Click on women category
        self.home.women().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the first item
        self.item.item_selection(0).click()
        # Clear the quantity bar
        self.item.quantity().clear()
        # Set qty to 0
        self.item.quantity_selection_by_text().send_keys(0)
        # Click plus
        self.item.quantity_plus().click()
        # Click plus
        self.item.quantity_plus().click()
        # Check that quantity is 2
        self.assertEqual(self.item.quantity().get_attribute('value'), '2')

    def test_color_picking(self):
        # Click on women category
        self.home.women().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the first item
        self.item.item_selection(0).click()
        # Click on blue color
        self.item.colors('Blue').click()
        # Add to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Hover on the cart
        self.cart_icon.hover_cart()
        # Assert that the color is indeed picked
        self.cart_icon.wait_for_cart_to_show_up()
        # Wait until cart pops up after we hover on it
        self.assertTrue(self.cart_icon.item_color_in_cart('Blue'), True)

    def test_size_picking(self):
        # Click on dresses category
        self.home.dresses().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the first item
        self.item.item_selection(0).click()
        # Choose Large size
        self.item.size_selection('L')
        # Add item to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Hover on the cart
        self.cart_icon.hover_cart()
        # Wait for the icon to fully appear
        self.cart_icon.wait_for_cart_to_show_up()
        # Assert that the size is indeed picked
        self.assertTrue(self.cart_icon.item_size_in_cart('L'), True)

    def test_total_items_in_women_section(self):
        # Click on women category
        self.home.women().click()
        # Click on list view
        self.item.list_view().click()
        # Assert that the products counter is reliable by the number it presents to the actual manual count of the items
        self.assertEqual(self.item.total_products_in_section(), self.item.raw_total_items())

    def test_total_items_in_dresses_section(self):
        # Click on women category
        self.home.dresses().click()
        # Click on list view
        self.item.list_view().click()
        # Assert that the products counter is reliable by the number it presents to the actual manual count of the items
        self.assertEqual(self.item.total_products_in_section(), self.item.raw_total_items())

    def test_total_items_in_t_shirts_section(self):
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Assert that the products counter is reliable by the number it presents to the actual manual count of the items
        self.assertEqual(self.item.total_products_in_section(), self.item.raw_total_items())

    def test_payment_without_accepting_terms_invalid(self):
        # Click on sign in
        self.home.sign_in().click()
        # Sign in
        self.login.sign_in_flow('yantesting@testing.com', '123321ya')
        # Go to home Page
        self.home.site_logo().click()
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the third item
        self.item.item_selection(0).click()
        # Click add to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Click checkout
        self.cart_icon.checkout_button().click()
        # Proceed to checkout
        self.cart_icon.proceed_flow_invalid()
        # Wait until we see the pop up msg
        self.cart_icon.wait_for_terms_pop_up()
        # Assert that we see the pop up msg and we don't continue with the checkout
        self.assertEqual(self.cart_icon.shipping_terms_msg().text, 'You must agree to the terms of service before '
                                                                   'continuing.')

    def test_payment_bank_wire(self):
        # Click on sign in
        self.home.sign_in().click()
        # Sign in
        self.login.sign_in_flow('yantesting@testing.com', '123321ya')
        # Go to home Page
        self.home.site_logo().click()
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the third item
        self.item.item_selection(0).click()
        # Click add to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Hover on the cart
        self.cart_icon.hover_cart()
        # Click checkout
        self.cart_icon.checkout_button().click()
        # Proceed to checkout
        self.cart_icon.proceed_flow_valid()
        # Click "Pay by Bank Wire"
        self.cart_icon.pay_by_bank_wire().click()
        # Confirm order
        self.cart_icon.confirm_order_element().click()
        # Assert that order is done
        self.assertEqual(self.cart_icon.order_complete_bank_wire().text, 'Your order on My Store is complete.')

    def test_payment_check(self):
        # Click on sign in
        self.home.sign_in().click()
        # Sign in
        self.login.sign_in_flow('yantesting@testing.com', '123321ya')
        # Go to home Page
        self.home.site_logo().click()
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the third item
        self.item.item_selection(0).click()
        # Click add to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Click checkout
        self.cart_icon.hover_cart()
        self.cart_icon.checkout_button().click()
        # Proceed to checkout
        self.cart_icon.proceed_flow_valid()
        # Click "Pay by Check"
        self.cart_icon.pay_by_check().click()
        # Confirm order
        self.cart_icon.confirm_order_element().click()
        # Assert that order is done
        self.assertEqual(self.cart_icon.order_complete_check().text, 'Your order on My Store is complete.')

    def test_search_null_value(self):
        # Begin flow by typing the value inside the search bar and press enter
        self.home.search_bar_flow('')
        # Assert that we get an appropriate message
        self.assertEqual(self.home.search_bar_error_element().text, "Please enter a search keyword")

    def test_price_slider_functionality(self):
        # Enter women category
        self.home.women().click()
        # Set a variable that holds the total number of items in the page
        total_items_before_applying_filter = self.item.raw_total_items()
        # Slide the slider in the left side to the right
        self.item.slider_left(40, 0)
        # Wait for the filter element to pop-up
        self.item.explicit_wait_for_filters_pop()
        # Set a variable that holds the total number of items in the page
        total_items_after_applying_filter = self.item.raw_total_items()
        # Assert that when sliding the slider to the right, we get less items shown to us
        self.assertNotEqual(total_items_before_applying_filter, total_items_after_applying_filter)

    # =========================== Testing Sort Functionality ===============================

    def test_sort_by_lowest_first(self):
        # Enter women category
        self.home.women().click()
        # Change to list view
        self.item.list_view().click()
        # Putting all of the prices in the original order inside a variable
        before_sorting = self.item.item_prices()
        # Sort items by price: lowest first
        self.item.sort_items('Price: Lowest first')
        # Sleeping for four seconds
        self.item.raw_wait(4)
        # Putting all of the prices in ascending order inside a variable
        after_sorting = self.item.item_prices()
        # Assert that the two price lists are different
        self.assertNotEqual(before_sorting, after_sorting)
        # Assert that the cheapest item in the sorted list is actually the cheapest item
        self.assertEqual(after_sorting[0], self.item.cheapest_item())

    def test_sort_by_highest_first(self):
        # Enter women category
        self.home.women().click()
        # Change to list view
        self.item.list_view().click()
        # Putting all of the prices in the original order inside a variable
        before_sorting = self.item.item_prices()
        # Sort items by price: lowest first
        self.item.sort_items('Price: Highest first')
        # Sleeping for four seconds
        self.item.raw_wait(4)
        # Putting all of the prices in ascending order inside a variable
        after_sorting = self.item.item_prices()
        # Assert that the two price lists are different
        self.assertNotEqual(before_sorting, after_sorting)
        # Assert that the cheapest item in the sorted list is actually the cheapest item
        self.assertEqual(after_sorting[0], self.item.most_expensive_item())
        # Assert that the last item is the cheapest item
        self.assertEqual(after_sorting[-1], self.item.cheapest_item())
        # BUG FOUND HERE - Sorting by lowest instead of highest first

    def test_sort_by_name_A_to_Z(self):
        # Enter women category
        self.home.women().click()
        # Change to list view
        self.item.list_view().click()
        # Sort items by price: lowest first
        before_sorting = self.item.item_names()
        # Sorting by A to Z
        self.item.sort_items('Product Name: A to Z')
        # Sleeping for three seconds
        self.item.raw_wait(3)
        # Putting all of the names inside a variable before sorting
        after_sorting = self.item.item_names()
        # Assert that the two price lists are different
        self.assertNotEqual(before_sorting, after_sorting)
        # Doing my own sort by A to Z to see that the first and last item are identical
        sorted_items = self.item.item_names_sorted_a_to_z()
        self.assertEqual(after_sorting[0], sorted_items[0])
        self.assertEqual(after_sorting[-1], sorted_items[-1])

    def test_sort_by_name_Z_to_A(self):
        # Enter women category
        self.home.women().click()
        # Change to list view
        self.item.list_view().click()
        # Sort items by price: lowest first
        before_sorting = self.item.item_names()
        # Sorting by A to Z
        self.item.sort_items('Product Name: Z to A')
        # Sleeping for three seconds
        self.item.raw_wait(3)
        # Putting all of the names inside a variable before sorting
        after_sorting = self.item.item_names()
        # Assert that the two price lists are different
        self.assertNotEqual(before_sorting, after_sorting)
        # Doing my own sort by A to Z to see that the first and last item are identical
        sorted_items = self.item.item_names_sorted_z_to_a()
        self.assertEqual(after_sorting[0], sorted_items[0])
        self.assertEqual(after_sorting[-1], sorted_items[-1])
        # Bug Found Here, sorting by A - Z instead Z - A

    def test_my_orders_check(self):
        """Make a transaction and check that we the order in my orders section"""
        # Click on sign in
        self.home.sign_in().click()
        # Sign in
        self.login.sign_in_flow('yantesting@testing.com', '123321ya')
        # Go to home Page
        self.home.site_logo().click()
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Click on the third item
        self.item.item_selection(0).click()
        # Click add to cart
        self.item.add_to_cart().click()
        # Wait until we can see the pop up msg
        self.item.wait_pop_up_msg()
        # Click on continue shopping once we see the pop up
        self.item.click_continue_shopping()
        # Hover on the cart
        self.cart_icon.hover_cart()
        # Click checkout
        self.cart_icon.checkout_button().click()
        # Proceed to checkout
        self.cart_icon.proceed_flow_valid()
        # Click "Pay by Bank Wire"
        self.cart_icon.pay_by_bank_wire().click()
        # Confirm order
        self.cart_icon.confirm_order_element().click()
        # Wait for order confirmation page to appear
        self.cart_icon.wait_for_order_completion()
        # Set the reference ID inside a variable
        reference = self.cart_icon.take_reference_from_order_completion()
        # Set the price inside a variable
        price = self.cart_icon.take_total_from_order_completion()
        # Set the chosen payment method inside a variable
        method = self.cart_icon.take_payment_method_from_order_completion()
        # Click on My Account
        self.home.account_name_when_logged_in().click()
        # Click on My Orders
        self.home.my_order().click()
        # Assert that the reference ID is correct inside the "My Orders" page
        self.assertEqual(reference, self.my_orders.order_reference_first_in_row().text)
        # Assert that the price is correct inside the "My Orders" page
        self.assertEqual(price, self.my_orders.order_price_first().text)
        # Assert that the method is correct inside the "My Orders" page
        self.assertEqual(method, self.my_orders.order_payment_method().text)
        # Assert that the date is correct
        self.assertEqual(self.today_format, self.my_orders.order_date_first().text)

    def test_wishlist_valid(self):
        # Click on sign in
        self.home.sign_in().click()
        # Sign in
        self.login.sign_in_flow('yantesting@testing.com', '123321ya')
        # Go to home Page
        self.home.site_logo().click()
        # Click on t_shirts category
        self.home.t_shirts().click()
        # Click on list view
        self.item.list_view().click()
        # Add the first item to the wishlist
        self.item.add_to_wishlist_from_catalog(0).click()
        # Press 'Close' on the pop-up message
        self.item.close_pop_up_wishlist().click()
        # Put the name of the item we put inside a wishlist inside a variable
        item_name = self.item.item_names_individual(0).text
        # Go to my account
        self.home.account_name_when_logged_in().click()
        # Go to wishlist
        self.home.wishlist().click()
        # Click on wishlist collection
        self.home.wishlist_collection().click()
        # Assert that the item we put inside the wishlist is there
        self.assertEqual(item_name, self.home.item_name_in_wishlist().text)

    def tearDown(self):
        self.driver.quit()
