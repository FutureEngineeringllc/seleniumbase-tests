import time
from page_objects.cart_page import CartPage


class CartTest(CartPage):

    def setUp(self):
        super().setUp()
        self.open("https://domus.am/")

    def test_add_to_cart(self):
        # add item to the cart
        self.click(self.add_to_cart_btn)

        # assert product is added to the cart
        self.assert_text("1", self.count_on_basket)

        # open cart page
        self.click(self.cart_page_popup_btn)

        # get current subtotal
        text_first = self.get_text(self.total_price)

        # change cart quantity
        self.click(self.count_increment_btn)

        #time.sleep(5)  - first method (bad practice)

        self.wait_for_text("799 800", self.total_price)  # - second method (preferable)

        # assert subtotal to be different than the original
        text_second = self.get_text(self.total_price)
        self.assert_not_equal(text_first, text_second)

