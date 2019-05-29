from rest_framework import viewsets
from rest_framework import mixins
from .models import Redirection
from .serializers import RedirectionSerializer


class RedirectionViewSet(viewsets.GenericViewSet,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = RedirectionSerializer

    def get_queryset(self):
        return Redirection.objects.filter(user_id=self.request.user.id)
