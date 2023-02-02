from django.urls import path
from .import views

urlpatterns = [
    path('', views.WebHook.as_view(), name='webhook_details')
]