from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        # open the page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = "/Users/vardanmikayelyan/Documents/IMG_2018.jpg"

        # upload file
        self.choose_file("#file-upload", file_path)

        # click the upload button
        self.click("#file-submit")

        # assert file upolad text
        self.assert_text("File Uploaded!", "h3")