from django.test import TestCase
from .models import *
# Create your tests here.

# test image class


class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create(
            username='test_user',
            full_name='abdi ali',
        )
        Image.objects.create(
            title='test image',
            image='https://res.cloudinary.com/waberi33/image/upload/v1654592232/post_k1dlxs.jpg',
            caption='test caption',
            user=self.user
        )

    def test_image_title(self):
        image = Image.objects.get(id=self.user.id)
        self.assertEqual(image.title, 'test image')


# test profile class
class ProfileTestCase(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create(
            username='test_user',
            full_name='abdi ali',
        )

        Profile.objects.create(
            bio='test bio',
            avatar='https://res.cloudinary.com/waberi33/image/upload/v1654592232/post_k1dlxs.jpg',
            user=self.user
        )

    def test_bio(self):
        profile = Profile.objects.get(user_id=self.user.id)
        self.assertEqual(profile.bio, 'test bio')


# test likes class
class LikesTestCase(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create(
            username='test_user',
            full_name='abdi ali',
        )
        # create a image
        self.image = Image.objects.create(
            title='test image',
            image='https://res.cloudinary.com/waberi33/image/upload/v1654592232/post_k1dlxs.jpg',
            caption='test caption',
            user=self.user
        )
        # create a like
        Likes.objects.create(
            image_id=self.image.id,
            user_id=self.user.id
        )

    def test_image_id(self):
        likes = Likes.objects.get(image_id=self.image.id)
        self.assertEqual(likes.image_id, self.image.id)


# test likes class
class CommentsTestCase(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create(
            username='test_user',
            full_name='abdi ali',
        )
        # create a image
        self.image = Image.objects.create(
            title='test image',
            image='https://res.cloudinary.com/waberi33/image/upload/v1654592232/post_k1dlxs.jpg',
            caption='test caption',
            user=self.user
        )
        # create a comment
        Comments.objects.create(
            image_id=self.image.id,
            user_id=self.user.id,
            comment="test comment"
        )

    def test_image_id(self):
        comments = Comments.objects.get(image_id=self.image.id)
        self.assertEqual(comments.image_id, self.image.id)
