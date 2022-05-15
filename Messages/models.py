from django.db import models


# Create your models here.
class Messages(models.Model):
    mid = models.AutoField(primary_key=True, null=False)
    mcontent = models.CharField(max_length=100)
    send_time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('Users.Users', on_delete=models.CASCADE, unique=True, related_name='sender', null=True)
    receiver = models.ForeignKey('Users.Users', on_delete=models.CASCADE, related_name='receiver', null=True)

    class Meta:
        verbose_name = "메시지"
        ordering = ["mid", "send_time"]
        db_table = u'Messages'
