from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Animal, Donation, Comments, Information, TemporaryHome, Follow


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-center',
                                                             'placeholder': 'Your cool username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-center',
                                                                 'placeholder': "Type in your secret password!"}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-center',
                                                             'placeholder': 'Your cool username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-center',
                                                                 'placeholder': "Type in your secret password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-center',
                                                                  'placeholder': "Make sure you typed it correctly!"
                                                                  }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-center', 'placeholder': 'Your beautiful first name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-center', 'placeholder': 'Your nice last name'}),
            "email": forms.EmailInput(attrs={'class': 'form-center', 'placeholder': """Don't forget the "@"!"""}),
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            if password2 != password:
                raise ValidationError("Passwords are not the identical!")

        def clean_mail(self):
            email = self.cleaned_data.get('email')
            user = User.objects.filter(email=email)
            if user:
                raise ValidationError("This email is already in use, please use a different one!")


class ResetPasswordForm(forms.Form):

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'from-center',
                                                                     'placeholder': "Type in new password"}))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-center',
                                                                      'placeholder': "Make sure you typed it correctly!"
                                                                      }))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('new_password') != cleaned_data.get('new_password2'):
            raise ValidationError("Passwords are different! Please type in same passwords.")


class AnimalCreateForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ("type", "name", "description", "age")

        widgets = {
            "type": forms.Select(attrs={'class': 'form-center'}),
            "name": forms.TextInput(attrs={'class': 'form-center', 'placeholder': 'Name your sale'}),
            "description": forms.Textarea(attrs={'class': 'form-center', 'placeholder': 'Describe your puppy'}),
            "age": forms.NumberInput(attrs={'class': 'form-center', 'placeholder': 'age'})
        }


class DonationCreateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ("name", "amount", "message")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-center', 'placeholder': 'Your name here'}),
            'amount': forms.NumberInput(attrs={'class': 'form-center',
                                               'placeholder': "The amount you want to donate"}),
            'message': forms.Textarea(attrs={'class': 'form-center', 'placeholder': "Your message here"})
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', )

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-center', 'placeholder': 'Comment'})
        }


class FollowCreateForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('note', )

        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-center', 'placeholder': 'Note'})
        }


class InformationCreateForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('type', 'description')

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-center', 'placeholder': "type"}),
            'description': forms.Textarea(attrs={'class': 'form-center', 'placeholder': "Description"})
        }


class TemporaryHomeForm(forms.ModelForm):
    class Meta:
        model = TemporaryHome
        fields = ('date', )

        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-center',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

