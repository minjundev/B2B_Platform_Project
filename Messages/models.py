from django.db import models


# Create your models here.
class Messages(models.Model):
    mid = models.AutoField(primary_key=True, null=False)
    mcontent = models.CharField(max_length=100)
    send_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "메시지"
        ordering = ["send_time"]
