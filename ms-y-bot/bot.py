import time
import random
import datetime
import coloredlogs, logging

import numpy as numpy
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sched, time

logger = logging.getLogger(__name__)
coloredlogs.install(level="DEBUG", logger=logger)
scheduler = sched.scheduler(time.time, time.sleep)


def wait(minWaitTime, maxWatitime, operation_name):
    logger.debug("**** [NOT A BOT] buffering: {} ****".format(operation_name))
    time.sleep(random.choice(numpy.arange(minWaitTime, maxWatitime, 1)))


class Bot:
    def __init__(self, username, password):
        # self.driver = webdriver.Chrome("chromedriver")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.username = username
        self.password = password
        self.base_url = "https://www.instagram.com"
        self.app_start = datetime.datetime.now()
        self.to_scout = []

    def go_to_user(self, user):
        limit = 5
        while limit >= 0:
            time.sleep(1)
            try:
                self.driver.get("{}/{}/".format(self.base_url, user))
                limit -= 1
                wait(5, 10, "opened user profile: {}".format(user))
                return True
            except (TimeoutException, WebDriverException) as e:
                logger.error("cannot open user profile with reason = {}. Retry initiated.".format(e))
                return False




    def set_value_to_input_by_name(self, name, value):
        input = self.driver.find_element(By.NAME, name)
        input.send_keys(value)

    def login(self):
        logger.info("Logging In: {}".format(self.username))
        self.driver.get("{}/accounts/login".format(self.base_url))
        wait(2, 3, "opened login page")

        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Accept All')]").click()

        time.sleep(2)
        self.set_value_to_input_by_name("username", self.username)
        time.sleep(2)
        self.set_value_to_input_by_name("password", self.password)
        time.sleep(2)
        try:
            logger.debug("Waiting for login form to be clickable")
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.ID, "loginForm"))).click()
        except TimeoutException:
            logger.error("likely blocked by insta temporarily")


        # WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
        #     (By.XPATH, "//button[contains(text(), 'Allow All Cookies')]"))).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Not now')]"))).click()

        wait(2, 3, "logged in: {}".format(self.username))

    def find_accounts_to_follow(self, user):
        # go to users/followers
        logger.info("going to account {}".format(user))
        if not self.go_to_user(user):
            logger.error("cannot visit user profile: {}".format(user))
            # TODO
            return

        # followers = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "follower")))
        # waiter.find_element(self.driver, "//a[@href='/instagram/followers/']", XPATH).click()        # followers.click()

        # Wait for the followers modal to load
        logger.info("getting followers from user: {}".format(user))
        # waiter.find_element(self.driver, "//div[@role='dialog']", XPATH)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/followers')]"))).click()
        wait(3, 5, "clicked on followers pop up")
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
        logger.debug("account scrapped: {} ".format(names))
        self.to_scout = names
        return names

    def find_user_profile_element(self, by, identifier):
        try:
            return self.driver.find_element(by, identifier)
        except NoSuchElementException:
            return False

    def check_for_warning(self):
        if self.find_user_profile_element(By.XPATH,
                                          "(//*[contains(text(), 'Your Account Has Been Temporarily Locked')])") or \
                self.find_user_profile_element(By.XPATH, "(//*[contains(text(), 'Confirm it's you to log in')])"):
            logger.fatal("!!!!!!!!!!!!!!!!!warning received, do not process further!!!!!!!!!!!!!")
            self.driver.quit()
            return True
        logger.debug("no warning, safe to proceed")
        return False

    def get_time_elapsed(self):
        app_end = datetime.datetime.now()
        elapsed_time = app_end - self.app_start
        datetime.timedelta(0, 8, 562000)
        seconds_in_day = 24 * 60 * 60
        return divmod(elapsed_time.days * seconds_in_day + elapsed_time.seconds, 60)

    def follow_followers(self):
        follower_list = self.to_scout

        logger.info("Number of accounts to scout: {}".format(len(follower_list)))
        scheduler.enter(3600, 1, self.follow_followers)

        self.app_start = datetime.datetime.now()
        logger.info("new app run started: {}".format(self.app_start))

        followed = []
        failed_to_scout = []
        last_followed = " "
        temp = open("[Followed][{}]".format(self.username), "a+")
        temp.close()

        for username in follower_list:
            if not self.go_to_user(username):
                logger.error("cannot visit user profile: {}".format(username))
                failed_to_scout.append(username)
                pass

            self.check_for_warning()

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Requested')]"):
                logger.info("skipping: already requested.")
                time.sleep(2)
                continue

            if self.find_user_profile_element(By.XPATH, "//*[contains(text(), 'Follow Back')]"):
                logger.info("skipping: already following you.")
                time.sleep(2)
                continue

            try:
                self.driver.find_element(By.XPATH, "//*[contains(text(), 'This account is private')]")
                with open("[Followed][{}]".format(self.username), "r+") as flist:
                    lines = flist.readlines()
                    if username not in lines:
                        self.driver.find_element(By.XPATH, "(//button[contains(text(),'Follow')])").click()
                        if self.find_user_profile_element(By.XPATH, "(//*[contains(text(), 'Try again later')])"):
                            logger.fatal("!!!!! Temporarily blocked. Exiting Program: retry in a few hours. !!!!!!")
                            self.driver.quit()
                        flist.write(username+"\n")
                        followed.append(username)
                        if len(followed) == 30:
                            diff = self.get_time_elapsed()
                            logger.info("followed 30 account - waiting for the next run. Total time used for the current run: {} mins {}secs".format(diff[0], diff[1]))
                            last_followed = username
                            break
                    else:
                        logger.info("skipping: followed before. Not interested in Ms Y English :( ")
                wait(30, 90, "requested to follow {}".format(username))
                logger.info("followed {} accounts on this run so far".format(len(followed)))
            except NoSuchElementException or ElementClickInterceptedException:
                if self.find_user_profile_element(By.CSS_SELECTOR, "[aria-label='Following']"):
                    logger.info("skipping: you are already following this account")
                else:
                    marketed = self.like_first_six_pics(username, failed_to_scout)
                    if marketed:
                        wait(3, 30, "public account: liked recent photos")
                    else:
                        logger.info("skipping: unmarketable public account")
                pass

        logger.info("requested to follow the following accounts: {}".format(followed))
        logger.info("unable to scout the following accounts due to errors: {}".format(failed_to_scout))
        if len(failed_to_scout) > 0:
            logger.debug("appending users unable to scout back in to scout list for retry later.")
            self.to_scout.extend(failed_to_scout)
        diff = self.get_time_elapsed()
        logger.info("finsihing current run. Total time used: {} mins {}secs".format(diff[0], diff[1]))
        self.to_scout = follower_list[follower_list.index(last_followed) + 1:]
        logger.info("remaining number of accounts to scout: {}".format(len(self.to_scout)))

    def like_first_six_pics(self, user, failed_to_scout):
        images = self.driver.find_elements(By.XPATH, "//div[@class='eLAPa']")
        if len(images) == 0:
            logger.info("no post on public account")
            return False
        for i in range(0, 6 if len(images) >= 6 else len(images)):
            self.driver.execute_script("arguments[0].click();", images[i])
            time.sleep(2)
            #better XPATH
            try:
                like_button = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")))
                if not self.find_user_profile_element(By.CSS_SELECTOR, "[aria-label='Unlike']"):
                    like_button.click()
                else:
                    logger.info("already liked this account's photo recently. Account not interested in Ms Y :( ")
                    return False
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                wait(1, 5, "liked {} photo".format(i + 1))
            except TimeoutException:
                failed_to_scout.append(user)
                logger.error("like_button not found")
                return False
        return True


def start_job_for_day(bot):
    scheduler.enter(1, 1, bot.follow_followers, ())
    scheduler.run()


def scrap_and_follow(bot, target):
    bot.find_accounts_to_follow(target)
    start_job_for_day(bot)


def scrap_only(bot, target):
    bot.find_accounts_to_follow(target)


def follow_only(bot, list_name):
    bot.to_scout = list_name
    start_job_for_day(bot)


def main():
    print('''
                                   __  __      ____  ____  ______
                                   \ \/ /     / __ )/ __ \/_  __/
                                    \  /_____/ __  / / / / / /   
                                    / /_____/ /_/ / /_/ / / /    
                                   /_/     /_____/\____/ /_/                              
 
    ''')

    # my_bot = Bot("*", "*")
    # my_bot.login()

    # logger.info("app started at: ", my_bot.app_start)

    # scrap_and_follow(my_bot, "")
    # scrap_only(my_bot, "")
    # follow_only(my_bot, "")


if __name__ == "__main__":
    main()
