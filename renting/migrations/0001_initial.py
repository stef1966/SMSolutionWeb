# Generated by Django 4.0.3 on 2022-05-28 14:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French')], default='fr', max_length=100)),
                ('units', models.CharField(choices=[('met', 'Metric'), ('imp', 'Imperial')], default='metric', max_length=20)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address_street_num', models.CharField(blank=True, max_length=20, null=True)),
                ('address_street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address_city', models.CharField(blank=True, max_length=100, null=True)),
                ('address_province', models.CharField(blank=True, max_length=30, null=True)),
                ('address_postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('page_web', models.CharField(blank=True, max_length=100, null=True)),
                ('telephoone1_name', models.CharField(blank=True, max_length=50, null=True)),
                ('telephoone1_num', models.CharField(blank=True, max_length=20, null=True)),
                ('telephoone2_name', models.CharField(blank=True, max_length=50, null=True)),
                ('telephoone2_num', models.CharField(blank=True, max_length=20, null=True)),
                ('contact1_firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('contact1_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('contact1_email', models.CharField(blank=True, max_length=100, null=True)),
                ('contact1_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('contact1_cell', models.CharField(blank=True, max_length=20, null=True)),
                ('contact2_firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('contact2_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('contact2_email', models.CharField(blank=True, max_length=100, null=True)),
                ('contact2_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('contact2_cell', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('inv_letters_before', models.CharField(blank=True, max_length=10, null=True)),
                ('inv_add_year', models.BooleanField(blank=True, default=False, null=True)),
                ('inv_length', models.IntegerField(blank=True, default=0, null=True)),
                ('inv_advise_days_bf', models.IntegerField(blank=True, default=0, null=True)),
                ('taxes1_name', models.CharField(blank=True, max_length=20, null=True)),
                ('taxes1_num', models.CharField(blank=True, max_length=50, null=True)),
                ('taxes1_pourc', models.IntegerField(blank=True, default=0, null=True)),
                ('taxes2_name', models.CharField(blank=True, max_length=20, null=True)),
                ('taxes2_num', models.CharField(blank=True, max_length=50, null=True)),
                ('taxes2_pourc', models.IntegerField(blank=True, default=0, null=True)),
                ('taxes3_name', models.CharField(blank=True, max_length=20, null=True)),
                ('taxes3_num', models.CharField(blank=True, max_length=50, null=True)),
                ('taxes3_pourc', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('reference', models.CharField(max_length=200)),
                ('sentence_en', models.TextField()),
                ('sentence_fr', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('demo_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('source_link', models.CharField(blank=True, max_length=2000, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('type', models.CharField(choices=[('room', 'Room'), ('whareouse', 'Wharehouse'), ('building', 'Building'), ('house', 'House'), ('self_storage', 'Self storage')], max_length=40)),
                ('commercial', models.BooleanField(blank=True, default=False, null=True)),
                ('number', models.CharField(blank=True, max_length=100, null=True)),
                ('page_web', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.project')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate_Company',
            fields=[
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('related_RealEstate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.realestate')),
                ('related_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renting.company')),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='company_id',
            field=models.ManyToManyField(through='renting.RealEstate_Company', to='renting.company'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='renting.tag'),
        ),
        migrations.AddField(
            model_name='company',
            name='realestate_id',
            field=models.ManyToManyField(through='renting.RealEstate_Company', to='renting.realestate'),
        ),
    ]
