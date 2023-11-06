# Import all required modules and libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
import time

# Get use data
    # Code to be updated

# Declare Constants
PROMISED_UP = 10
PROMISED_DOWN = 27
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWWORD"
# No twitter account? Create one here https://twitter.com/


class InternetSpeedTwitterBot:
    # This is a bot responsible for monitoring your internet speed and making a complaint when necessary
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.down = 0
        self.up = 0

    # @staticmethod
    # find_element_by

    def get_internet_speed(self):
        """Checks your internet speed"""
        pass
        # Launch browser
        self.driver.set_page_load_timeout(360)
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(7)

        # Accept cookies
        cookies = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookies.click()
        time.sleep(3)

        # Start speed test
        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go.click()

        # Get data
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        down_speed_div = self.driver.find_element(By.XPATH, value="//*[@title='Receiving Time']")
        up_speed_div = self.driver.find_element(By.XPATH, value="//*[@title='Sending Time']")
        down_speed = down_speed_div.find_element(By.CLASS_NAME, value="result-data-large")
        up_speed = up_speed_div.find_element(By.CLASS_NAME, value="result-data-large")
        # print(down_speed.get_attribute("outerHTML"))
        # print(up_speed.get_attribute("innerHTML"))
        # print("Up: text", up_speed.text, "get attr", up_speed.get_attribute("text"))
        # print("Down: text", down_speed.text, "get attr", down_speed.get_attribute("text"))
        self.down = down_speed.text
        self.up = up_speed.text
        # print("down:", self.down, '\n', "up:", self.up)

    def tweet_at_provider(self):
        """Logs a complaint at your internet service provider on twitter"""
        # Log in to twitter account
        self.driver.get(url="https://twitter.com/i/flow/login")
        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.NAME, "text")))
        email_input = self.driver.find_element(By.NAME, value="text")
        email_input.send_keys(TWITTER_EMAIL)
        # spans = self.driver.find_elements(By.TAG_NAME, "span")
        next_button = self.driver.find_element(By.XPATH, "//*[text() = 'Next']")
        # for span in spans:
        #     if span.text == "Next":
        #         next_button = span
        next_button.click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'number')]")
            phone_number = self.driver.find_element(By.NAME, value="text")
            phone_number.send_keys("YOUR PHONE NUMBER")
            next_button = self.driver.find_element(By.XPATH, value="//*[contains(text(), 'Next')]")
            next_button.click()
            time.sleep(5)
        except EC.NoSuchElementException:
            pass
        password_entry = self.driver.find_element(By.NAME, value="password")
        password_entry.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value="//*[text() = 'Log in']")
        # print("lalal")
        # print(login_button.get_attribute("outerHTML"))
        # print(login_button.get_attribute("innerHTML"))
        login_button.click()

        # Create tweet
        tweet = f"Hey, @webprovider, why is my internet speed {self.down}down/{self.up}up" \
                f" when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        time.sleep(5)
        text_box = self.driver.find_element(By.XPATH, value="//*[@role='textbox']")
        text_box = text_box.find_element(By.TAG_NAME, value="span")
        text_box.send_keys(tweet)
        post_button = self.driver.find_element(By.XPATH, "//*[text() = 'Post']")
        # print("lilal")
        # print(post_button.get_attribute("outerHTML"))
        # print(post_button.get_attribute("innerHTML"))
        
        # Post tweet
        post_button.click()


net_speed_bot = InternetSpeedTwitterBot()
net_speed_bot.get_internet_speed()
net_speed_bot.tweet_at_provider()
