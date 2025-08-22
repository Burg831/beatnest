from django.urls import path
from . import views

urlpatterns = [
    path("", views.gig_list, name="gig_list"),
    path("<int:pk>/", views.gig_detail, name="gig_detail"),
]

