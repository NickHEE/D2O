from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.common.exceptions import NoSuchElementException

d2l = 'https://learn.bcit.ca/'
ID = ''
Password = ''


# Login to D2l
browser = webdriver.Chrome()
browser.get(d2l)
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
username.send_keys(ID)
password.send_keys(Password)
password.send_keys(Keys.ENTER)
courses = ui.WebDriverWait(browser, 10).until(
    lambda b: b.find_elements_by_css_selector('.course-text.style-scope.d2l-course-image-tile'))

for course in courses:
    print(course.text)
    course.click()
    elem = browser.find_element_by_link_text('Content')
    elem.click()
    contentItems = browser.find_elements_by_css_selector('.d2l-datalist-item-content')
    for item in contentItems:
        title = item.find_element_by_xpath(r'.//a[@class="d2l-link"]')
        try:
            item.find_element_by_xpath(r'.//img[@alt="Task: View this topic"]')
            print(f"Found new content - {title.text}")
            dropMenu = item.find_element_by_xpath(r'.//a[@role="button"]')
            dropMenu.click()
            #time.sleep(0.5)
            #item.find_element_by_xpath('.//span[text()="Download"]').click()
        except NoSuchElementException:
            print(f"Found old content - {title.text}")
    browser.get('https://learn.bcit.ca/d2l/home/')


    time.sleep(10)




