from django.db import models


class Posts(models.Model):
    pid = models.AutoField(primary_key=True, null=False)
    pcontent = models.CharField(max_length=100)
    post_time = models.DateTimeField(auto_now_add=True)
    pclass = models.IntegerField()  # 0 is free_post, 1 is group_post

    class Meta:
        verbose_name = "포스트"
        ordering = ["pid", "post_time"]
