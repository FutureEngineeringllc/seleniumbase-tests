from seleniumbase import BaseCase

class ShopPage(BaseCase):
    search_input = '//*[@id="chrome-search"]'
    search_btn = ".vjmVpyd" # class
    product_img = '//*[@id="product-203984649"]/a/div/div[1]/img'
    no_product_text = '//*[@id="chrome-app-container"]/section[1]/section/section/section/section/section/h2'

    def shop_page(self):
        self.open("https://www.asos.com/men/?ctaref=hp|gen|top|men")