# Generated by Django 3.2.7 on 2021-09-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210919_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
