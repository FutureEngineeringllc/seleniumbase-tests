from seleniumbase import BaseCase
# https://domus.am/


class CartPage(BaseCase):

    add_to_cart_btn = "/html/body/div[10]/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div[2]"
    count_on_basket = '/html/body/header/div[2]/div[3]/div/div/span'
    cart_page_popup_btn = '/html/body/header/div[2]/div[3]/div'
    count_increment_btn = '/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/span[2]'
    count_in_cart = '/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/input'
    total_price = '/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/span/span'

# '//*[@id="swiper-wrapper-b2f7b85421e0b348"]/div[1]/div/div[2]/div[2]/div[2]'