from django.test import TestCase
from django.contrib.auth.models import User
from .models import Avatar
from django.urls import reverse
from .generate import generate_and_save_punk_for_user
from django.contrib.admin.sites import AdminSite
from .admin import AvatarAdmin
from PIL import Image


class AvatarModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")

    def test_avatar_creation(self):
        avatar = Avatar.objects.create(
            user=self.user, punk_type="male", attributes={"Punk Type": "Male"})
        self.assertTrue(isinstance(avatar, Avatar))
        self.assertEqual(avatar.__str__(), avatar.user.username)


class AvatarViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")

    def test_avatar_detail_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('avatar_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "avatar")


class AvatarGenerationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")

    def test_generate_and_save_punk_for_user(self):
        punk_image = generate_and_save_punk_for_user(self.user, None)
        self.assertTrue(isinstance(punk_image, Image.Image))
        avatar = Avatar.objects.get(user=self.user)
        self.assertIsNotNone(avatar.image)


class AvatarAdminTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword")
        self.avatar = Avatar.objects.create(
            user=self.user,
            punk_type="zombie",
            attributes={
                "Punk Type": "Zombie",
                "Head Attribute": "zhair01.png",
                "Facial Hair": "zbeard01.png"})
        self.avatar.save()
        self.site = AdminSite()

    def test_show_attributes(self):
        admin = AvatarAdmin(Avatar, self.site)
        self.assertIn(
            'Punk Type: Zombie', admin.show_attributes(self.avatar))
