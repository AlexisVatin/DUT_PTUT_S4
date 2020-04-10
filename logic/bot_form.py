from selenium import webdriver
import time
import os


class Bot():
    urlJustin = "http://justin-ozannat.alwaysdata.net/"
    urlCoco = "http://corentin-plee.alwaysdata.net/projetptut.html"
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        self.driver = webdriver.Chrome(os.path.join(self.BASE_DIR, 'drivers', 'chromedriver.exe'))

    def execForm(self, french_word, translated_word):
        self.driver.get(self.urlCoco)
        self.driver.find_element_by_id("addNew").click()
        time.sleep(2)
        self.driver.find_element_by_id("french_word").send_keys(french_word)
        time.sleep(2)
        self.driver.find_element_by_id("translated_word").send_keys(translated_word)
        time.sleep(2)
        self.driver.find_element_by_id("manageBtn").click()
        time.sleep(2)
        self.driver.quit()

    def execute(self):
        self.driver.get(self.urlJustin)
