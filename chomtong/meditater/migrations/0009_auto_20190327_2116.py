# Generated by Django 2.1.7 on 2019-03-27 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meditater', '0008_emailmeditater_meditater'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailMeditater',
            new_name='Email',
        ),
    ]
