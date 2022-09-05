"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sklep import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainSiteView.as_view(), name='main_site'),
    path('animal_create/', views.AnimalCreate.as_view(), name='animal_create'),
    path('accounts/login/', views.LoginView.as_view(), name='login_required'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('pass_reset/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('donation_create/', views.DonationCreate.as_view(), name='donation_create'),
    path('donations/', views.DonationsView.as_view(), name='donations_site'),
    path('description/<int:animal_id>/', views.DescriptionView.as_view(), name='description'),
    path('support/', views.SupportSiteView.as_view(), name='support_site'),
    path('information_create/', views.InformationCreate.as_view(), name='information_create'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('dogs/', views.Dogs.as_view(), name='dogs'),
    path('cats/', views.Cats.as_view(), name='cats'),
    path('animal_delete/<int:id>', views.AnimalDelete.as_view(), name='animal_delete'),
    path('manage_panel', views.ManagePanel.as_view(), name='manage_panel'),
    path('temporary_home/<int:animal_id>', views.TemporaryHomeCreate.as_view(), name='temporary_home'),
    path('your_comments/', views.YourComments.as_view(), name='your_comments'),
    path('temp_home_manage/', views.TemporaryHomeManage.as_view(), name='temp_home_manage'),
    path('temp_home_delete/<int:id>', views.TemporaryHomeDelete.as_view(), name='temp_home_delete'),
    path('follow/<int:animal_id>', views.FollowView.as_view(), name='follow'),
    path('your_follows/', views.YourFollows.as_view(), name='your_follows'),
    path('follow_delete/<int:id>', views.YourFollowsDelete.as_view(), name='follow_delete'),
    path('comment_delete/<int:id>', views.YourCommentsDelete.as_view(), name='comment_delete'),
]
