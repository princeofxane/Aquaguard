# Generated by Django 2.1.7 on 2019-03-01 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190301_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpTarget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('callTarget', models.IntegerField()),
                ('commitTarget', models.IntegerField()),
                ('startingDate', models.CharField(max_length=10, null=True)),
                ('endingDate', models.CharField(max_length=10, null=True)),
                ('employeeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Employee')),
            ],
        ),
    ]
