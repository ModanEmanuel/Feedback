from django.urls import path

from feedback.profiles.migrations import views

urlpatterns = [
    path("", views.CreateProfileView.as_view())
]