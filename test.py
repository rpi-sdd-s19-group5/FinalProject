from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == "__main__":
    # Initial driver
    chrome = webdriver.Chrome()
    for num in range(1, 20):
        url = "http://catalog.rpi.edu/content.php?catoid=18&catoid=18&navoid=444&filter%5Bitem_type%5D=3&filter" \
              "%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(num) + "#acalog_template_course_filter"
        chrome.get(url)
        assert "Rensselaer" in chrome.title
        trs = chrome.find_elements_by_css_selector("table.table_default")[6].find_element_by_tag_name("tbody"). \
            find_elements_by_tag_name("tr")
        index = trs.pop()
        trs = trs[1:-1]
        for course_link in trs:
            # Open description
            a_tag = course_link.find_element_by_tag_name("a")
            # a_tag.click()
            try:
                # Wait for description by AJAX
                content = WebDriverWait(course_link, 10).until(
                    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.ajaxcourseindentfix"))
                )
                print(content.text)

            except TimeoutException as e:
                print("Elements not found")
                break

    # Close drive
    chrome.quit()
