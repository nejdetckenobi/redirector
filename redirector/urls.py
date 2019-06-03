"""redirector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from forwarder.views import forward
from users.views import signup
from rest_framework.routers import DefaultRouter
from redirections.views import RedirectionViewSet
from users.views import UserViewSet

api_router = DefaultRouter()
api_router.register('redirections', RedirectionViewSet, basename='redirections')
api_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
    path('api/api-auth/', include('rest_framework.urls',
                                  namespace='rest_framework')),
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', signup),
    re_path(r'([A-Za-z0-9]{8}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{12})', forward),
]
