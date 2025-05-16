from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.scorepage, name="home"),
    path("about/", view=views.aboutpage, name="about"),
]
