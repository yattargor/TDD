from selenium import webdriver
import unittest

#TEST ARE ORGANIZED INTO CLASS INHEREDIT FROM UNITTEST.TESTCASE
class NewVisitorTest(unittest.TestCase):

    #THESE ARE SPECIAL METHODS RUN BEFORE AND AFTER TEST
    def setUp(self):
        self.browser = webdriver.Firefox()       #CREATE INSTANCE TO OPEN FIREFOX

    def tearDown(self):
        self.browser.quit()

    #MAIN BODY OF TEST(ALAWAYS METHOD INITIAL WITH test WILL BE RUN BY TEST RUNNER)
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        [...rest of comments as before]

if __name__='__main__':
    unittest.main(warnings='ignore')
