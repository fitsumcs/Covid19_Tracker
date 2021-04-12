
from django.urls import path
from .views import covidDisplay
urlpatterns = [
   path('',covidDisplay)
]
