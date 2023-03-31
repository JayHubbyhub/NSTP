from django.urls import path

from . import views   

urlpatterns = [
    path('', views.login, name='login'),
    # login/users/add/
    path("users/add/", views.add, name="add"),
    path("homepage/", views.homepage, name="homepage"),
]

app_name = "login"