# Generated by Django 4.2.3 on 2023-09-05 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0005_remove_userprofile_role_userprofile_is_gestionnaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_gestionnaire',
        ),
    ]