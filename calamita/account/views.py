from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from .forms import SignUpForm
from .services import get_pair, send_private_key_to_mail


class SignUpView(CreateView):

    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        pk, form.instance.public_key = get_pair()
        user = form.save()
        login(self.request, user)
        send_private_key_to_mail(pk, form.instance.email)
        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('login')
