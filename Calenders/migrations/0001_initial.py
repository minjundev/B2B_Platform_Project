# Generated by Django 4.0.4 on 2022-05-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calenders',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('ccontent', models.CharField(max_length=10000)),
                ('cclass', models.IntegerField()),
            ],
            options={
                'verbose_name': '캘린더',
                'ordering': ['cid'],
            },
        ),
    ]
