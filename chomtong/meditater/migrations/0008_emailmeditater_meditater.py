# Generated by Django 2.1.7 on 2019-03-27 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meditater', '0007_remove_emailmeditater_meditater'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmeditater',
            name='meditater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meditaters', to='meditater.Meditater'),
        ),
    ]