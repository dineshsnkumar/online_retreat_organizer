from . import views
from django.urls import path

app_name = 'usermanagement'

urlpatterns = [
    path("", views.user_dashboard, name="dashboard"),
    # retreat/1/
    path("<int:retreat_id>/", views.retreat_details, name="retreat_details"),
]
