# Generated by Django 3.0.8 on 2020-07-09 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitinglist', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
