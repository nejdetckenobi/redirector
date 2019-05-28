from django.urls import include, path
from rest_framework import routers
import redirections.views as views


router = routers.DefaultRouter()

router.register(r'', views.RedirectionViewSet, base_name='Redirection')

urlpatterns = [
    path('', include(router.urls)),
]
