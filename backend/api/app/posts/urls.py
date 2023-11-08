from django.urls import path
from .views import CulturePostDetailView, EventPostDetailView, HomeView

urlpatterns = [
    path('posts/cultures/<int:pk>/detail/', CulturePostDetailView.as_view(), name="culture_post_detail"),
    path('posts/events/<int:pk>/detail/', EventPostDetailView.as_view(), name="event_post_detail"),
    path('', HomeView.as_view(), name="home")

]