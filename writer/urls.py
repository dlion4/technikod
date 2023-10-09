from django.urls import path, include
from . import views

app_name = "writer"

urlpatterns = [
    path("<int:pk>/", views.WriterProfileView.as_view(), name="writer_view"),
    path("authors/<int:pk>/", views.WriterPublicProfileView.as_view(), name="public_profile_view"),
]
