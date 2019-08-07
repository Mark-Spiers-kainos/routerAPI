import os
import unittest
from applications.models import Application
from good.models import Good
from user.models import User
from applications.serializer import ApplicationSerializer


class testApplications(unittest.TestCase):

    def setUp(self):
        User.objects.create(
            username="testUser", password="testPassword")
        user = User.objects.get(username="testUser")
        Good.objects.create(
            user=user, name="testGood")
        good = Good.objects.get(name="testGood")

    def test_create_app(self):
        user = User.objects.get(username="testUser")
        good = Good.objects.get(name="testGood")
        data = {
            "user": user.id,
            "name": "testApp",
            "destination": "location",
            "goods": [good.id]
        }
        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        application = Application.objects.get(name="testApp")
        self.assertEqual(application.destination, "location")

    def tearDown(self):
        Application.objects.filter(name="testApp").delete()
        Good.objects.filter(name="testGood").delete()
        User.objects.filter(username="testUser").delete()
