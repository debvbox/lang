# Generated by Django 4.1.4 on 2022-12-20 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=55, verbose_name='Zip code')),
                ('phone', models.CharField(max_length=8, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Website Addres')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event name')),
                ('event_date', models.DateTimeField(verbose_name='Event date')),
                ('manager', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('attendees', models.ManyToManyField(blank=True, to='events.myclubuser')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]