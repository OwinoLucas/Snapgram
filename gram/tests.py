from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='default')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                    user=self.user)
    #Test Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    #Test Save Profile
    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='default', user=User(username='default-007'))
        self.profile_test.save()

        self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)

class TestComment(TestCase):
    def setUp(self):
        self.comment = Profile(name='default', user=User(username='default-007'))
        self.comment.save()

    #Test Instance