# Generated by Django 4.1.3 on 2024-10-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krome', '0006_athlete_date_alter_athlete_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
