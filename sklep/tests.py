from django.contrib.auth.models import User
from django.urls import reverse
import pytest

from sklep.models import Animal, Comments, Information, TemporaryHome, Follow


@pytest.mark.django_db
def test_main_site(client):
    url = reverse('main_site')
    response = client.get(url)

    assert response.status_code == 200


def test_login(client):
    url = reverse("login")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_correct(client, user):
    url = reverse('login')
    data = {
        'username': user.username,
        'password': "123"
    }
    response = client.post(url, data, follow=True)
    assert response.context["user"] == user


@pytest.mark.django_db
def test_login_fail(client, user):
    url = reverse('login')
    data = {
        'username': f'no_{user.username}',
        'password': "123"
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


def test_register(client):
    url = reverse('register')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_register_correct(client):
    url = reverse('register')
    num = len(User.objects.all())
    data = {
        'username': 'different',
        'email': 'a@a.com',
        'password': "123",
        'password2': "123",
        'first_name': 'ala',
        'last_name': 'kowalska'
    }
    response = client.post(url, data, follow=True)
    assert len(User.objects.all()) == num + 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout(client, user):
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)

    assert response.status_code == 302


def test_logout_fail(client):
    url = reverse('logout')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_reset_password_login(client, user):
    client.force_login(user)
    url = reverse('reset_password')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_reset_password_no_login(client):
    url = reverse('reset_password')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_reset_password_correct_login(client, user):
    client.force_login(user)
    url = reverse('reset_password')
    data = {
        'new_password': "new"
    }
    response = client.post(url, data, follow=True)
    assert response.context["user"] == user
    assert response.status_code == 200


