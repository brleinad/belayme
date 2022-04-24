from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def login(self, request, user):
        return super().login(request, user)

    def save_user(self, request, user, form, commit=True):
        return super().save_user(request, user, form, commit)
