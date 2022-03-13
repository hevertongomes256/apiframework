from rest_framework import routers
from django.urls import path
from consumer.views import ListUsers, LogListView

router = routers.SimpleRouter()

urlpatterns = [
    path('users/', ListUsers.as_view(), name='users'),
    path('logs/', LogListView.as_view(), name='logs')
]

urlpatterns += router.urls