# Generated by Django 4.0.4 on 2022-05-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Calenders', '0003_alter_calenders_table'),
        ('Groups', '0002_alter_groups_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='group_calender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_calender', to='Calenders.calenders', unique=True),
        ),
    ]
