from .views import ContentView, ContentDetailView
from django.urls import path


urlpatterns = [
    path("courses/<course_id>/contents/", ContentView.as_view()),
    path("courses/<course_id>/contents/<content_id>/", ContentDetailView.as_view()),
]
