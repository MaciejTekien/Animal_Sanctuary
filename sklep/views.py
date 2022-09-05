from django.shortcuts import render, redirect
from django.views import View, generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from sklep import forms
from .models import Animal, Donation, Comments, Information, TemporaryHome, Follow
from .forms import AnimalCreateForm, DonationCreateForm, CommentCreateForm, InformationCreateForm, TemporaryHomeForm, \
    FollowCreateForm


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class MainSiteView(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(
            request,
            'main_site.html',
            context={
                'animals': animals
            }
        )


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()

        return render(
            request,
            'login.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_site')
            else:
                msg = 'Incorrect username or password!'

                return render(
                    request,
                    'login.html',
                    context={
                        'form': form,
                        'msg': msg
                    }
                )

        else:
            return render(
                request,
                "login.html",
                context={
                    'form': form
                }
            )


class RegisterView(View):
    def get(self, request):
        form = forms.RegisterForm()

        return render(
            request,
            'register.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = User.objects.create_user(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password')
            )
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')

            user.save()

            return redirect('login')
        else:
            return render(
                request,
                'register.html',
                context={
                    'form': form
                }
            )


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user:
            logout(request)

        return redirect('main_site')


class ResetPasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = forms.ResetPasswordForm()

        return render(
            request,
            'reset_password.html',
            context={
                "form": form
            }
        )

    def post(self, request):
        user = self.request.user
        form = forms.ResetPasswordForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user.set_password(data.get('new_password'))
            user.save()

            return redirect('login')
        else:
            return render(
                request,
                'reset_password.html',
                context={
                    "form": form
                }
            )


class AnimalCreate(SuperuserRequiredMixin, generic.CreateView):
    model = Animal
    form_class = AnimalCreateForm
    template_name = "animal_create.html"
    success_url = "/manage_panel"


class CategoriesView(View):
    def get(self, request):
        return render(
            request,
            'categories_site.html',
        )


class DonationCreate(generic.CreateView):
    model = Donation
    form_class = DonationCreateForm
    template_name = "donation_create.html"
    success_url = '/donations'


class DonationsView(View):
    def get(self, request):
        donation = Donation.objects.all()
        return render(
            request,
            'donation_site.html',
            context={
                'donation': donation
            }
        )


class DescriptionView(LoginRequiredMixin, View):
    def get(self, request, animal_id):
        animals = Animal.objects.all()
        comment_form = forms.CommentCreateForm()
        animal = get_object_or_404(Animal, id=animal_id)
        comments = animal.comments.filter(status=True)
        user_comment = None
        temps = TemporaryHome.objects.all()
        name = self.request.user
        return render(
            request,
            'description.html',
            context={
                'animal': animal,
                'comm': user_comment,
                'comments': comments,
                'comment_form': comment_form,
                'animal_id': animal_id,
                'temps': temps,
                'animals': animals,
                'user': name
            }
        )

    def post(self, request, animal_id):
        name = self.request.user
        animal = get_object_or_404(Animal, id=animal_id)
        temps = TemporaryHome.objects.all()
        animals = Animal.objects.all()
        comments = animal.comments.filter(status=True)
        user_comment = None
        comment_form = CommentCreateForm(request.POST)

        if comment_form.is_valid():
            comment_form.instance.user = name
            user_comment = comment_form.save(commit=False)
            user_comment.animal = animal
            user_comment.save()
            return redirect(f'/description/{animal_id}')

        else:
            return render(
                request,
                'description.html',
                context={
                    'animal': animal,
                    'comm': user_comment,
                    'comments': comments,
                    'comment_form': comment_form,
                    'temps': temps,
                    'animals': animals,
                    'user': name,
                }
            )


class SupportSiteView(View):
    def get(self, request):
        information = Information.objects.all()
        return render(
            request,
            'support_site.html',
            context={
                'information': information
            }
        )


class InformationCreate(SuperuserRequiredMixin, generic.CreateView):
    model = Information
    form_class = InformationCreateForm
    template_name = "information_create.html"
    success_url = '/support'


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        comments = Comments.objects.all()
        if user.is_superuser:
            return render(
                request,
                'profile_superuser.html',
                context={
                    'user': user,
                    'comments': comments
                }
            )
        else:
            return render(
                request,
                'profile.html',
                context={
                    'user': user,
                    'comments': comments
                }
            )


class Dogs(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(
            request,
            'dogs.html',
            context={
                'animals': animals
            }
        )


class Cats(View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(
            request,
            'cats.html',
            context={
                'animals': animals
            }
        )


class AnimalDelete(SuperuserRequiredMixin, generic.DeleteView):
    model = Animal
    template_name = 'delete.html'
    success_url = '/manage_panel'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Animal, id=id_)


class ManagePanel(SuperuserRequiredMixin, View):
    def get(self, request):
        animals = Animal.objects.all()
        return render(
            request,
            'manage_panel.html',
            context={
                'animals': animals
            }
        )


class TemporaryHomeCreate(SuperuserRequiredMixin, View):
    def get(self, request, animal_id):
        form = TemporaryHomeForm()

        return render(
            request,
            'temporary_home_create.html',
            context={
                'form': form,
            }
        )

    def post(self, request, animal_id):
        form = TemporaryHomeForm(request.POST)
        animal = get_object_or_404(Animal, id=animal_id)

        if form.is_valid():
            temp_home = form.save(commit=False)
            temp_home.animal = animal
            temp_home.save()

            return redirect('temp_home_manage')
        else:
            return render(
                request,
                'temporary_home_create.html',
                context={
                    'form': form,
                }
            )


class TemporaryHomeManage(SuperuserRequiredMixin, View):
    def get(self, request):
        animals = Animal.objects.all()
        temps = TemporaryHome.objects.all()
        return render(
            request,
            'temporary_home_manage.html',
            context={
                'animals': animals,
                'temps': temps
            }
        )


class TemporaryHomeDelete(SuperuserRequiredMixin, generic.DeleteView):
    model = TemporaryHome
    template_name = 'delete_temp.html'
    success_url = '/temp_home_manage'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(TemporaryHome, id=id_)


class YourComments(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        dude = request.user
        comments = Comments.objects.all()
        return render(
            request,
            'your_comments.html',
            context={
                'users': users,
                'dude': dude,
                'comments': comments
            }
        )


class FollowView(LoginRequiredMixin, View):
    def get(self, request, animal_id):
        form = FollowCreateForm()
        return render(
            request,
            'follow.html',
            context={
                'form': form,
            }
        )

    def post(self, request, animal_id):
        name = self.request.user
        animal = get_object_or_404(Animal, id=animal_id)
        user_follow = None

        if request.method == 'POST':
            form = FollowCreateForm(request.POST)

            if form.is_valid():
                form.instance.user = name
                user_follow = form.save(commit=False)
                user_follow.animal = animal
                user_follow.save()
                return redirect(f'/description/{animal_id}')
            else:
                form = FollowCreateForm()
            return render(
                request,
                'follow.html',
                context={
                    'form': form
                }
            )


class YourFollows(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        dude = request.user
        follows = Follow.objects.all()
        return render(
            request,
            'your_follows.html',
            context={
                'users': users,
                'dude': dude,
                'follows': follows
            }
        )


class YourFollowsDelete(LoginRequiredMixin, generic.DeleteView):
    model = Follow
    template_name = 'delete_follow.html'
    success_url = '/your_follows'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Follow, id=id_)


class YourCommentsDelete(LoginRequiredMixin, generic.DeleteView):
    model = Comments
    template_name = 'delete_comment.html'
    success_url = '/your_comments'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Comments, id=id_)
