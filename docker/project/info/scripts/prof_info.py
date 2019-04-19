import os
import sys

import django
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# Setting up environment
sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django):
    django.setup()


# Function returns the department and professor's webpages in one time
# Case 1: get lists of department
# Case 2: get lists of teacher
def get_url(driver, case):
    ans = []
    size_need = len("https://faculty.rpi.edu/departments")
    link = driver.find_elements_by_tag_name("a")  # get all urls in one time
    for n in link:
        try:
            try1 = n.get_attribute('href')
            if case == 1:
                # Assert the urls is correct
                if ("https://faculty.rpi.edu/departments" in try1 and len(
                        try1) > size_need and "main-content" not in try1):
                    # print try1
                    ans.append(try1)
            if case == 2:
                # Assert the urls is correct
                if "https://faculty.rpi.edu/" in try1 and "-" in try1 and "main-content" not in try1:
                    # print try1
                    ans.append(try1)
        except TypeError as e:
            # Fail to get the webpage
            print("ERROR: get_url unable to get attribute from {} ".format(n))
    driver.quit()
    return ans


def get_driver(url):
    """
    Function returns a webdriver object
    :param url: String
    :return: selenium drive
    """
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(url)
    return driver


# Function returns string of a given web page title
def get_name(driver):
    name = []
    try:
        n = driver.find_element_by_id("page-title")
        name.append(n.text)
        # print(name.text)
    except:
        print("get_name fail to get title text from {}".format(driver))
    return name


# Function returns all the text in input web page
def get_page(driver):
    ans = []
    im_word = driver.find_elements_by_class_name("view-content")
    for im in im_word:
        try:
            lang = im.text
            ans.append(lang.text)
        except:
            print("get_page fail to get title text from {}".format(driver))
    return ans


# Function returns the image address from given image
def get_image(driver):
    ans = []
    image = driver.find_elements_by_tag_name("img")

    for i in image:
        try2 = i.get_attribute('src')
        try:
            if "https://faculty.rpi.edu/" in try2: ans.append(try2)
        except:
            print("get_image fail to get image address from {}".format(driver))
    return ans


# Function returns text line from list of selector
def line(selector):
    """

    :param selector: List
    :return: List
    """
    ans = []
    for s in selector:
        try:
            ans.append(s.text)
        except:
            print("line unable to get test from input selector")
    return ans


# Function returns urls get from selector
def address(selector):
    ans = []
    for s in selector:
        try:
            x = s.get_attribute('href')
            ans.append(x)
        except:
            print("address unable to get address from input selector")
    return ans


# Wrapper function that collect all information from a single professor page
def get_people(url):
    try:
        driver = get_driver(url)
    except:
        return dict()

    ew = line(driver.find_elements_by_tag_name("a"))
    # print(ew)

    email = []
    for e in ew:
        if e.find("@") != -1:
            email.append(e)

    webpage = []
    for w in ew:
        if "http://" in w:
            webpage.append(w)

    td = line(driver.find_elements_by_css_selector(".views-field.views-field-field-title"))
    if len(td) > 0:
        retd = td[0].split(",")

    title = []
    department = []
    if len(retd) > 1:
        title.append(retd[0])
        for i in range(1, len(retd)):
            department.append(retd[i].replace(" ", ""))

    # Get required info from web page
    focus = line(driver.find_elements_by_css_selector(".views-field.views-field-field-focus-area"))
    education = line(driver.find_elements_by_css_selector(".views-field.views-field-field-education"))
    biography = line(driver.find_elements_by_css_selector(".views-field.views-field-field-biography"))

    # Assign info into dict
    page = dict()
    page["url"] = url
    page["name"] = get_name(driver)
    page["title"] = title
    page["department"] = department
    page["email"] = email
    page["web_page"] = webpage
    page["focus"] = focus
    page["education"] = education
    page["biography"] = biography
    page["image"] = get_image(driver)

    # Save to database
    from info.scripts.import_data import update_prof_info
    update_prof_info(page)
    driver.quit()
    return page


# Wrapper function that for crawling the whole RPI INFO page for professor information
def crawler_wrapper():
    name_list = []  # <-- list of all names

    try3 = get_url(get_driver("https://faculty.rpi.edu/"), 1)  # <-- list of all departments

    jump = 0

    for t in try3:
        if jump == 2:
            break
        try4 = get_url(get_driver(t), 2)
        for r in try4:
            name_list.append(r)
            # print(r)

    people_list = []
    for name in name_list:
        x = get_people(name)  # <-- list of dictionary of people
        people_list.append(x)

    return people_list


# Start the function
if __name__ == "__main__":

    json_list = crawler_wrapper()
    for j in json_list:
        print(j)
