# Generated by Django 4.0.3 on 2022-06-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0004_alter_company_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='payment_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
