from django.test import TestCase
from .models import Image, Profile, Comment, Like, User


class ImageModelTest(TestCase):
    def setUp(self):
        self.iamge_name = 'vacay'
        self.user = User(username='sam')
        self.user.save()
        self.profile = Profile(bio="Never say never", user=self.user)
        self.new_img = Image(id=40, caption="tembea kenya", profile=self.profile)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_img, Image))
    
    
    def test_delete_method(self):
        self.new_img.delete_image()
        self.assertTrue(self.new_img.DoesNotExist)
    
    def test_update_method(self):
        new_caption = 'testing'
        self.new_img.update_image(new_caption)
        self.assertEqual(self.new_img.caption, 'testing')
    


   
    
