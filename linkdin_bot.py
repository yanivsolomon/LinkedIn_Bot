from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# This file contains the following steps:
# 1. Open Linkedin.com.
# 2. Log in.
# 3. Search for "recruiters" to add.
# 4. If they are available to add, click and confirm, if not, go to next page.

# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_login(test_setup):
# fetch linkdin.com
    driver.get("https://www.linkedin.com/")
    time.sleep(3)
# log in
    driver.find_element_by_id("session_key").send_keys("our_email@gmail.com")
    driver.find_element_by_id("session_password").send_keys("our_password")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)
# search for "recruiter" and click enter, then click on "people".
    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("recruiter")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element_by_xpath("//button[@aria-pressed='false'][normalize-space()='People']").click()
    time.sleep(5)


# click on "Connect", then "Send Now" loop (when no more available, click "Next Page")
    while 1 > 0:
        try:
            elem = driver.find_element_by_xpath("//span[text()='Connect']")
            elem.click()
            time.sleep(2)
            driver.find_element_by_xpath("//button[@aria-label='Send now']").click()
            time.sleep(3)
        except NoSuchElementException:
            # Scroll to the bottom of the page and click next page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            next_page = driver.find_element_by_xpath("//button[@aria-label='Next']")
            next_page.click()
            time.sleep(3)



