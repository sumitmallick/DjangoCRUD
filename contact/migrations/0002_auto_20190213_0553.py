# Generated by Django 2.1.7 on 2019-02-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contactno',
            field=models.IntegerField(),
        ),
    ]