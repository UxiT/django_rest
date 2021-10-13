from django.db import models


class ModelUser(models.Model):
    name = models.CharField(verbose_name="Name", max_length=20)
    last_name = models.CharField(
        verbose_name="Last name", max_length=50, blank=True, null=True)
    img = models.CharField(verbose_name="Img link",
                           null=True, blank=True, max_length=200)
    status = models.CharField(verbose_name="Status", max_length=40)
    follow = models.BooleanField(verbose_name="Follow", default=False)
    city = models.CharField(verbose_name="City",
                            max_length=30, null=True, blank=True)
    county = models.CharField(verbose_name="Country",
                              max_length=50, null=True, blank=True)
