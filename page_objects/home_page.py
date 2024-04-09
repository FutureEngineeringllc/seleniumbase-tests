from seleniumbase import BaseCase


class HomePage(BaseCase):
    get_title = "Domus.am"
    logo_icon = ".logo_mob"
    get_started_btn = '//*[@id="home_sticky_ID_Link"]'
    heading_text = "h2"
    username = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    password = '//*[@id="loginForm"]/div/div[2]/div/label/input'


    def open_page(self):
        self.open("https://www.instagram.com/accounts/login/?hl=en")


    def log_in(self):
        self.add_text(self.username, "userone")
        self.add_text(self.password, "password")
        self.click('//*[@id="loginForm"]/div/div[3]/button')