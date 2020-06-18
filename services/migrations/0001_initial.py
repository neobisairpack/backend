# Generated by Django 3.0.7 on 2020-06-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service_type', models.CharField(choices=[('Hosting', 'Hosting')], default='Hosting', max_length=32)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=512)),
                ('preferences', models.CharField(choices=[('Private bedroom', 'Private bedroom'), ('Living room', 'Living room'), ('Common space', 'Common space')], max_length=64)),
                ('status', models.CharField(choices=[('Created, not accepted', 'Created, not accepted'), ('Accepted/in process', 'Accepted/in process'), ('Successfully done', 'Successfully done'), ('Not confirmed', 'Not confirmed'), ('Canceled', 'Canceled')], default='Created, not accepted', max_length=64)),
                ('image', models.ImageField(upload_to='')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('Package delivery', 'Package delivery'), ('Airport pick up/drop off', 'Airport pick up/drop off')], max_length=32)),
                ('start_location', models.CharField(max_length=128)),
                ('end_location', models.CharField(max_length=128)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(choices=[('Created, not accepted', 'Created, not accepted'), ('Accepted/in process', 'Accepted/in process'), ('Successfully done', 'Successfully done'), ('Not confirmed', 'Not confirmed'), ('Canceled', 'Canceled')], default='Created, not accepted', max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
    ]
