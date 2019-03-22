# Generated by Django 2.1.7 on 2019-03-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='customerID',
        ),
        migrations.RemoveField(
            model_name='services',
            name='technicianID',
        ),
        migrations.RenameField(
            model_name='complaints',
            old_name='request_date',
            new_name='createdDate',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='id',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='req_id',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='technician',
        ),
        migrations.AddField(
            model_name='complaints',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='complaints',
            name='appointmentTime',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='complaints',
            name='bookingID',
            field=models.CharField(default=None, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='complaints',
            name='customerID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Leads'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='location',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='complaints',
            name='pincode',
            field=models.CharField(default='000000', max_length=6),
        ),
        migrations.AddField(
            model_name='complaints',
            name='technicianID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Employee'),
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
