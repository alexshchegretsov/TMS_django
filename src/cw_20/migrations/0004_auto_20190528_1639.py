# Generated by Django 2.2.1 on 2019-05-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cw_20', '0003_auto_20190523_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profession',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
