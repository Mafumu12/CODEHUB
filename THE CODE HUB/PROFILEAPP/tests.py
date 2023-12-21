from django.test import TestCase
from .models import UserProfile

# Create your tests here.
class FirstModelTest(TestCase):

    def test_string(self):
        profile = UserProfile(name="Mafumu")
        self.assertEqual(str(profile),profile.name)
