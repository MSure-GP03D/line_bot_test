from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('protected/', views.protected, name='protected'),
    path('api/action-items/', views.action_items, name='action_items'),
]