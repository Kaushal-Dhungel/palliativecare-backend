# Generated by Django 3.2.8 on 2021-10-30 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20211030_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='religion',
        ),
    ]
