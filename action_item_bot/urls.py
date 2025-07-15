# main/urls.py (新規作成)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('protected', views.protected, name='protected'),
    path('api/action-items', views.action_items, name='action_items'),
]

# action_item_bot/urls.py (修正)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]