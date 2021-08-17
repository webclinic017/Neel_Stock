from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class AccountManagerCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.profile.account_manager
