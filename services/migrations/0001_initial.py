# Generated by Django 3.0.7 on 2020-08-18 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProvideService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_from', models.CharField(blank=True, max_length=128, null=True)),
                ('service_type', models.CharField(blank=True, choices=[('Delivery', 'Delivery'), ('Pick Up', 'Pick Up'), ('Hosting', 'Hosting')], max_length=128, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('preferences', models.CharField(blank=True, choices=[('Private bedroom', 'Private bedroom'), ('Living room', 'Living room'), ('Common space', 'Common space')], max_length=128, null=True)),
                ('pickup_location', models.CharField(blank=True, max_length=128, null=True)),
                ('drop_off_location', models.CharField(blank=True, max_length=128, null=True)),
                ('arrive_date', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('text', models.TextField(blank=True, max_length=640, null=True)),
                ('status', models.CharField(blank=True, choices=[('Created, not accepted', 'Created, not accepted'), ('Accepted/in process', 'Accepted/in process'), ('Successfully done', 'Successfully done'), ('Not confirmed', 'Not confirmed'), ('Expired', 'Expired'), ('Canceled', 'Canceled')], default='Created, not accepted', max_length=64, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RequestProvideService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='Pending', max_length=64)),
                ('accept', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RequestService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Canceled', 'Canceled')], default='Pending', max_length=64)),
                ('accept', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_from', models.CharField(blank=True, max_length=128, null=True)),
                ('service_type', models.CharField(blank=True, choices=[('Delivery', 'Delivery'), ('Pick Up', 'Pick Up'), ('Hosting', 'Hosting')], max_length=128, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('preferences', models.CharField(blank=True, choices=[('Private bedroom', 'Private bedroom'), ('Living room', 'Living room'), ('Common space', 'Common space')], max_length=128, null=True)),
                ('pickup_location', models.CharField(blank=True, max_length=128, null=True)),
                ('drop_off_location', models.CharField(blank=True, max_length=128, null=True)),
                ('arrive_date', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Created, not accepted', 'Created, not accepted'), ('Accepted/in process', 'Accepted/in process'), ('Successfully done', 'Successfully done'), ('Not confirmed', 'Not confirmed'), ('Expired', 'Expired'), ('Canceled', 'Canceled')], default='Created, not accepted', max_length=64, null=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('text', models.TextField(blank=True, max_length=512, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=512)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services_images')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.Service')),
            ],
        ),
    ]
