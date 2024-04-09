from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open page
        self.open("https://www.saleeasy.org/contact/")

        # fill all fields
        self.send_keys('//*[@id="wpforms-13-field_1"]', "test@gmail.com")
        self.send_keys('//*[@id="wpforms-13-field_3"]', "test subject here")
        self.send_keys('//*[@id="wpforms-13-field_2"]', "some message to send")

        # click submit button
        self.click("#wpforms-submit-13")

        # verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly.", "/html/body/div/div[1]/div/div/main/article/div/div/section/div[2]/div[2]/div/section/div/div/div/div[2]/div/div/div/div/p")

        #  for ID - #
        #  for class - . 