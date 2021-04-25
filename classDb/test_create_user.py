import unittest

from django.test import TestCase, Client
from .models import Stuff, MyUser

class TestCreatteUser(TestCase):
    def setUp(self):
        self.c = Client()
        self.user_data= {"user_ID": "axel650", "first_Name": "Axel", "last_Name": "Rodriguez", "phone_Number": "414-555-5555", "role": "Admin", "assignment_ID": "1500", "email": "uwm@email.com"}
        session = self.c.session

    def test_page_redirect(self):
        response = self.c.post('/', self.user_data, follow=True)
        self.assertEquals([('/things/', 302)], response.redirect_chain, "redirect failed")

    def test_create_user_name(self):
        response = self.c.post('/', self.user_data, follow=True)
        self.assertEqual("Axel", response.context["first_Name"], "Name not the same as entered name")
        self.assertEqual("Rodriguez", response.context["last_Name"], "Last name not the same as entered last name")
        self.assertEqual("axel650", response.context["user_ID"], "User ID not the same as entered ID")
        self.assertEqual("414-555-5555", response.context["phone_Number"], "Phone number not the same as entered")
        self.assertEqual("admin", response.context["role"], "Role not correctly set")
        self.assertEqual("1500", response.context["assignment_ID"], "Assignment ID not equal to set ID")
        self.assertEqual("uwm@email.com", response.context["email"], "Name not the same as entered name")


    def test_page_redirect(self):
        response = self.c.post('/', {"name": "axel", "password": "admin"}, follow=True)
        self.assertEquals([('/pop_up_create_user/', 302)], response.redirect_chain, "redirect failed")



    def test_no_name_user(self):
        no_name = self.user_data
        no_name["name"] = ""
        response = self.c.post('/', no_name, follow=True)
        assert no_name_error in response.context["errMessages"]


    def test_not_last_empty_user(self):
        no_last_name = self.user_data
        no_last_name["last_Name"]=""
        response = self.c.post('/', no_last_name, follow=True)
        assert no_last_name_err in response.context["errMessages"]


if __name__ == '__main__':
    unittest.main()
