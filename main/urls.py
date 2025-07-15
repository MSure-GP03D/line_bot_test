# action_item_bot/urls.py (修正)
from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("Hello World")

urlpatterns = [
    path('', hello, name='hello')
]