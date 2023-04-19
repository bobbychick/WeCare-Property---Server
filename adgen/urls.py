from django.urls import path
from .views import Ad_Generator

urlpatterns = [
    path("adgen/", Ad_Generator.as_view()),
]
