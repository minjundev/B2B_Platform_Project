from django.db import models


class Posts(models.Model):
    pid = models.AutoField(primary_key=True, null=False)
    pcontent = models.CharField(max_length=1000)
    post_time = models.DateTimeField(auto_now_add=True)
    pclass = models.IntegerField()  # 0 is free_post, 1 is group_post
    writer = models.ForeignKey('Users.Users', on_delete=models.CASCADE, related_name='writer', null=True)

    class Meta:
        verbose_name = "포스트"
        ordering = ["pid", "post_time"]
        db_table = u'Posts'
