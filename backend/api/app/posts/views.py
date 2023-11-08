
from django.views.generic import DetailView, TemplateView, ListView

from account.models import CheckInURL
from posts.models import CulturePost, EventPost


class HomeView(TemplateView):
    template_name = 'posts/home.html'


class CulturePostListView(ListView):
    model = CulturePost


class EventPostListView(ListView):
    model = EventPost


class CulturePostDetailView(DetailView):
    model = CulturePost
    template_name = "posts/culture_detail.html"
    context_object_name = "post"


class EventPostDetailView(DetailView):
    model = DetailView
    template_name = "posts/event_detail.html"
    context_object_name = "post"


