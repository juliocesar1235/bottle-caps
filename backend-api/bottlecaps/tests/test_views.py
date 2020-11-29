import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User, Category, Title, Review, Token
from ..serializers import *

# initialize the APIClient app
client = Client()

class loginTest(TestCase):
    
    def setUp(self):
        User.objects.create(
            username='alvaro', 
            email='alvaro@bottlecaps.com', 
            password='a1234'
            )