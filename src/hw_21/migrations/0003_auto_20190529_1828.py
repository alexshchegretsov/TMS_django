# Generated by Django 2.2.1 on 2019-05-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_21', '0002_auto_20190529_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.TimeField(),
        ),
    ]
