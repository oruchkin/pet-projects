# Generated by Django 3.1.2 on 2021-07-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
