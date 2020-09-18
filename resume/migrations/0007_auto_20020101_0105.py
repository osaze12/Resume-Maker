# Generated by Django 3.1 on 2002-01-01 09:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_certificate_education_experience_hobbie_info_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='school',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.info'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='year',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxLengthValidator(4), django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='education',
            name='school_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='studied',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.info'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.info'),
        ),
        migrations.AlterField(
            model_name='hobbie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.info'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.info'),
        ),
    ]
