from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class usermodeltest(TestCase):
   def doesexist(self):
      user = User.objects.count
      self.assertEqual(user,1)
      
     