# Generated by Django 3.1.2 on 2021-07-31 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0003_auto_20210728_2108'),
        ('patient', '0003_auto_20210731_0856'),
        ('insurancecompany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_status_code', models.CharField(max_length=8)),
                ('status_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_number', models.IntegerField(primary_key=True, serialize=False)),
                ('details', models.TextField()),
                ('update_date', models.DateField()),
                ('claim_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='claims.claimstatus')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('insurance_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurancecompany.company')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
