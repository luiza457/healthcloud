# Generated by Django 4.1.7 on 2023-04-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_alter_appointment_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.CharField(default='description', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='keywords',
            field=models.CharField(default='keyword1,keyword2', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='sample_name',
            field=models.CharField(default='sample', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='transcription',
            field=models.CharField(default='transcriptions', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Allergy / Immunology', 'Allergy / Immunology'), ('Cardiovascular / Pulmonary ', 'Cardiovascular / Pulmonary'), ('Consult - History and Phy.', 'Consult - History and Phy.'), ('Dermatology', 'Dermatology'), ('Endocrinology', 'Endocrinology'), ('Gastroenterology', 'Gastroenterology'), ('General Medicine', 'General Medicine'), ('Genomics', 'Genomics'), ('Hematology', 'Hematology'), ('Immunology', 'Immunology'), ('Infectious Diseases', 'Infectious Diseases'), ('Neurology', 'Neurology'), ('Obstetrics / Gynecology ', 'Obstetrics / Gynecology '), ('Hematology - Oncology', 'Hematology - Oncology'), ('Orthopedic', 'Orthopedic'), ('Psychiatry / Psychology', 'Psychiatry / Psychology'), ('Radiology', 'Radiology'), ('Routine Check-Up', 'Routine Check-Up'), ('Surgery', 'Surgery'), ('Urology', 'Urology'), ('Vaccines', 'Vaccines')], max_length=50),
        ),
    ]
