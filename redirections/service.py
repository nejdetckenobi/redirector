from .models import Redirection
from users.models import User
from uuid import uuid4


class RedirectionService(object):
    def get(id):
        return Redirection.objects.get(pk=id)

    def get_by_unique_id(self, unique_id):
        try:
            result = Redirection.objects.get(unique_id=unique_id)
        except Redirection.DoesNotExist:
            result = None
        return result

    def create(user_id, url):
        user = User.objects.get(pk=user_id)
        new_redirection = Redirection(unique_id=str(uuid4()), user_id=user.id,
                                      url=url, is_active=True)
        new_redirection.save()

    def change_status(id, value):
        assert value in (True, False)
        redirection = Redirection.objects.get(pk=id)
        redirection.is_active = value
        redirection.save()
