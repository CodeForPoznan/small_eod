# Generated by Django 3.1.1 on 2020-10-01 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0013_auto_20200722_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='ordering',
        ),
    ]