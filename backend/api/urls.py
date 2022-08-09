from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserView)

urlpatterns = [
]

urlpatterns += router.urls