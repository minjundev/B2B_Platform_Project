from django.db import models


# Create your models here.

class Users(models.Model):
    uid = models.AutoField(primary_key=True, null=False)
    uname = models.CharField(max_length=100, null=False, editable=True)
    id = models.CharField(max_length=18, null=False, editable=True)
    password = models.CharField(max_length=30, null=False, editable=True)
    birthday = models.DateField(editable=True)
    phone = models.CharField(max_length=13, null=True)
    profile_image = models.ImageField(null=True, editable=True)
    email = models.EmailField(blank=False, null=False, editable=True)
    friends = models.ManyToManyField('self', symmetrical=True)
    personal_calender = models.ForeignKey('Calenders.Calenders', on_delete=models.CASCADE, unique=True,
                                          related_name='personal_calender', null=True)

    class Meta:
        verbose_name = "유저"
        ordering = ["uid", "uname"]
        db_table = u'Users'
