# Generated by Django 4.2.16 on 2024-10-27 07:32

import django.core.validators
from django.db import migrations, models
import final_exam.authors.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), final_exam.authors.validators.AlphaValidator()])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), final_exam.authors.validators.AlphaValidator()])),
                ('passcode', models.CharField(help_text='Your passcode must be a combination of 6 digits', max_length=6, validators=[final_exam.authors.validators.ExactSixDigitsValidator()])),
                ('pets_number', models.PositiveSmallIntegerField()),
                ('info', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
