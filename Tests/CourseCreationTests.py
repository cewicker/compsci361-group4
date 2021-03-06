import unittest
from django.test import TestCase, Client
from django.conf import settings


class CourseCreationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def testCourseCreation(self):
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false', 'meeting_times': 'MW 10:30-12:00'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context['course_name'], 'test_course')
        self.assertEquals(response.context['course_no'], '000')
        self.assertEquals(response.context['section_no'], '000')
        self.assertEquals(response.context['is_lab'], 'false')
        self.assertEquals(response.context['meeting_times'], 'MW 10:30-12:00')
        self.assertEquals(response.get_full_path(), '/courses')

    def testDupCourseNumber(self):
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'meeting_times': 'None', 'is_lab': 'false'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context['created_course_id'], '000')
        self.assertEquals(response.context['section_no'], '000')
        self.assertEquals(response.context['is_lab'], 'false')
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course 2', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false', 'meeting_times': 'None'})
        self.assertNotEquals(response.status_code, 302)
        # should stay on the page and tell user they cannot make two courses with the same number

    def testDupSectionCreation(self):
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['created_course_id'], '000')
        self.assertEquals(response.context['section_no'], '000')
        self.assertEquals(response.context['is_lab'], 'false')
        self.assertEquals(response.get_full_path(), '/courses')
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false', 'section_only': 'true'})
        self.assertNotEquals(response.status_code, 302)
        # should stay on the page and tell user they cannot make a duplicate section

    def testSectionCreation(self):
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['created_course_id'], '000')
        self.assertEquals(response.context['section_no'], '000')
        self.assertEquals(response.context['is_lab'], 'false')
        self.assertEquals(response.get_full_path(), '/courses')
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '001',
                                     'is_lab': 'false', 'section_only': 'true'})
        self.assertEquals(response.get_full_path(), '/courses')
        response = self.client.get('courses', {'course_no': '000'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['lab_sections'], 2)

    def testInvalidSection(self):
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false', 'section_only': 'true'})
        self.assertNotEquals(response.status_code, 302)
        # should stay on the page and tell user they cannot make a section only without a course
