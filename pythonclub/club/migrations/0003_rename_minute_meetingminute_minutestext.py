# Generated by Django 3.2 on 2021-05-14 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_rename_meetingtype_meetingminute_meetingid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingminute',
            old_name='minute',
            new_name='minutestext',
        ),
    ]
