# Generated by Django 4.2.7 on 2023-12-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=100)),
                ('imageURL', models.CharField(blank=True, max_length=100)),
                ('eventDate', models.CharField(max_length=100)),
                ('eventTime', models.CharField(max_length=100)),
                ('venueName', models.CharField(blank=True, max_length=100)),
                ('venueCity', models.CharField(blank=True, max_length=100)),
                ('venueState', models.CharField(blank=True, max_length=100)),
                ('venueAdd', models.CharField(blank=True, max_length=100)),
                ('eventURL', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='eventlist',
            name='imageURL',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='venueAdd',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='venueCity',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='venueName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='venueState',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
