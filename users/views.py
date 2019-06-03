from django.shortcuts import render, redirect
from rest_framework import mixins
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .forms import UserCreationForm


class UserViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
        return redirect('/auth/login', permanent=False)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
