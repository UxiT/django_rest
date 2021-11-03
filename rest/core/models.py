from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyUser(User):
    img = models.CharField(verbose_name="Img link",
                           null=True, blank=True, max_length=200)
    status = models.CharField(verbose_name="Status", max_length=40)
    city = models.CharField(verbose_name="City",
                            max_length=30, null=True, blank=True)
    county = models.CharField(verbose_name="Country",
                              max_length=50, null=True, blank=True)