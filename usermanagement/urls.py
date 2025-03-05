from . import views
from django.urls import path

app_name = 'usermanagement'

urlpatterns = [
    path("dashboard/", views.user_dashboard, name="dashboard"),
    path("", views.user_dashboard, name="dashboard"),
    # retreat/1/
    path("retreat/<int:retreat_id>/", views.retreat_details, name="retreat_details"),
    path("retreat/<int:retreat_id>/recordings/", views.retreat_recordings, name="retreat_recordings"),
]
