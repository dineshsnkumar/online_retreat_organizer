# Generated by Django 5.1.4 on 2025-02-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0007_recording_retreat_recordings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retreat',
            name='recordings',
        ),
    ]
