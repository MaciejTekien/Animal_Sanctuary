from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from sklep.models import Animal, Follow, Donation, Comments, TemporaryHome, Information


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('tex', 'tex@g.com', 'coderslab')
        self.user = User.objects.create_superuser('flex', 'flex@t.com' 'coderslab')
        self.main_site_url = reverse('main_site')
        self.logout_url = reverse('logout')
        self.categories_url = reverse('categories')
        self.donations_url = reverse('donations_site')
        self.support_url = reverse('support_site')
        self.profile_url = reverse('profile')
        self.dogs_url = reverse('dogs')
        self.cats_url = reverse('cats')
        self.manage_panel_url = reverse('manage_panel')
        self.temp_home_manage_url = reverse('temp_home_manage')
        self.your_comments_url = reverse('your_comments')
        self.your_follows_url = reverse('your_follows')
        self.login_url = reverse('login')
        self.user1 = User.objects.create(
            first_name='ala',
            last_name='kowalska',
            email='a@k.com',
            username='ala',
            password='123'
        )

    def test_main_site_GET(self):
        response = self.client.get(self.main_site_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_site.html')

    def test_logout_GET(self):
        self.client.login(username='tex', password='coderslab')
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)

    def test_categories_site_GET(self):
        response = self.client.get(self.categories_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories_site.html')

    def test_donations_site_GET(self):
        response = self.client.get(self.donations_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'donation_site.html')

    def test_support_site_GET(self):
        response = self.client.get(self.support_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'support_site.html')

    def test_profile_GET(self):
        self.client.login(username='tex', password='coderslab')
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html', 'profile_superuser.html')

    def test_dogs_GET(self):
        response = self.client.get(self.dogs_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dogs.html')

    def test_cats_GET(self):
        response = self.client.get(self.cats_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cats.html')

    def test_manage_panel_GET(self):
        self.client.login(username='flex', password='coderslab')
        import pdb

        response = self.client.get(self.manage_panel_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_panel.html')

    # def test_temp_home_manage_panel_GET(self):
    #     self.client.login(username='flex', password='coderslab')
    #     response = self.client.get(self.temp_home_manage_url)
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'temporary_home_manage.html')

    def test_your_comments_GET(self):
        self.client.login(username='tex', password='coderslab')
        response = self.client.get(self.your_comments_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_comments.html')

    def test_your_follows_GET(self):
        self.client.login(username='tex', password='coderslab')
        response = self.client.get(self.your_follows_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_follows.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    # def test_login_POST_adds_new_expense(self):
    #     User.objects.create(
    #         first_name='ala',
    #         last_name='kowalska',
    #         email='a@k.com',
    #         username='ala',
    #         password='123'
    #     )
    #
    #     response = self.client.post(self.login_url)
    #
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals()


