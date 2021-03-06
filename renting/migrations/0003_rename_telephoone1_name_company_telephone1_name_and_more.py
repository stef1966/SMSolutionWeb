# Generated by Django 4.0.3 on 2022-06-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0002_company_address_country_company_couleur1mois_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='telephoone1_name',
            new_name='telephone1_name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='telephoone1_num',
            new_name='telephone1_num',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='telephoone2_name',
            new_name='telephone2_name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='telephoone2_num',
            new_name='telephone2_num',
        ),
        migrations.AlterField(
            model_name='company',
            name='realestate_id',
            field=models.ManyToManyField(blank=True, through='renting.RealEstate_Company', to='renting.realestate'),
        ),
    ]
