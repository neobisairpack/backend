# Generated by Django 2.2 on 2020-09-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200906_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='canceled_posts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_posts',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
