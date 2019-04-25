from django.test import TestCase

from info.models import CourseInfo, ProfInfo

import os
import sys
import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimpleTestCase(TestCase):
    # this test case tests searching in a specific department with a keyword
    def test_CourseSearchInDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="FFFF", course_code="FFFF 0001",
            description="This is another test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        # there is only one course that has the keyword "abracadabra" in dept "TEST"
        search_result = CourseInfo.search_course_tool("abracadabra", "TEST")
        self.assertEqual(len(search_result), 1)
        # there is only one course that has the keyword "abracadabra" in dept "FFFF"
        search_result = CourseInfo.search_course_tool("abracadabra", "FFFF")
        self.assertEqual(len(search_result), 1)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    # This test case tests searching in all departments with a keyword
    def test_CourseSearchAllDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="FFFF", course_code="FFFF 0001",
            description="This is another test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        # there are two courses that have the keyword "abracadabra"
        search_result = CourseInfo.search_course_tool("abracadabra", "ALL")
        self.assertEqual(len(search_result), 2)
        # there is only one course that has the keyword "jakads"
        search_result = CourseInfo.search_course_tool("jakads", "ALL")
        self.assertEqual(len(search_result), 1)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    # this test case tests searching in a specific department w/o keyword
    def test_NoKeyWordInDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="AAAA", course_code="AAAA 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 3", dept="BBBB", course_code="BBBB 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 4", dept="TEST", course_code="TEST 0002", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        # there are two courses in dept "TEST"
        search_result = CourseInfo.search_course_tool("", "TEST")
        self.assertEqual(len(search_result), 2)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    def test_NoKeyWordAllDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="AAAA", course_code="AAAA 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 3", dept="BBBB", course_code="BBBB 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 4", dept="TEST", course_code="TEST 0002", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        # there are 4 courses in total
        search_result = CourseInfo.search_course_tool("", "ALL")
        self.assertEqual(len(search_result), 4)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    def test_NoResultInDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="AAAA", course_code="AAAA 0001",
            description="This is a test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 3", dept="BBBB", course_code="BBBB 0001",
            description="This is a test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 4", dept="TEST", course_code="TEST 0002", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        search_result = CourseInfo.search_course_tool("jakads", "TEST")
        # no courses w/ keyword "jakads" in dept "TEST"
        self.assertEqual(len(search_result), 0)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    # this test case tests when there are no matching results among all departments
    def test_NoResultInAllDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="AAAA", course_code="AAAA 0001",
            description="This is a test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 3", dept="BBBB", course_code="BBBB 0001",
            description="This is a test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 4", dept="TEST", course_code="TEST 0002", description="This is a test abracadabra",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        search_result = CourseInfo.search_course_tool("no result lel", "ALL")
        # no courses w/ keyword "no result lel"
        self.assertEqual(len(search_result), 0)
        CourseInfo.objects.filter(cross_listed="Delete me").delete()

    # this test case tests when there are matching resultss
    def test_SearchProf(self):
        ProfInfo.objects.all().delete()
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="John Doe", title="Prof", dept="TEST", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="Uncle Tony", title="Prof", dept="AAAA", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="Uncle Johnny", title="Prof", dept="AAAA", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        search_result = ProfInfo.search_prof_tool("John")
        # 2 results matching the keyword "John"
        self.assertEqual(len(search_result), 2)
        search_result = ProfInfo.search_prof_tool("Tony")
        # 1 result matching the keyword "Tony"
        self.assertEqual(len(search_result), 1)
        ProfInfo.objects.all().delete()

    # this test case tests searching professors w/o a keyword
    def test_SearchProfWOKeyWord(self):
        ProfInfo.objects.all().delete()
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="John Doe", title="Prof", dept="TEST", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="Uncle Tony", title="Prof", dept="AAAA", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        ProfInfo.objects.update_or_create(
            url="http://this.url", name="Uncle Johnny", title="Prof", dept="AAAA", email="jd@jd.com", web_page="jd.com",
            focus="N/A",
            education="kindergarten",
            biography="N/A", image="N/A"
        )
        search_result = ProfInfo.search_prof_tool("")
        # there are 3 results in total
        self.assertEqual(len(search_result), 3)
        ProfInfo.objects.all().delete()

sys.path.append("/src")
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest.settings'
def get_driver(url):
    driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub',
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
    
    button_element = web.find_element_by_css_selector(loc)#WebDriverWait(web, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, loc)))
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

