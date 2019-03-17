import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#current just test statement for location, I will up load the full one within this week

#course url
url = "https://faculty.rpi.edu/departments/Cognitive-Science" #"https://faculty.rpi.edu/departments"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
driver.get(url)

#get link to each course page
#link = driver.find_elements_by_tag_name("a")
#for n in link:
    #try1 = n.get_attribute('href')
    #try:
        #if("https://faculty.rpi.edu/" in try1 and "-" in try1):print try1
    #except TypeError as e:
#print ("None")
    #drive.get(try1)


img = driver.get("https://faculty.rpi.edu/atsushi-akera")
image = driver.find_elements_by_class_name("field-content")
im_word = driver.find_elements_by_class_name("view-content")
im = driver.find_elements_by_tag_name("img")
name = driver.find_element_by_id("page-title")
print(name.text)
for i in im:
    try2 = i.get_attribute('src')
    print(try2)

for i in im_word:
    try:
        try3 = i.text
        print(try3)
    except: print("Np")






#sample for each course page
#web = "http://catalog.rpi.edu/preview_course_nopop.php?catoid=18&coid=34363"
#driver.get(web)
#data = driver.find_elements_by_id('gateway-toolbar-container')  #driver.find_elements_by_id('course_preview_title')
#for d in data:
    #print(d.text)

#still in determine the range to get the needed information 

#head_tale = driver.find_elements_by_class_name("block_content")
#content = driver.find_elements_by_css_selector("table.table_default")
#for c in content:
    #print(c.text)


#print(data)

