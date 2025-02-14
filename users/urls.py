from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    # register/
    path("", views.register, name="register"),
]
