# Generated by Django 3.1.7 on 2021-04-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('classTracker', '0002_auto_20210427_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='course_no',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='is_lab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='section_no',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='meeting_times',
            field=models.CharField(default='', max_length=200),
        ),
    ]
