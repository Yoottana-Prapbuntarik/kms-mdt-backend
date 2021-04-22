from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, GetUserProfileAPI, UserProfileAPI, Test
from knox import views as knox_views
urlpatterns = [
    path('test/', Test.as_view()),
    path('api/auth',include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/signin', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/profile/<first_name>/<last_name>/<int:id>', GetUserProfileAPI.as_view()),
    path('api/auth/profile/<int:pk>/update', UserProfileAPI.as_view())

]
