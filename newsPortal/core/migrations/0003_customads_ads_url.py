# Generated by Django 3.2.7 on 2021-10-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customads_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='customads',
            name='ads_url',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
    ]
