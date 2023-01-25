from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    # path('list/', views.list1),
    path('', views.list1)
]