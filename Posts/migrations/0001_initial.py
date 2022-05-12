# Generated by Django 4.0.4 on 2022-05-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pcontent', models.CharField(max_length=100)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('pclass', models.IntegerField()),
            ],
            options={
                'verbose_name': '포스트',
                'ordering': ['pid', 'post_time'],
            },
        ),
    ]