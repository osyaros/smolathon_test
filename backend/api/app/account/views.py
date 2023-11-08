from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from .exceptions import TransactionError, CheckInUrlError
from .forms import RegisterUserForm, AuthenticationUserForm
from .models import CheckInURL
from .utils.point_transaction import add_points_to_user


@login_required
def check_in_place(request: HttpRequest, *args, **kwargs):
    check_url: CheckInURL = get_object_or_404(CheckInURL, id=kwargs.get('id', None))

    model = ContentType.objects.get(model=check_url.content_type.model)
    post = check_url.content_object
    try:
        transaction = add_points_to_user(request.user, check_url)
    except TransactionError as e:
        """Chow transaction error message"""
        return render(request, 'posts/check_in_error.html', {'error': "error"})

    except CheckInUrlError as e:
        """Chow url error message"""
        return render(request, 'account/check_in_error.html', {'error': "error"})

    return render(request, 'account/check_in_success.html', {'post': post, 'transaction': transaction})

    # return render(request, 'posts/check_in_error.html', {'error': "error"})


def logout_view(request):
    logout(request)
    return redirect("main")


class AccountLoginView(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'account/login.html'


class RegisterView(CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = 'account/register.html'
    success_url = reverse_lazy('profile')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


# class SearchResultsView():
#     pass