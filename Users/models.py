from django.db import models


# Create your models here.

class Users(models.Model):
    uid = models.AutoField(primary_key=True, null=False)
    uname = models.CharField(max_length=100, null=False, editable=True)
    id = models.CharField(max_length=18, null=False, editable=True)
    password = models.CharField(max_length=30, null=False, editable=True)
    birthday = models.DateField(editable=True)
    phone = models.CharField(max_length=13, null=True)
    # profile_image = models.ImageField(blank=False, null=True, editable=True)
    email = models.EmailField(blank=False, null=False, editable=True)

    class Meta:
        verbose_name = "유저"
        ordering = ["uid", "uname"]
