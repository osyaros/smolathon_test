from django.urls import path
from .views import AccountLoginView, RegisterView, check_in_place, UserProfileView, logout_view

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('check/in/<uuid:id>/', check_in_place, name="check_in_place"),
    path('profile/', UserProfileView.as_view(), name="profile"),
]