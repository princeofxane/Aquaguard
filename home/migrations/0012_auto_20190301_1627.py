# Generated by Django 2.1.7 on 2019-03-01 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190228_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='type',
            new_name='role',
        ),
    ]
