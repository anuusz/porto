from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    # URL lain jika ada
]
