# myapp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),  # Home page
    path("about/", views.about, name="about"),  # About page
    path("prediction/", views.prediction, name="prediction"),
    ]