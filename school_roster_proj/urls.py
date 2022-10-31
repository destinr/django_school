# school_roster_proj/urls.py

from django.contrib import admin
from django.urls import path, include # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("school/", include("school_roster_app.urls")), # add this
]
