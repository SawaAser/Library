from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm, EditProfileUserForm, \
                    EditUserForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required, user_passes_test


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/login.html'
    extra_context = {'title': 'LoginNew'}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'authentication/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUserEdit(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = EditProfileUserForm
    template_name = 'authentication/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class EditUser(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = EditUserForm
    template_name = 'authentication/edit_user.html'
    permission_required = 'user.is_superuser'

    def get_success_url(self):
        return reverse_lazy('users:manage_users')

    def get_object(self, queryset=None):
        user_id = self.kwargs['user_id']
        return get_object_or_404(self.model, id=user_id)


def home(request):
    return render(request, 'authentication/home.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect('users:manage_users')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = CustomUser.objects.all()
    return render(request, 'authentication/manage_users.html', {'users': users})


class UserPasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "authentication/password_change_form.html"


@login_required
@user_passes_test(lambda u: u.is_superuser)
def profile_user_by_id(request, user_id):
    users = CustomUser.get_by_id(user_id)
    form_class = ProfileUserForm(instance=users)
    return render(request, 'authentication/profile.html', {'form': form_class})
