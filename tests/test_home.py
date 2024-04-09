from page_objects.home_page import HomePage

hp = HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("running before each test")

        # login
        self.open_page()
        self.log_in()

    def tearDown(self):
        print("running after each test")
        super().tearDown()

    def test_home_page(self):
        # open home page
        #  self.open("https://picsart.com/")

        # assert page title
        self.assert_title(hp.get_title)

        # assert title
        self.assert_element(hp.logo_icon)

        # click on the get started button and assert the url
        self.click(hp.get_started_btn)

        #my_profile = self.get_current_url()
        #self.assert_equal(my_profile, "https://picsart.com/create/editor?category=uploads")
        #self.assert_true("editor?category=uploads" in my_profile)

        # get the text of the url and assert the value
        self.assert_text("About our cookies", hp.heading_text)

        # Exercise: scroll to bottom and assert the copyright text

        #bottom - grid - aside - 0 - 2 - 716 right


        #print(self.get_text("/html/body/div[1]/main/div/div[3]/div/div/div/footer/section[2]/div/div/div[3]/strong"))
        #  self.assert_text("© 2024 Picsart, Inc.", "/html/body/div[1]/main/div/div[3]/div/div/div/footer/section[2]/div/div/div[3]/strong")


    def test_menu_links(self):
        # open url
        self.open("https://www.saleeasy.org/")

        expected_links = ["HOME", "ALL PRODUCTS", "ABOUT", "CONTACT", "ACCOUNT", "", "", "MY ACCOUNT", "STORE LIST"]

        # find menu links elements
        # //*[starts-with(@id, 'menu-item')]
        # li[id*=menu-item-]
        menu_links_el = self.find_elements("//*[starts-with(@id, 'menu-item')]")

        # loop through our menu links
        for idx, link_element in enumerate(menu_links_el):
            #print(idx, link_element.text)
            self.assert_equal(expected_links[idx], link_element.text)