from django.contrib.auth import views
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from core import forms


class LoginView(views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    form_class = forms.LoginForm

    def form_invalid(self, form):
        print('so sad', form.error_messages)
        return super().form_invalid(form)

    def form_valid(self, form):
        print('uyooyoyoyoyoyo')
        password = form.cleaned_data.get('password')
        print(f'BOB: {password}')
        return super().form_valid(form)


class HomepageView(TemplateView):
    template_name = 'home.html'


class MessagingView(FormView):
    template_name = ''
    # form_class =
