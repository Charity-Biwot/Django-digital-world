# Generated by Django 4.1 on 2022-09-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0020_alter_customer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='signature',
            field=models.ImageField(max_length=15, null=True, upload_to=''),
        ),
    ]
