# Generated by Django 2.1.7 on 2019-03-27 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meditater', '0009_auto_20190327_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='meditater',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]
