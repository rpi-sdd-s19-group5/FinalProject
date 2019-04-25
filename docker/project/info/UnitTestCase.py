import os
import sys

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'

#Open the website in a CHROM broswer remote
def get_driver(url):
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(url)
    return driver


#Three basic operation#
#-------------------------------------------------------------------------------------#

def enter_(web,loc,data):

    #input_element = web.find_by_css_selector(loc)
    input_element =  WebDriverWait(web, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, loc)))
    input_element.send_keys(data)

def click_(web,loc):

    button_element = WebDriverWait(web, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, loc)))
    button_element.click()


def select_(web,data):

    for i in range(1,42):
        loc = "select.ng-valid > option:nth-child({})".format(i)
        bar = web.find_element_by_css_selector(loc)
        if(bar.text == data):
            bar.click()
            return
        bar = web.find_element_by_css_selector("select.ng-valid > option:nth-child(1)")
        bar.click()

#-------------------------------------------------------------------------------------#

#global vairable loc

loc = Dict()
loc["search-button"] = ".btn"
loc["nav-bar"] = ".navbar > a:nth-child(1)"
loc["input-bar"] = "input.ng-pristine"
loc["course-button"] = "li.nav-item:nth-child(1) > a:nth-child(1)"
loc["faculty-button"] = "li.nav-item:nth-child(2) > a:nth-child(1)"
loc["web"] = "http://www.worldpara.com:9000/"
loc["arb-web"] = "http://www.worldpara.com:9000/prof/Wes%20Turner/211"

#Assertation 

#------------------------------------------------------------------------------------#
def basic_assert(web,title_urls):

    print(web.title)
    print(web.current_url)

    #assertEquals(title_urls[0],web.title)
    #assertEquals(title_urls[0],web.current_urls)
#-------------------------------------------------------------------------------------#


def SearchCourse(dept=None,data=None,result):

    
    web = get_driver(loc["web"]) #preC

    #Sequences of action

    if(dept is not None):select_(web,dept)
    if(dara is not None):enter_(web,loc["input-bar"],"data structure")
    click_(loc["search-button"])

    basic_assert(web,result)

    web.close()


def SearchFaculty(dept=None,name=None,result):

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")

    if(dept is not None):select_(web,dept)
    if(name is not None):enter_(web,loc["input-bar"],name)
    click_(loc["search-button"])
    basic_assert(web,result)

    web.close()


def Pagination(number=None,action=None,result):
    pass

def DetailPage(Type,result):
    

    web = get_driver(loc["list-web"]) #preC

    #switch to profess page

    click_(web,get_url(web)[0])
    basic_assert(web,"")

    web.close()



if _name_ == _main_:

    #Search course group
    
    #01
    SearchCourse(dept="CISH or CSCI",data="data structure",CourseResult[1])
    #02
    SearchCourse(dept="PHYS",data="@#$$%v",CourseResult[2])
    #03
    SearchCourse(dept="PHYS",data="data structure",CourseResult[3])
    #04
    SearchCourse(dept="MAME",CourseResult[4])
    #05
    SearchCourse(data="algorithm",CourseResult[5])
    #06
    SearchCourse(CourseResult[6])
    
    #Search faculty group
    
    #01
    SearchFaculty(dept="MTLE",name="Shi",FacultyResult[1])
    #02
    SearchFaculty(dept="CHEM",name="@#%$%^&",FacultyResult[2])
    #03
    SearchFaculty(dept="CHEM",name="Chuck Stewart",FacultyResult[3])
    #04
    SearchFaculty(dept="CHEM",FacultyResult[4])
    #05
    SearchFaculty(name="Xia",FacultyResult[5])
    #06
    SearchFaculty(FacultyResult[6])

    #Pagination
    #01
    #02
    #03
    #04
    #05
    #06

    #Detail page
    #01
    #02
