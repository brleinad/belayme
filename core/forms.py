from django.forms import Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, get_user_model, password_validation

from common.models import User

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            print('yasdfaouou ', self.user_cache)
            if self.user_cache is None:
                user = User.objects.create(email=username)
                user.set_password(password)
                user.save()
                self.user_cache = authenticate(self.request, username=username, password=password)
                print('youou ', self.user_cache)

                # raise self.get_invalid_login_error() if facebook api fails
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data



class MessageForm(Form):
    pass