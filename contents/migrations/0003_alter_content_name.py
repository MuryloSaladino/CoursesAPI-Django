# Generated by Django 4.2.6 on 2023-10-31 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
