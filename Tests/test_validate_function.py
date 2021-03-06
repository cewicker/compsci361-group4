import unittest
from classTracker.models import User
from django.test import TestCase
from classTracker.validateFunction import validate_user




class TestValidateFunction(TestCase):

    def test_good_input(self):
        user = User(first_name="test", last_name="last test", id="badger", number="414", role="Supervisor",
                    assignment_ID="42", email="test@email.com", user_id="lucky")
        self.assertEqual([], validate_user(user))

    def test_no_firstname(self):
        user = User(first_name="", last_name="last test", id="badger", number="414", role="Supervisor",
                    assignment_ID="42", email="test@email.com",user_id="lucky")
        self.assertEqual(["First name can't be empty"], validate_user(user))

    def test_no_lastname(self):
        user = User(first_name="test", last_name="", id="badger", number="414", role="Supervisor",
                    assignment_ID="42", email="test@email.com",user_id="lucky")
        self.assertEqual(["Last name can't be empty"], validate_user(user))

    def test_no_id(self):
        user = User(first_name="test", last_name="last test", id="", number="414", role="Supervisor",
                    assignment_ID="42", email="test@email.com",user_id="lucky")
        self.assertEqual(["User must be given a user ID"], validate_user(user))

    def test_no_number(self):
        user = User(first_name="test", last_name="last test", id="badger", number="", role="Supervisor",
                    assignment_ID="42", email="test@email.com",user_id="lucky")
        self.assertEqual(["Please enter a valid phone number"], validate_user(user))

    def test_no_role(self):
        user = User(first_name="test", last_name="last test", id="badger", number="414", role="",
                    assignment_ID="42", email="test@email.com",user_id="lucky")
        self.assertEqual(["User must be given a role"], validate_user(user))

    def test_no_assignment_id(self):
        user = User(first_name="test", last_name="last test", id="badger", number="414", role="Supervisor",
                    assignment_ID="", email="test@email.com",user_id="lucky")
        self.assertEqual(["Enter a valid assignment ID"], validate_user(user))

    def test_no_email(self):
        user = User(first_name="test", last_name="last test", id="badger", number="414", role="Supervisor",
                    assignment_ID="42", email="",user_id="lucky")
        self.assertEqual(["Enter a valid email"], validate_user(user))


if __name__ == '__main__':
    unittest.main()
