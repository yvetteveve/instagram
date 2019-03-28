from django.test import TestCase
from .models import Profile,Image,Comments
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kt = Profile(name="yvette umubyeyi",picture="https://www.instagram.com/p/BlDQch_H4VE/",bio="<p>sghjjrt</p>")
    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kt,Profile))
        # Testing Save Method
    def test_save_method(self):
        self.kt.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        