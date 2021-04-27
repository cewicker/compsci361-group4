import unittest

from django.test import TestCase, Client
from models import User


class TestCreateUser(TestCase):
    def setUp(self):
        self.c = Client()
        self.user_data = {"user_ID": "axel650", "first_Name": "Axel", "last_Name": "Rodriguez",
                          "phone_Number": "414-555-5555", "role": "Admin", "assignment_ID": "1500",
                          "email": "uwm@email.com"}
        session = self.c.session

    def test_page_redirect(self):
        response = self.c.post('/', self.user_data, follow=True)
        self.assertEquals([('/create_user/', 302)], response.redirect_chain, "redirect failed")

    def test_create_user_name(self):
        response = self.c.post('/', self.user_data, follow=True)
        self.assertEqual("Axel", response.context["first_Name"], "Name not the same as entered name")
        self.assertEqual("Rodriguez", response.context["last_Name"], "Last name not the same as entered last name")
        self.assertEqual("axel650", response.context["user_ID"], "User ID not the same as entered ID")
        self.assertEqual("414-555-5555", response.context["phone_Number"], "Phone number not the same as entered")
        self.assertEqual("admin", response.context["role"], "Role not correctly set")
        self.assertEqual("1500", response.context["assignment_ID"], "Assignment ID not equal to set ID")
        self.assertEqual("uwm@email.com", response.context["email"], "Name not the same as entered name")

    def test_no_name_user(self):
        no_name = self.user_data
        no_name["name"] = ""
        response = self.c.post('/', no_name, follow=True)
        assert "First name can't be empty" in response.context["errors"]

    def test_no_last_name(self):
        no_last_name = self.user_data
        no_last_name["last_Name"] = ""
        response = self.c.post('/', no_last_name, follow=True)
        assert "Last name can't be empty" in response.context["errors"]

    def test_no_user_id(self):
        no_user_id = self.user_data
        no_user_id["user_ID"] = ""
        response = self.c.post('/', no_user_id, follow=True)
        assert "User must be given a user ID" in response.context["errors"]

    def test_no_number(self):
        no_number = self.user_data
        no_number["number"] = ""
        response = self.c.post('/', no_number, follow=True)
        assert "Please enter a valid phone number" in response.context["errors"]

    def test_no_assignment_id(self):
        no_assigment_id = self.user_data
        no_assigment_id["assignment_id"] = ""
        response = self.c.post('/', no_assigment_id, follow=True)
        assert "Enter a valid assignment ID" in response.context["errors"]

    def test_no_role(self):
        no_role = self.user_data
        no_role["role"] = ""
        response = self.c.post('/', no_role, follow=True)
        assert "User must be given a role" in response.context["errors"]

    def test_email(self):
        no_email = self.user_data
        no_email["email"] = ""
        response = self.c.post('/', no_email, follow=True)
        assert "Enter a valid email" in response.context["errors"]


if __name__ == '__main__':
    unittest.main()
