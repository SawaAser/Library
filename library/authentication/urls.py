from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
                                        PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('profile_by_id/<int:user_id>/', views.profile_user_by_id, name='profile_by_id'),
    path('profile-edit/', views.ProfileUserEdit.as_view(), name='profile_edit'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('password-reset/',
         PasswordResetView.as_view(
            template_name='authentication/password_reset_form.html',
            email_template_name='authentication/password_reset_email.html',
            success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
            template_name='authentication/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),
    path('manage/', views.manage_users, name='manage_users'),
    # path('toggle_active/<int:user_id>/', views.toggle_user_active, name='toggle_user_active'),
    # path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    # path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('edit/<int:user_id>/', views.EditUser.as_view(), name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
