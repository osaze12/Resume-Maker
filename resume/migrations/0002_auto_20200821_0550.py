# Generated by Django 3.1 on 2020-08-21 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='user',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(4), django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.DeleteModel(
            name='Hobbies',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]
