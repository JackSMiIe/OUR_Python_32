from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remove_person/<int:journey_id>/', views.remove_person, name='remove_person'),
]