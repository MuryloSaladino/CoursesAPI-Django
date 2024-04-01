from rest_framework_simplejwt.views import TokenObtainPairView
from .views import AccountView
from django.urls import path


urlpatterns = [
    path("accounts/", AccountView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
