import time
import random

import numpy as numpy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait(minWaitTime, maxWatitime, operation_name):
    print("**** [NOT A BOT] buffering: {} ****".format(operation_name))
    time.sleep(random.choice(numpy.arange(minWaitTime, maxWatitime, 0.1)))


class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("chromedriver")
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"

    def go_to_user(self, user):
        # Goes to a user's page
        self.driver.get("{}/{}/".format(self.base_url, user))
        wait(4, 5, "opened user profile: {}".format(user))

    def set_value_to_input_by_name(self, name, value):
        input = self.driver.find_element(By.NAME, name)
        input.send_keys(value)

    def login(self):
        print("Logging In: {}".format(self.username))
        self.driver.get("{}/accounts/login".format(self.base_url))
        wait(2, 3, "opened login page")

        print("Alert is present: {}", expected_conditions.alert_is_present())
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accept All')]").click()

        wait(1, 2, "closed cookies alert")
        self.set_value_to_input_by_name("username", self.username)
        wait(1, 2, "set username")
        self.set_value_to_input_by_name("password", self.password)
        wait(1, 2, "set password")
        print("Waiting for login form to be clickable")
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "loginForm"))).click()
        except TimeoutException:
            print("likely blocked by insta temporarily")


        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//button[contains(text(), 'Allow All Cookies')]"))).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Not now')]"))).click()

        wait(2, 3, "logged in: {}".format(self.username))

    def get_followers(self, user):
        # go to users/followers
        print("going to account {}".format(user))
        self.go_to_user(user)

        # followers = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "follower")))
        # waiter.find_element(self.driver, "//a[@href='/instagram/followers/']", XPATH).click()
        # followers.click()

        # Wait for the followers modal to load
        print("getting followers from user: ", user)
        # waiter.find_element(self.driver, "//div[@role='dialog']", XPATH)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))).click()
        wait(2, 3, "clicked on followers pop up")
        scroll_box = self.driver.find_element(By.CLASS_NAME, "isgrP")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            wait(1, 2, "scrolled down")
            ht = self.driver.execute_script('''
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            ''', scroll_box)
        links = scroll_box.find_elements(By.TAG_NAME, "a")
        names = [name.text for name in links if name.text != '']
        print("account scrapped: {} ".format(names))
        return names

    def find_user_profile_element(self, by, identifier):
        try:
            return self.driver.find_element(by, identifier)
        except NoSuchElementException:
            return False

    def follow_followers(self, follower_list):
        followed = []
        for username in follower_list:
            self.go_to_user(username)
            # follow_button = self.driver.find_element(By.CSS_SELECTOR, 'button')
            # button_text = follow_button.text.strip()
            # print("button text = ", button_text)

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Requested')]"):
                print("skipping: already requested.")
                continue

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Follow Back')]"):
                print("skipping: already following you.")
                continue

            try:
                self.driver.find_element(By.XPATH, "//*[contains(text(), 'This account is private')]")
                self.driver.find_element(By.XPATH, "(//button[contains(text(),'Follow')])").click()
                followed.append(username)
                wait(1, 60, "requested to follow {}".format(username))
            except NoSuchElementException:
                if self.find_user_profile_element(By.CSS_SELECTOR, "[aria-label='Following']"):
                    print("skipping: you are already following this account")
                else:
                    print("skipping: public account")
                pass

        print("requested to follow the following accounts: ", followed)

# Future feature:
# (1) unfollow accounts that do not follow back
# (2) keep a file that record accounts that are unfollowed through the app and
#     make sure future app run do not re-request following these accounts
# (3) like the first 9 pictures of public accounts
# (4) store account credential separately

def main():
    my_bot = Bot("*", "*")
    target_account = input("Which account do you want to scrape followers from? ")
    my_bot.login()
    target_followers = my_bot.get_followers(target_account)
    my_bot.follow_followers(target_followers)

if __name__ == "__main__":
    main()
