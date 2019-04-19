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

    button_element = WebDriverWait(web, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, loc)))
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

#Assertation 

#------------------------------------------------------------------------------------#
def basic_assert(web,title_urls):

    print(web.title)
    print(web.current_url)

    #assertEquals(title_urls[0],web.title)
    #assertEquals(title_urls[0],web.current_urls)

def advance_assert(web,result):
    pass

#------------------------------------------------------------------------------------#
#global variable: dict [function][css selector]

loc = dict()
loc["search-button"] = ".btn"
loc["nav-bar"] = ".navbar > a:nth-child(1)"
loc["input-bar"] = "input.ng-pristine" 
loc["course-button"] = "li.nav-item:nth-child(1) > a:nth-child(1)"
loc["faculty-button"] = "li.nav-item:nth-child(2) > a:nth-child(1)"
loc["web"] = "http://www.worldpara.com:9000/"
loc["arb-web"] = "http://www.worldpara.com:9000/prof/Wes%20Turner/211"

def TC1(result):

    print("TC1")
    web = get_driver(loc["web"]) #preC
    
    #Sequences of action 


    select_(web,"CSCI")
    enter_(web,loc["input-bar"],"data structure")
    click_(web,loc["search-button"])

    basic_assert(web,result)

    web.close()

def TC2(result):
     
    print("TC2")
    web = get_driver(loc["web"]) #preC

    #Sequences of action I

    enter_(web,loc["input-bar"],"data")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.back()

    #Sequences of action II

    select_(web,"All departments")
    enter_(web,loc["input-bar"],"data")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.close()

def TC3(result):
    
    print("TC3")
    web = get_driver(loc["web"]) #preC

    #Sequences of action

    click_(web,loc["search-button"])

    basic_assert(web,result)

    web.close()

def TC4(result):

    print("TC4")
    web = get_driver(loc["web"]) #preC

    #Sequences of action 

    select_(web,"CISH or CSCI")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.close()

def TC5(result):


    print("TC5")
    web = get_driver(loc["web"]) #preC

    #Sequences of action 
    
    select_(web,"CISH or CSCI")
    enter_(web,loc["input-bar"],"abracadabra")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.close()

def TC6(result):

         
    print("TC6")
    web = get_driver(loc["web"]) #preC

    #Sequences of action 

    enter_(web,loc["input-bar"],"abracadabra")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.close()

def TC7(result):


    print("TC7")
    web = get_driver(loc["web"]) #preC

    #Prec to reach a result page

    select_(web,"CISH or CSCI")
    enter_(web,loc["input-bar"],"data")
    click_(web,loc["search-button"])
    basic_assert(web,"")

    click_(web,"div.row:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h5:nth-child(1)")
    basic_assert(web,result)

    web.close()

#fail time out
def TC8(result):

    print("TC8")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button") 

    select_(web,"CSCI")
    enter_(web,loc["input-bar"],"Wes Turner")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    web.close()



def TC9(result):

    print("TC9")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")
    
    select_(web,"CISH or CSCI")
    enter_(web,loc["input-bar"],"Wes")
    click_(web,loc["search-button"])
    basic_assert(web,result)
    
    web.close()
    

def TC10(result):

    print("TC10")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")
    
    select_(web,"CISH or CSCI")
    enter_(web,loc["input-bar"],"asfdfgh")
    click_(web,loc["search-button"])
    basic_assert(web,result)
    
    web.close()
    

def TC11(result):

    print("TC11")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")
    
    enter_(web,loc["input-bar"],"Wes Turner")
    click_(web,loc["search-button"])
    basic_assert(web,result)
    
    web.close()
    
def TC12(result):

    print("TC12")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")

    enter_(web,loc["input-bar"],"Wes")
    click_(web,loc["search-button"])
    basic_assert(web,result)
    
    web.close()

def TC13(result):

    print("TC13")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")

    enter_(web,loc["input-bar"],"qwewqrewt")
    click_(web,loc["search-button"])
    basic_assert(web,result)
    
    web.close()

def TC14(result):

    print("TC14")

    web = get_driver(loc["web"]) #preC

    #switch to profess page
    click_(web,"faculty-button")
    
    #reach search result 
    enter_(web,loc["input-bar"],"Wes Turner")
    click_(web,loc["search-button"])
    basic_assert(web,result)

    click_(web,"div.row:nth-child(2) > div:nth-child(1)") #can switch to check whole a href elements

    web.close()

def TC15(result):

    print("TC15")
    
    #preC
    web = get_driver(loc["prof-web"]) 
    web.close()

    #Wait for new function come to server


def TC16(result):

    print("TC16")
    
    #preC
    web = get_driver(loc["prof-web"])
    web.close()

    #Wait for new function come to server

def TC17(result):

    print("TC17")
    #preC
    web = get_driver(loc["arb-web"])
    #Sequence of actions
    click_(web,loc["nav-bar"])
    assert_basic(web,result)
    web.close()


def TC18(result):

    print("TC18")
    #preC
    web = get_driver(loc["arb-web"])
    #Sequence of actions
    click_(web,loc["course-button"])
    assert_basic(web,result)
    web.close()

def TC19(result):

    print("TC19")
    #preC
    web = get_driver(loc["arb-web"])
    #Sequence of actions
    click_(web,loc["faculty-button"])
    assert_basic(web,result)
    web.close()

TC9("")
TC10("")
TC11("")
