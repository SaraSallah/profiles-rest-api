# Generated by Django 2.2 on 2025-05-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_Active',
            new_name='is_active',
        ),
    ]
