from . import views
from django.urls import path

urlpatterns = [
    path("", views.user_dashboard, name="dashboard"),
]
