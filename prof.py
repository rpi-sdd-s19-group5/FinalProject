import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(url):
    
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
    driver.get(url)

    return driver 



def get_url(driver,case):
    
    ans = []
    size_need = len("https://faculty.rpi.edu/departments")
    link = driver.find_elements_by_tag_name("a")
    for n in link:
        try:
            try1 = n.get_attribute('href')
            if(case == 1):
                if("https://faculty.rpi.edu/departments" in try1 and len(try1) > size_need and "main-content" not in try1):
                    print try1
                    ans.append(try1)
            if(case == 2):
                if("https://faculty.rpi.edu/" in try1 and "-" in try1 and "main-content" not in try1):
                    print try1
                    ans.append(try1)
        except TypeError as e:
            print ("None")

    return ans
def get_name(url):
    
    name = ""
    driver = get_driver(url)
    try:
        name = driver.find_element_by_id("page-title")
        print(name.text)
    except:
        print("?")
    return name.text

def get_page(url):

    ans = []
    driver = get_driver(url)
    im_word = driver.find_elements_by_class_name("view-content")
    for im in im_word:
        try:
            lang = im.text
            ans.append(lang)
        except:
            print "failed"
    return ans

def get_picture(url):

    ans = ""
    driver = get_driver(url);
    image = driver.find_elements_by_tag_name("img")

    for i in im:
        try2 = i.get_attribute('src')
        try:
            if("https://faculty.rpi.edu/" in try2):return try2
        except:
            print("NO image")



url = "https://faculty.rpi.edu/departments"
loc = get_driver(url)
look = get_url(loc,1)
for l in range(2):
    try:
        x = get_driver(look[l])
        people = get_url(x,2)
        print(get_page(people[1]))
    except: print("None")
