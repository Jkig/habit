from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerNew, name="register"),


    path('', views.list1, name="main"),
]