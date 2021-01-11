from django.urls import path

from . import views


urlpatterns = [
    path("", views.FlowersView.as_view()),
]