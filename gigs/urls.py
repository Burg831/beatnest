from django.urls import path
from . import views

urlpatterns = [
    path("", views.gigs_list, name="gigs_list"),
]

