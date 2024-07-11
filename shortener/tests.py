from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, URL

class UserProfileModelTest(TestCase):
    def test_user_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        user_profile = UserProfile.objects.create(user=user, bio='This is a bio')
        self.assertEqual(user_profile.user.username, 'testuser')
        self.assertEqual(user_profile.bio, 'This is a bio')

class URLModelTest(TestCase):
    def test_url_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        short_url = 'short12345'
        url = URL.objects.create(user=user, original_url='http://example.com', short_url=short_url)
        self.assertEqual(url.user.username, 'testuser')
        self.assertEqual(url.original_url, 'http://example.com')
        self.assertEqual(url.short_url, short_url)
        self.assertIsNotNone(url.created_at)

from .forms import UserRegistrationForm, URLForm

class UserRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': '12345',
            'password2': '12345'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': '12345',
            'password2': '54321'  # passwords don't match
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

class URLFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'original_url': 'http://example.com'}
        form = URLForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'original_url': 'not a url'}
        form = URLForm(data=form_data)
        self.assertFalse(form.is_valid())

from django.urls import reverse
from django.contrib.auth import get_user_model

class UserViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/register.html')

    def test_valid_user_registration(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'password': '12345',
            'password2': '12345'
        }
        response = self.client.post(reverse('register'), data=form_data)
        self.assertEqual(response.status_code, 302)  # should redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/login.html')

    def test_valid_user_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)  # should redirect after successful login

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shortener/dashboard.html')

class URLViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_url_creation(self):
        form_data = {'original_url': 'http://example.com'}
        response = self.client.post(reverse('dashboard'), data=form_data)
        self.assertEqual(response.status_code, 302)  # should redirect back to dashboard after successful creation
        self.assertTrue(URL.objects.filter(original_url='http://example.com').exists())

    def test_redirect_url_view(self):
        short_url = 'short12345'
        url = URL.objects.create(user=self.user, original_url='http://example.com', short_url=short_url)
        response = self.client.get(reverse('redirect_url', args=[short_url]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'http://example.com')
