# Generated by Django 5.1.1 on 2024-09-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='arrival_time',
            field=models.DateTimeField(null=True),
        ),
    ]