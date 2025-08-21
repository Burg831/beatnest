from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [

    path("admin/", admin.site.urls),
    path("gigs/", include("gigs.urls")),
    path("", home),

    path("", include("core.urls")),  # homepage -> core app

]

