from django.test import TestCase
from .models import Image, Profile, Comment, Like, User


class ImageModelTest(TestCase):
    def setUp(self):
        self.image_name = 'vacay'
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

class ProfileModelTest(TestCase):
    def setUp(self):
        bio = 'here to stay'
        user = User(username='sam')
        user.save()
        self.profile = Profile(bio=bio, user=user)

    def test_instance(self):
            self.assertTrue(isinstance(self.profile, Profile))
    
    def test_profile_images(self):
        self.assertTrue(self.profile.profile_images != 0)
    
class CommentModelTest(TestCase):
    def setUp(self):
        user = User(username='sam')
        body = 'nice!!'
        self.comment = Comment(user=user, body=body)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))





   
    
