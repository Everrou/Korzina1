# Generated by Django 4.2.7 on 2023-12-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]