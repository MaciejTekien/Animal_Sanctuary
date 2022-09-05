import pytest
import datetime
from django.contrib.auth.models import User

from sklep.models import Animal, TemporaryHome, Comments, Follow


@pytest.fixture
def user():
    u = User.objects.create_user('tex', 't@t.com', '123')
    return u


@pytest.fixture
def superuser():
    u = User.objects.create_superuser('flex', 't@t.com', '123')

    return u


@pytest.fixture
def animal():
    a = Animal.objects.create(
        name='olo',
        age=2.5,
        description='cute',
        type=1
    )
    return a


@pytest.fixture
def temp_home(animal):
    a = TemporaryHome.objects.create(
        date=datetime.date(1977,12,20),
        is_active=True,
        animal=animal
    )
    return a


@pytest.fixture
def comments():
    a = Comments.objects.create(
        content='olo',
        user=user,
        animal=animal,
        publish='2022.12.01',
        status=True
    )
    return a
