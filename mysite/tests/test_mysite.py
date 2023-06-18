from django.test import SimpleTestCase
from django.urls import resolve, reverse
from user_accounts.views import ProfileView
from blog.views import PostList, PostDetail


class URLTests(SimpleTestCase):
    def test_admin_url_resolves(self):
        url = reverse('admin:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class.__name__, 'LoginView')

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class.__name__, 'LogoutView')

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, ProfileView)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=['post-slug'])
        self.assertEqual(resolve(url).func.view_class, PostDetail)
