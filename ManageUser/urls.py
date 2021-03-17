from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, Test
from knox import views as knox_views
urlpatterns = [
    path('test/', Test.as_view()),
    path('api/auth',include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/signin', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
]
