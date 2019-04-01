from django.test import TestCase
from .models import Profile,Image,Comments
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        # self.yvette= Profile(name="YVETTE",picture="https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",bio="<p>sghjjrt</p>")
        
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Yvette,Profile))
        # Testing Save Method
    def test_save_method(self):
        self.yvette.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
