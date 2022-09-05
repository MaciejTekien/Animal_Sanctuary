from django.test import SimpleTestCase
from sklep.forms import LoginForm, RegisterForm, ResetPasswordForm, AnimalCreateForm, DonationCreateForm,\
    CommentCreateForm, FollowCreateForm, InformationCreateForm, TemporaryHomeForm


class TestForms(SimpleTestCase):

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'user',
            'password': 'password'
        })

        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    # def test_register_form_valid_data(self):
    #     form = RegisterForm(data={
    #         'username': 'ola',
    #         'first_name': 'ola',
    #         'last_name': 'ola',
    #         'email': 'o@g.com',
    #         'password': '123',
    #         'password2': '123'
    #     })
    #
    #     self.assertTrue(form.is_valid())

    # def test_register_form_no_data(self):
    #     form = RegisterForm(data={})
    #
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 6)

    def test_reset_password_valid_data(self):
        form = ResetPasswordForm(data={
            'new_password': '123',
            'new_password2': '123'
        })

        self.assertTrue(form.is_valid())

    def test_reset_password_no_data(self):
        form = ResetPasswordForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_animal_create_valid_data(self):
        form = AnimalCreateForm(data={
            'name': 'antek',
            'age': 2.5,
            'description': 'cool',
            'type': 1
        })

        self.assertTrue(form.is_valid())

    def test_animal_create_no_data(self):
        form = AnimalCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_donation_create_valid_data(self):
        form = DonationCreateForm(data={
            'name': 'antek',
            'amount': 12.55,
            'message': 'cool',
        })

        self.assertTrue(form.is_valid())

    def test_donation_create_no_data(self):
        form = DonationCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_comment_create_valid_data(self):
        form = CommentCreateForm(data={
            'content': 'antek',
        })

        self.assertTrue(form.is_valid())

    def test_comment_create_no_data(self):
        form = CommentCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_follow_create_valid_data(self):
        form = FollowCreateForm(data={
            'note': 'antek',
        })

        self.assertTrue(form.is_valid())

    def test_follow_create_no_data(self):
        form = FollowCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_information_create_valid_data(self):
        form = InformationCreateForm(data={
            'type': 'antek',
            'description': 'okay'
        })

        self.assertTrue(form.is_valid())

    def test_information_create_no_data(self):
        form = InformationCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_temp_home_create_valid_data(self):
        form = TemporaryHomeForm(data={
            'date': '2022-12-01',
        })

        self.assertTrue(form.is_valid())

    def test_temp_home_create_no_data(self):
        form = TemporaryHomeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
