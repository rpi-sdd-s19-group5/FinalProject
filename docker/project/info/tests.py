from django.test import TestCase
from info.models import CourseInfo, ProfInfo
from info.search_test import search_course_tool


class SimpleTestCase(TestCase):
    # this test case tests searching in a specific department with a keyword
    def test_CourseSearchInDept(self):
        CourseInfo.objects.all().delete()
        CourseInfo.objects.update_or_create(
            title="Test Course 1", dept="TEST", course_code="TEST 0001", description="This is a test abracadabra", prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 2", dept="FFFF", course_code="FFFF 0001", description="This is another test abracadabra jakads",
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

    #this test case tests searching in all departments with a keyword
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
            title="Test Course 2", dept="AAAA", course_code="AAAA 0001", description="This is a test abracadabra jakads",
            prerequisites="N/A",
            offered="Never", cross_listed="Delete me", credit_hours=0
        )
        CourseInfo.objects.update_or_create(
            title="Test Course 3", dept="BBBB", course_code="BBBB 0001", description="This is a test abracadabra jakads",
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
            url="http://this.url", name="John Doe", title="Prof", dept="TEST", email="jd@jd.com", web_page="jd.com", focus="N/A",
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


# Create your tests here.
