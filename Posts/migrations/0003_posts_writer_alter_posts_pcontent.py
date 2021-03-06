# Generated by Django 4.0.4 on 2022-05-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_users_friends_users_personal_calender_and_more'),
        ('Posts', '0002_alter_posts_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer', to='Users.users'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pcontent',
            field=models.CharField(max_length=1000),
        ),
    ]
