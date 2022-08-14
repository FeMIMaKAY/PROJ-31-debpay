# Generated by Django 4.1 on 2022-08-13 22:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0029_rename_phone_number_school_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='participants',
        ),
        migrations.AddField(
            model_name='meeting_comment',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='Main', to=settings.AUTH_USER_MODEL),
        ),
    ]