@pytest.mark.django_db
def test_reset_password_correct_no_login(client):
    url = reverse('reset_password')
    data = {
        'new_password': "new"
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_animal_create_permissions(client, superuser):
    client.force_login(superuser)
    url = reverse('animal_create')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_animal_create_no_permissions(client, user):
    client.force_login(user)
    url = reverse('animal_create')
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_animal_create_no_login(client):
    url = reverse('animal_create')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_animal_create_correct(client, animal, superuser):
    num = len(Animal.objects.all())
    client.force_login(superuser)
    url = reverse('animal_create')
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200
    assert len(response.context['animals']) == len(Animal.objects.all()) == num + 1


@pytest.mark.django_db
def test_animal_create_correct_login(client, animal, user):
    client.force_login(user)
    url = reverse('animal_create')
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 403


@pytest.mark.django_db
def test_animal_create_correct_no_login(client, animal):
    url = reverse('animal_create')
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


def test_categories_view(client):
    url = reverse('categories')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_donation_create(client):
    url = reverse('donation_create')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_donations_view(client):
    url = reverse('donations_site')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_description_view_no_login(client, animal):
    url = reverse('description', args=[1])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_description_view_login(client, animal, user):
    client.force_login(user)
    url = reverse('description', args=[animal.pk])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_description_correct(client, animal, user):
    num = len(Comments.objects.all())
    client.force_login(user)
    url = reverse('description', args=[animal.pk])
    data = {
        'content': 'abc',
        'user': user,
        'animal': animal,
    }
    response = client.post(url, data, follow=True)
    assert len(response.context['comments']) == len(Comments.objects.all()) == num + 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_description_correct_no_login(client, animal, user):
    url = reverse('description', args=[animal.pk])
    data = {
        'content': 'abc',
        'user': user,
        'animal': animal,
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_support_site_view(client):
    url = reverse('support_site')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_information_create_view_no_login(client):
    url = reverse('information_create')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_information_create_view_login(client, user):
    client.force_login(user)
    url = reverse('information_create')
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_information_create_view_superuser(client, superuser):
    client.force_login(superuser)
    url = reverse('information_create')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_information_create_correct(client, superuser):
    num = len(Information.objects.all())
    client.force_login(superuser)
    url = reverse('information_create')
    data = {
        'type': 'ok',
        'description': 'not'
    }
    response = client.post(url, data, follow=True)
    assert len(response.context['information']) == len(Information.objects.all()) == num + 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_information_create_correct_login(client, user):
    client.force_login(user)
    url = reverse('information_create')
    data = {
        'type': 'ok',
        'description': 'not'
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 403


@pytest.mark.django_db
def test_information_create_correct_no_login(client):
    url = reverse('information_create')
    data = {
        'type': 'ok',
        'description': 'not'
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_login(client, user):
    client.force_login(user)
    url = reverse('profile')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_no_login(client):
    url = reverse('profile')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_dogs_view(client):
    url = reverse('dogs')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_cats_view(client):
    url = reverse('cats')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_animal_delete_view_superuser(client, superuser, animal):
    client.force_login(superuser)
    url = reverse('animal_delete', args=[animal.pk])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_animal_delete_view_login(client, user, animal):
    client.force_login(user)
    url = reverse('animal_delete', args=[1])
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_animal_delete_view_no_login(client, animal):
    url = reverse('animal_delete', args=[1])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_animal_delete_correct(client, animal, superuser):
    num = len(Animal.objects.all())
    client.force_login(superuser)
    url = reverse('animal_delete', args=[animal.pk])
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert len(response.context['animals']) == num - 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_animal_delete_correct_login(client, animal, user):
    url = reverse('animal_delete', args=[animal.pk])
    client.force_login(user)
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 403


@pytest.mark.django_db
def test_animal_delete_correct_no_login(client, animal):
    url = reverse('animal_delete', args=[animal.pk])
    data = {
        'name': animal.name,
        'age': animal.age,
        'description': animal.description,
        'type': animal.type
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_manage_panel_view_superuser(client, superuser):
    client.force_login(superuser)
    url = reverse('manage_panel')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_manage_panel_view_login(client, user):
    client.force_login(user)
    url = reverse('manage_panel')
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_manage_panel_view_no_login(client):
    url = reverse('manage_panel')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_temporary_home_create_view_superuser(client, superuser):
    client.force_login(superuser)
    url = reverse('temporary_home', args=[1])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_temporary_home_create_view_login(client, user):
    client.force_login(user)
    url = reverse('temporary_home', args=[1])
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_temporary_home_create_view_no_login(client):
    url = reverse('temporary_home', args=[1])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_temporary_home_create_correct(client, temp_home, superuser):
    client.force_login(superuser)
    num = len(TemporaryHome.objects.all())
    url = reverse('temporary_home', args=(temp_home.animal.id,))
    data = {
        'is_active': True,
        'animal': temp_home.animal,
        'date': temp_home.date
    }
    response = client.post(url, data)
    assert len(TemporaryHome.objects.all()) == num + 1
    assert response.status_code == 302


@pytest.mark.django_db
def test_temporary_home_manage_view_superuser(client, superuser):
    client.force_login(superuser)
    url = reverse('temp_home_manage')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_temporary_home_manage_view_login(client, user):
    client.force_login(user)
    url = reverse('temp_home_manage')
    response = client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_temporary_home_manage_view_no_login(client):
    url = reverse('temp_home_manage')
    response = client.get(url)

    assert response.status_code == 302


# @pytest.mark.django_db
# def test_temporary_home_delete_view(client, superuser, temp_home):
#     client.force_login(superuser)
#     url = reverse('temp_home_delete', args=[temp_home.pk])
#     response = client.get(url)
#
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_temporary_home_delete_correct(client, temp_home, superuser):
#     client.force_login(superuser)
#     num = len(TemporaryHome.objects.all())
#     url = reverse('temp_home_delete', args=[temp_home.pk])
#     data = {
#         'is_active': True,
#         'animal': temp_home.animal,
#         'date': temp_home.date
#     }
#     response = client.post(url, data, follow=True)
#     assert len(TemporaryHome.objects.all()) == num - 1
#     assert response.status_code == 200


@pytest.mark.django_db
def test_your_comments_view_login(client, user):
    client.force_login(user)
    url = reverse('your_comments')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_your_comments_view_no_login(client):
    url = reverse('your_comments')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_your_follows_view_login(client, user):
    client.force_login(user)
    url = reverse('your_follows')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_your_follows_view_no_login(client):
    url = reverse('your_follows')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_follow_view_login(client, user):
    client.force_login(user)
    url = reverse('follow', args=[1])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_follow_view_np_login(client):
    url = reverse('follow', args=[1])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_follow_correct(client, animal, user):
    client.force_login(user)
    num = len(Follow.objects.all())
    url = reverse('follow', args=[animal.pk])
    data = {
        'user': user,
        'animal': animal,
        'note': 'abc'
    }
    response = client.post(url, data, follow=True)
    assert len(Follow.objects.all()) == num + 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_follow_correct_no_login(client, animal, user):
    url = reverse('follow', args=[animal.pk])
    data = {
        'user': user,
        'animal': animal,
        'note': 'abc'
    }
    response = client.post(url, data, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_follow_delete_view(client, user, animal):
    client.force_login(user)
    follow = Follow.objects.create(
        user=user,
        animal=animal,
        note='abc'
    )
    url = reverse('follow_delete', args=[follow.pk])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_follow_delete_view_no_login(client, user, animal):
    follow = Follow.objects.create(
        user=user,
        animal=animal,
        note='abc'
    )
    url = reverse('follow_delete', args=[follow.pk])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_follow_delete_correct(client, animal, user):
    follow = Follow.objects.create(
        user=user,
        animal=animal,
        note='abc'
    )
    num = len(Follow.objects.all())
    client.force_login(user)
    url = reverse('follow_delete', args=[follow.pk])
    data = {
        'user': follow.user,
        'animal': follow.animal,
        'note': follow.note,
        'date': follow.date
    }
    response = client.post(url, data, follow=True)
    assert len(Follow.objects.all()) == num - 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_delete_view(client, user, animal):
    client.force_login(user)
    comment = Comments.objects.create(
        user=user,
        animal=animal,
        content='abc'
    )
    url = reverse('comment_delete', args=[comment.pk])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_comment_delete_view_no_login(client, user, animal):
    comment = Comments.objects.create(
        user=user,
        animal=animal,
        content='abc'
    )
    url = reverse('comment_delete', args=[comment.pk])
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db
def test_comment_delete_correct(client, animal, user):
    comment = Comments.objects.create(
        user=user,
        animal=animal,
        content='abc'
    )
    num = len(Comments.objects.all())
    client.force_login(user)
    url = reverse('comment_delete', args=[comment.pk])
    data = {
        'user': comment.user,
        'animal': comment.animal,
        'content': comment.content,
        'publish': comment.publish,
        'status': comment.status
    }
    response = client.post(url, data, follow=True)
    assert len(Follow.objects.all()) == num - 1
    assert response.status_code == 200


