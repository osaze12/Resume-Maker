# Generated by Django 3.1 on 2002-01-03 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20020101_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hobbie',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Hobbie',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
