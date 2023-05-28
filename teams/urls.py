from django.urls import path
from .views import TeamsView
from .ViewWhithParams import teamViewWhithParams

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", teamViewWhithParams.as_view())
]