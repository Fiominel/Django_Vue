# Generated by Django 4.0.1 on 2022-01-31 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='poster',
            field=models.ImageField(default='SOME STRING', upload_to='media/', verbose_name='Постер'),
        ),
    ]
