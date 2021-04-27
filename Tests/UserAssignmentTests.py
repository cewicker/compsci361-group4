import unittest
from django.test import TestCase, Client


class UserAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post('/', {'user_id': 'testTA', 'password': 'testpassword'})
        self.client.post('/', {'user_id': 'testIns', 'password': 'testpassword'})
        response = self.client.post('/courses/create_course',
                                    {'course_name': 'test_course', 'course_no': '000', 'section_no': '000',
                                     'is_lab': 'false'})
        self.created_id = response.context['created_course_id']

    def testTaAssignments(self):
        response = self.client.patch('/courses', {'course_id': self.created_id.__str__, 'ta_user_id': 'testTA'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses', {'course_id': self.created_id.__str__})
        self.assertIn('testTa', response.context['course_tas'])

    def testInsAssignments(self):
        response = self.client.patch('/courses', {'course_id': self.created_id.__str__, 'instructor_user_id': 'testIns'})
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses', {'course_id': self.created_id.__str__})
        self.assertIn('testTa', response.context['course_instructors'])
