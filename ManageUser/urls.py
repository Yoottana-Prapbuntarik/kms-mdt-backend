from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, GetUserProfileAPI, UserProfileAPI, Test, ChangePasswordView
from knox import views as knox_views
urlpatterns = [
    path('test/', Test.as_view()),
    path('api/auth',include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/signin', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/profile/<first_name>/<last_name>/<int:id>', GetUserProfileAPI.as_view()),
    path('api/auth/profile/<int:pk>/update', UserProfileAPI.as_view()),


    # path('api/reset-password/confirm', ChangePasswordView.as_view(), name='reset-password-confirm'),

    # NEW: The django-rest-passwordreset urls to request a token and confirm pw-reset
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
