from django.contrib.auth import views
from django.views import generic
from django.urls import reverse_lazy


from core import forms
from core.messenger import Messenger
from core import models


class LoginView(views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    form_class = forms.LoginForm

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        # print(f'BOB: {password}')
        return super().form_valid(form)


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO get contact list from messenger
        # TODO add flag for belayers
        messenger = Messenger(self.request.user, self.request.session.get('messenger_session'))
        messenger_contacts = messenger.get_contacts()
        context["contacts"] = messenger_contacts
        return context


class AddBelayerView(generic.CreateView):
    success_url = reverse_lazy('contacts')
    model = models.MessengerBelayer
    fields = ['name', 'user', 'photo', 'messenger_id',]
    template_name = 'contacts.html'


class RemoveBelayerView(generic.DeleteView):
    success_url = reverse_lazy('contacts')
    model = models.MessengerBelayer
    template_name = 'contacts.html'


class MessagingView(generic.FormView):
    template_name = 'message.html'
    form_class = forms.MessageForm
    success_url = reverse_lazy('send_message')

    def form_valid(self, form):
        messenger = Messenger(self.request.user, self.request.session.get('messenger_session'))
        message = form.cleaned_data.get('message')
        messenger.send_message(message)
        return super().form_valid(form)
