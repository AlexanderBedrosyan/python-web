# Generated by Django 4.2.16 on 2024-10-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='Nema', max_length=25, null=True),
        ),
    ]
