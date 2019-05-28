from .models import User


class UserService(object):
    def get(id=None, username=None):
        if id is not None:
            return User.objects.get(pk=id)
        elif username is not None:
            return User.objects.get(username=username)
        raise Exception('You should provide username or password')

    def create(username, password):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def delete(id):
        return User.objects.get(pk=id).delete()

    def change_password(id, new_password):
        user = User.objects.get(pk=id)
        user.set_password(new_password)
        user.save()
        return user
