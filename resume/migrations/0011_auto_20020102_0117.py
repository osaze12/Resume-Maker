# Generated by Django 3.1 on 2002-01-02 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20020103_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=9),
        ),
    ]