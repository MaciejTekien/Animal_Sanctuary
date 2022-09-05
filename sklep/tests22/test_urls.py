from django.test import SimpleTestCase
from django.urls import resolve, reverse
from sklep.views import MainSiteView, AnimalCreate, LoginView, RegisterView, ResetPasswordView, LogoutView,\
    CategoriesView, DonationCreate, DonationsView, DescriptionView, SupportSiteView, InformationCreate, Profile, Dogs,\
    Cats, AnimalDelete, ManagePanel, TemporaryHomeCreate, YourComments, YourFollows, TemporaryHomeDelete,\
    TemporaryHomeManage, FollowView


class TestUrls(SimpleTestCase):

    def test_main_site_url(self):
        url = reverse("main_site")
        self.assertEquals(resolve(url).func.view_class, MainSiteView)

    def test_animal_add_url(self):
        url = reverse("animal_create")
        self.assertEquals(resolve(url).func.view_class, AnimalCreate)

    def test_login_url(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func.view_class, RegisterView)

    def test_pass_reset_url(self):
        url = reverse("reset_password")
        self.assertEquals(resolve(url).func.view_class, ResetPasswordView)

    def test_logout_url(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_categories_url(self):
        url = reverse("categories")
        self.assertEquals(resolve(url).func.view_class, CategoriesView)

    def test_donation_create_url(self):
        url = reverse("donation_create")
        self.assertEquals(resolve(url).func.view_class, DonationCreate)

    def test_donations_url(self):
        url = reverse("donations_site")
        self.assertEquals(resolve(url).func.view_class, DonationsView)

    def test_description_url(self):
        url = reverse("description", args=[1])
        self.assertEquals(resolve(url).func.view_class, DescriptionView)

    def test_support_url(self):
        url = reverse("support_site")
        self.assertEquals(resolve(url).func.view_class, SupportSiteView)

    def test_information_create_url(self):
        url = reverse("information_create")
        self.assertEquals(resolve(url).func.view_class, InformationCreate)

    def test_profile_url(self):
        url = reverse("profile")
        self.assertEquals(resolve(url).func.view_class, Profile)

    def test_dogs_url(self):
        url = reverse("dogs")
        self.assertEquals(resolve(url).func.view_class, Dogs)

    def test_cats_url(self):
        url = reverse("cats")
        self.assertEquals(resolve(url).func.view_class, Cats)

    def test_animal_delete_url(self):
        url = reverse("animal_delete", args=[1])
        self.assertEquals(resolve(url).func.view_class, AnimalDelete)

    def test_manage_panel_url(self):
        url = reverse("manage_panel")
        self.assertEquals(resolve(url).func.view_class, ManagePanel)

    def test_temp_home_create_url(self):
        url = reverse("temporary_home", args=[1])
        self.assertEquals(resolve(url).func.view_class, TemporaryHomeCreate)

    def test_your_comments_url(self):
        url = reverse("your_comments")
        self.assertEquals(resolve(url).func.view_class, YourComments)

    def test_your_follows_url(self):
        url = reverse("your_follows")
        self.assertEquals(resolve(url).func.view_class, YourFollows)

    def test_temp_home_manage_url(self):
        url = reverse("temp_home_manage")
        self.assertEquals(resolve(url).func.view_class, TemporaryHomeManage)

    def test_temp_home_delete_url(self):
        url = reverse("temp_home_delete", args=[1])
        self.assertEquals(resolve(url).func.view_class, TemporaryHomeDelete)

    def test_follow_url(self):
        url = reverse("follow", args=[1])
        self.assertEquals(resolve(url).func.view_class, FollowView)
