from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    profile_img = models.CharField(max_length=80, verbose_name="img link", blank=True, null=True)
    status = models.CharField(max_length=80, verbose_name="user status", blank=True, null=True)
    country = models.CharField(max_length=30, verbose_name="Country", blank=True, null=True)
    city = models.CharField(max_length=40, verbose_name="City", blank=True, null=True)


# class Posts(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     post_text = models.TextField(max_length=500)