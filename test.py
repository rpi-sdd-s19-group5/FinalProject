import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#current just test statement for location, I will up load the full one within this week

#course url
url = "http://catalog.rpi.edu/content.php?catoid=18&navoid=444"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
driver.get(url)

#get link to each course page
link = driver.find_elements_by_tag_name("a")

#for n in link:
    #try1 = n.get_attribute('href')
    #print try1
    #drive.get(try1)

#sample for each course page
web = "http://catalog.rpi.edu/preview_course_nopop.php?catoid=18&coid=34363"
driver.get(web)
data = driver.find_elements_by_id('course_preview_title')
for d in data:
    print(d.text)

#still in determine the range to get the needed information 

#content = driver.find_elements_by_class_name("block_content")
content = driver.find_elements_by_css_selector("table.table_default")
for c in content:
    print(c.text)

print(data)

