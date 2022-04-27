from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, password_validation
from common.models import User
from fbchat import Client as MessengerClient
from fbchat.models import ThreadType, Message

UserModel = get_user_model()

# MessengerClient.on2FACode =  TODO: override to deal with 2FA


class LoginForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            client = MessengerClient(username, password)
        except Exception:
            raise self.get_invalid_login_error()

        self.request.session['messenger_session'] = client.getSession()

        if username is not None and password:
            user = User.objects.create_or_update(email=username)
            user.set_password(password)
            user.save()
            self.user_cache = authenticate(self.request, username=username, password=password)
        # else:
        #     self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class MessageForm(forms.Form):
    message = forms.CharField(required=True, max_length=2024) #TODO: check if there's a better field and max length