class FrontendTestCase(TestCase):
    
   def test_PushButton(self):
    
        web = get_driver("http://djangosdd:8080/") #preC
        #print(web.current_url,": ",web.title)
        #x = web.find_element_by_xpath("/html/body")
        #print(x.text)
        
        loc = dict()
        loc["search-button"] = ".btn"
        loc["nav-bar"] = ".navbar > a:nth-child(1)"
        loc["input-bar"] = "input.ng-pristine"
        loc["course-button"] = "li.nav-item:nth-child(1) > a:nth-child(1)"
        loc["faculty-button"] = "li.nav-item:nth-child(2) > a:nth-child(1)"
        
        r0 = dict()
        r0["title"] = "RPI Advanced Academic Catalog"
        r0["url"] = "http://djangosdd:8080/"
        
        r1 = dict()
        r1["title"] = "RPI Advanced Academic Catalog"
        r1["url"] ="http://djangosdd:8080/search_course?dept=string%3AAll+Departments&search_content="

        r2 = dict()
        r2["title"] = "RPI Advanced Academic Catalog - Prof"
        r2["url"] ="http://djangosdd:8080/prof"

        #Sequences of action

        #check search button
        click_(web,loc["search-button"])
        self.assertEqual(r1["title"],web.title)
        self.assertEqual(r1["url"],web.current_url)


        #check course button
        click_(web,loc["course-button"])
        self.assertEqual(r0["title"],web.title)
        self.assertEqual(r0["url"],web.current_url)

        #check faculty button
        click_(web,loc["faculty-button"])
        self.assertEqual(r2["title"],web.title)
        self.assertEqual(r2["url"],web.current_url)

        #check navgation button 
        click_(web,loc["nav-bar"])
        self.assertEqual(r0["title"],web.title)
        self.assertEqual(r0["url"],web.current_url)
        print("Button test passed") 
        web.close()
        
   def test_Pagination(self):
        
        loc = dict()
        loc["next"] = "a.active:nth-child(6)"
        loc["prev"] = "a.active:nth-child(3)"
        loc["first"] = "li.page-item:nth-child(2) > a:nth-child(1)"
        loc["last"] = "a.active:nth-child(7)"
        loc["num"] = "li.active:nth-child(5) > a:nth-child(1)"
        
        r0 = dict()
        r0["title"] = "RPI Advanced Academic Catalog"
        r0["url"] ="http://djangosdd:8080/search_course?dept=string%3AAll+Departments&search_content="

        r1 = dict()
        r1["title"] = "RPI Advanced Academic Catalog"
        r1["url"] ="http://djangosdd:8080/search_course?page=1&dept=string%3AAll+Departments&search_content="

        r2 = dict()
        r2["title"] = "RPI Advanced Academic Catalog"
        r2["url"] ="http://djangosdd:8080/search_course?page=2&dept=string%3AAll+Departments&search_content="
        
        
        r3 = dict()
        r3["title"] = "RPI Advanced Academic Catalog"
        r3["url"] ="http://djangosdd:8080/search_course?page=3&dept=string%3AAll+Departments&search_content="
        
        r4 = dict()
        r4["title"] = "RPI Advanced Academic Catalog"
        r4["url"] ="http://djangosdd:8080/search_course?page=4&dept=string%3AAll+Departments&search_content="


        CourseInfo.objects.all().delete()

        #generate data needs
        for i in range(35):
            
            CourseInfo.objects.update_or_create(
                    title="Test{}".format(i), dept="ECSE", course_code="TEST 0001", description="This is {}th test abracadabra".format(i),prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
            )
        
        search_result = CourseInfo.search_course_tool("", "Test1")
        print(len(search_result))
        search_result = CourseInfo.search_course_tool("", "ALL")
        print(len(search_result))

        #PreC
        time.sleep(10)
        web = get_driver("http://djangosdd:8080/search_course?dept=string%3AAll+Departments&search_content=")

        #Sequence of action
        
        #page 2

        elements = WebDriverWait(web, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        #print(elements.text)
        click_(web,loc["num"])
        self.assertEqual(web.title,r2["title"])
        self.assertEqual(web.current_url,r2["url"])

        #prev
        click_(web,loc["prev"])
        self.assertEqual(web.title,r1["title"])
        self.assertEqual(web.current_url,r1["url"])

        #next
        click_(web,loc["next"])
        self.assertEqual(web.title,r2["title"])
        self.assertEqual(web.current_url,r2["url"])

        #first
        click_(web,loc["first"])
        self.assertEqual(web.title,r1["title"])
        self.assertEqual(web.current_url,r1["url"])

        #last
        click_(web,loc["last"])
        self.assertEqual(web.title,r4["title"])
        self.assertEqual(web.current_url,r4["url"])

        CourseInfo.objects.all().delete()
        web.close()

