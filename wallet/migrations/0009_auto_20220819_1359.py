# Generated by Django 2.2.12 on 2022-08-19 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_auto_20220819_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.Transaction'),
        ),
    ]