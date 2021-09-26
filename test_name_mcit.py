import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {
    "download.deafult_dictionary": r"./",
    "download.prompt_for_dpwnload": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
});

class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_name_title(self):
        driver = self.driver
        driver.get("https://montrealcollege.omnivox.ca/Login/Account/Login?L=ANG")
        self.assertIn("Omnivox - Montreal College of Information Technology",driver.title)
        name = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/a").text
        self.assertIn("Montreal College of Information Technology",name)
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()