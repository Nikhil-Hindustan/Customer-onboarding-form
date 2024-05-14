from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path('create-customer/', views.create_customer, name='create_customer'),
    path('list-customer/', views.list_customer, name='list_customer'),
]
