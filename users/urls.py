from django.urls import include, path
from rest_framework import routers
import users.views as views


router = routers.DefaultRouter()

router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
