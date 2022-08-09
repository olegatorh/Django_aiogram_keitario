from django.contrib.auth.backends import BaseBackend
from api.models import User
from django.contrib.auth.hashers import check_password


class MyCustomAuth(BaseBackend):
    def authenticate(self, request=None, username=None, password=None):
        try:
            user = User.objects.get(login=username, password=password)
        except User.DoesNotExist:
            return None
        return user
