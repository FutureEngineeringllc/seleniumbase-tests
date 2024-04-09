from seleniumbase.common.exceptions import NoSuchElementException
from page_objects.shop_page import ShopPage


class ShopTest(ShopPage):
    def test_search_products(self):
        # open page
        self.open("https://www.asos.com/")
        self.shop_page()
# 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
        # take screenshot
        self.save_screenshot("empty_contact_from", "custom_screenshot")

        # search for product
        self.send_keys(self.search_input, "asdfadsfadfasdf")
        self.click(self.search_btn)

        # assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException:
            self.assert_text("NOTHING MATCHES YOUR SEARCH", self.no_product_text)


