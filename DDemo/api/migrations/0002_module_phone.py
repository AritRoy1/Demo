# Generated by Django 4.2 on 2023-12-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]