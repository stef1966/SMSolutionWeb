# Generated by Django 4.0.3 on 2022-06-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0017_alter_realestate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
