# Generated by Django 2.2.12 on 2022-07-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20220730_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.CharField(max_length=15)),
                ('Points', models.IntegerField()),
                ('Date_time', models.DateTimeField()),
                ('balance', models.CharField(max_length=15)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
