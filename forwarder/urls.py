from django.urls import include, path
from forwarder.views import forward

urlpatterns = [
    path('', forward),
]
