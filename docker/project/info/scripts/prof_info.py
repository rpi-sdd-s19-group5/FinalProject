import os
import sys
import django
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
if 'setup' in dir(django):
    django.setup()


def get_url(driver, case):
    ans = []
    size_need = len("https://faculty.rpi.edu/departments")
    link = driver.find_elements_by_tag_name("a")
    for n in link:
        try:
            try1 = n.get_attribute('href')
            if case == 1:
                if ("https://faculty.rpi.edu/departments" in try1 and len(
                        try1) > size_need and "main-content" not in try1):
                    # print try1
                    ans.append(try1)
            if case == 2:
                if "https://faculty.rpi.edu/" in try1 and "-" in try1 and "main-content" not in try1:
                    # print try1
                    ans.append(try1)
        except TypeError as e:
            print("ERROR:None")
    driver.quit()
    return ans


def get_driver(url):
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(url)
    return driver


def get_name(driver):
    name = []
    try:
        n = driver.find_element_by_id("page-title")
        name.append(n.text)
        # print(name.text)
    except:
        print("?")
    return name


def get_page(driver):
    ans = []
    im_word = driver.find_elements_by_class_name("view-content")
    for im in im_word:
        try:
            lang = im.text
            ans.append(lang.text)
        except:
            print("failed")
    return ans


def get_image(driver):
    ans = []
    image = driver.find_elements_by_tag_name("img")

    for i in image:
        try2 = i.get_attribute('src')
        try:
            if "https://faculty.rpi.edu/" in try2: ans.append(try2)
        except:
            print("NO image")
    return ans


def extract(line, re):
    ans = []
    if re != "":
        for l in line:
            try:
                if re in line: ans.append(line.text)
            except:
                print("F")
    else:
        for _ in line:
            try:
                ans.append(line.text)
            except:
                print("F")
    return ans


def line(selector):
    ans = []
    for s in selector:
        try:
            ans.append(s.text)
        except:
            print("No")
    return ans


def address(selector):
    ans = []
    for s in selector:
        try:
            x = s.get_attribute('href')
            ans.append(x)
        except:
            print("No")
    return ans


def get_people(url):
    try:
        driver = get_driver(url)
    except:
        return dict()

    page = dict()
    words = get_page(driver)

    ew = line(driver.find_elements_by_tag_name("a"))
    # print(ew)

    email = []
    for e in ew:
        if (e.find("@") != -1): email.append(e)
    # print(email)

    webpage = []
    for w in ew:
        if ("http://" in w): webpage.append(w)
    # print(webpage)

    td = line(driver.find_elements_by_css_selector(".views-field.views-field-field-title"))
    if (len(td) > 0): retd = td[0].split(",")
    # print(retd)
    # retd = []
    # try:
    # retd = td.split(",")
    # except:
    # print("fail")

    title = []
    department = []
    if len(retd) > 1:
        title.append(retd[0])
        for i in range(1, len(retd)):
            department.append(retd[i].replace(" ", ""))
    # print(title)
    # print(department)

    focus = line(driver.find_elements_by_css_selector(".views-field.views-field-field-focus-area"))
    education = line(driver.find_elements_by_css_selector(".views-field.views-field-field-education"))
    biography = line(driver.find_elements_by_css_selector(".views-field.views-field-field-biography"))

    # print(focus)
    # print(education)
    # print(biography)

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


def crawler_wrapper():
    name_list = []  # <-- list of all names

    try3 = get_url(get_driver("https://faculty.rpi.edu/"), 1)  # <-- list of all departments

    jump = 0

    for t in try3:
        # print(t)
        # <--- uncommon will pull all list done
        # jump += 1
        if jump == 2: break
        try4 = get_url(get_driver(t), 2)
        for r in try4:
            name_list.append(r)
            # print(r)

    people_list = []
    for name in name_list:
        x = get_people(name)  # <-- list of dictionary of people
        people_list.append(x)

    return people_list


if __name__ == "__main__":

    json_list = crawler_wrapper()
    for j in json_list:
        print(j)
