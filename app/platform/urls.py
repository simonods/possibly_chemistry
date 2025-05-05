from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/message/', views.dynamic_message, name='htmx_message'),
]
