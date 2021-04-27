from django.urls import path

from classDb.create_user_view import create_User

urlpatterns = [
    path('create_user/', create_User.as_view(), name='create_User'),
]