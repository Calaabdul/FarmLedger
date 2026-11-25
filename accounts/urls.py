from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordChangeView,
    PasswordChangeDoneView,
    ProfileView,
    SignupView,
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path(
        'change-password/',
        CustomPasswordChangeView.as_view(),
        name='change-password',
    ),

    path(
        'password-change-done/',
        PasswordChangeDoneView.as_view(),
        name='password-change-done',
    ),

    # Password reset
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/password_reset_subject.txt',
            success_url='/accounts/password-reset/done/',
        ),
        name='password-reset',
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html',
        ),
        name='password-reset-done',
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url='/accounts/reset/done/',
        ),
        name='password-reset-confirm',
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html',
        ),
        name='password-reset-complete',
    ),
]
