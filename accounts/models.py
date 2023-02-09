from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user/image")

    def __str__(self):
        return self.first_name


def UserProfileCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(user=user, first_name=user.username)


post_save.connect(UserProfileCreated, sender=User)
