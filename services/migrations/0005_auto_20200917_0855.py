# Generated by Django 2.2 on 2020-09-17 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20200917_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceimage',
            name='post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.Service'),
        ),
    ]
