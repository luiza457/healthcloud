# Generated by Django 4.1.7 on 2023-03-26 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(choices=[('Consult', 'Consult'), ('Radiology', 'Radiology')], default='Consult', max_length=50)),
                ('day', models.DateField(choices=[(datetime.date(2023, 3, 26), 'Sunday, March 26'), (datetime.date(2023, 3, 27), 'Monday, March 27'), (datetime.date(2023, 3, 28), 'Tuesday, March 28'), (datetime.date(2023, 3, 29), 'Wednesday, March 29'), (datetime.date(2023, 3, 30), 'Thursday, March 30')], default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM')], default='3 PM', max_length=10)),
            ],
        ),
    ]
