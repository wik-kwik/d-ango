# Generated by Django 4.0.2 on 2022-11-21 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgTwo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
