import json
import threading
from typing import Dict
from multiprocessing import Process, pool, cpu_count
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyThread(threading.Thread):
    def __init__(self, num, dict):
        threading.Thread.__init__(self)
        self.num = num
        self.dict = dict

    def run(self):
        chrome = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        url = "http://catalog.rpi.edu/content.php?catoid=18&catoid=18&navoid=444&filter%5Bitem_type%5D=3&filter" \
              "%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(self.num) + "#acalog_template_course_filter"
        chrome.get(url)
        print(url)
        assert "Rensselaer" in chrome.title
        trs = chrome.find_elements_by_css_selector("table.table_default")[6].find_element_by_tag_name("tbody"). \
            find_elements_by_tag_name("tr")
        index = trs.pop()
        trs = trs[1:-1]
        for course_link in trs:
            # Open description
            a_tag = course_link.find_element_by_tag_name("a")
            a_tag.click()
            course: Dict[str, str] = {"title": "", "description": "", "prerequisites": "", "offered": "",
                                      "cross_listed": "",
                                      "credit_hours": ""}
            try:
                # Wait for description by AJAX

                content = WebDriverWait(course_link, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.ajaxcourseindentfix"))
                )
                course["title"] = content.find_element_by_tag_name("h3").text

                # Split by line and store into dict
                for line in content.text.split("\n")[1:]:
                    # Trim the line
                    line = line.strip()
                    # Ignore empty line
                    if line == "":
                        continue
                    if course["description"] == "":
                        course["description"] = line
                    elif "Prerequisites/Corequisites" in line:
                        course["prerequisites"] = line
                    elif "When Offered" in line:
                        course["offered"] = line
                    elif "Cross Listed" in line:
                        course["cross_listed"] = line
                    elif "Credit Hours" in line:
                        course["credit_hours"] = line
                threadLock.acquire()
                self.dict.append(course)
                threadLock.release()
                print("thread #" + str(self.num) + str(course))

            except TimeoutException as e:
                print("Elements not found")
                break
        chrome.quit()

if __name__ == "__main__":
    # course url

    #chrome = webdriver.Chrome()
    thread_count = 2
    #print("process count: " + str(process_count))
    courses_info = []
    processes = []
    threadLock = threading.Lock()
    for num in range(1, thread_count + 1):
        processes.append(MyThread(num, courses_info))
        processes[num-1].start()

    for num in range(0, thread_count):
        processes[num].join()

    # Close drive
    output = json.dumps(courses_info)
    with open("course_info.json", 'w') as outfile:
        json.dump(output, outfile, sort_keys=True, indent=4)


