from django.db import models


class Calenders(models.Model):
    cid = models.AutoField(primary_key=True, null=False)
    ccontent = models.CharField(max_length=10000)
    cclass = models.IntegerField()  # 0 is personal_post, 1 is group_post

    class Meta:
        verbose_name = "캘린더"
        ordering = ["cid"]