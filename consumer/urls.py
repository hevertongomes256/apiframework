from rest_framework import routers
from django.urls import path
from consumer.views import ListUsers

router = routers.SimpleRouter()

urlpatterns = [
    path('users/', ListUsers.as_view(), name='users'),
]

urlpatterns += router.urls