from selenium import webdriver
from bs4 import BeautifulSoup
import platform
from os import getcwd
from selenium.common.exceptions import NoSuchElementException
import re

if (platform.system() == 'Windows'):
    browser = webdriver.PhantomJS(executable_path=getcwd() + "\phantomjs")
if (platform.system() == 'Darwin' or platform.system() == 'Linux' ):
    browser = webdriver.PhantomJS(executable_path=getcwd() + "/phantomjs")


URL = input("Please enter the URL: ")
x = re.search("^https://www.instructables.com", URL)

# -----------------------------
def scrape():
    if x:
        browser.get(URL)
        page = BeautifulSoup(browser.page_source, "html5lib")

        print("\nScraped URL: " + URL)
        try:
            header = browser.find_element_by_xpath('//*[@id="article"]/header/h1').text
            print("Header Title: " + header)
        except NoSuchElementException:
            print("Header Title: N/A")

        try:
            views = browser.find_element_by_xpath("//*[@id='article']/header/div[1]/div[2]/p[1]").text
            print("Views Count: " + views)
        except NoSuchElementException:
            print("Views Count: N/A")
        try:
            heart = browser.find_element_by_xpath('//*[@id="article"]/header/div[1]/div[2]/p[2]').text
            print("Favourite Count: " + heart)
        except NoSuchElementException:
            print("Favourite Count: N/A")
        try:
            comment = browser.find_element_by_xpath('//*[@class="svg-comments active comment-count"]').text
            print("Comment Count: " + comment + "\n")
        except NoSuchElementException:
            print("Comment Count: N/A" + "\n")

        try:
            Supplies = browser.find_element_by_xpath('//*[@class="supplies-heading"]').text
            print(Supplies)

            try:
                ul = browser.find_element_by_xpath('//*[@id="intro"]/div[3]/ul')
                items = ul.find_elements_by_tag_name("li")
                for item in items:
                    text = item.text
                    print(text)
            except:
                step_body = browser.find_element_by_xpath('//*[@class="step-body"]')
                items = step_body.find_elements_by_tag_name("p")
                for item in items:
                    text = item.text
                    print(text)

        except NoSuchElementException:
            pass

        print('\n')

        tags = page.findAll("h2", {"class": "step-title"})
        for tag in tags:
            print(tag.getText())

        try:
            iframe = browser.find_element_by_tag_name("iframe")
            browser.switch_to.default_content()
            browser.switch_to.frame(iframe)
            iframe_source = browser.page_source
            print("Youtube URL: " + browser.current_url)
        except NoSuchElementException:
            pass

        browser.close()
    else:
        print("Only takes URLs from instructables.com")
        exit()
scrape()