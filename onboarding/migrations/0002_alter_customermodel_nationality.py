# Generated by Django 5.0.6 on 2024-05-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='nationality',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]
