from django.db import models


class Groups(models.Model):
    gid = models.AutoField(primary_key=True, null=False)
    gname = models.CharField(max_length=100, null=False, editable=True)
    gcontent = models.CharField(max_length=200, null=True, editable=True)
    group_calender = models.OneToOneField('Calenders.Calenders', on_delete=models.CASCADE,
                                          related_name='group_calender', unique=True, null=True)

    class Meta:
        verbose_name = "그룹"
        ordering = ["gid", "gname"]
        db_table = u'Groups'
