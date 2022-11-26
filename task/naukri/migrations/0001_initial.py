# Generated by Django 4.1.3 on 2022-11-26 08:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('availability', models.IntegerField(choices=[(1, 'Not Active'), (2, 'Active')])),
                ('dob', models.DateField(blank=True)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.TextField()),
                ('date_of_start', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('from_date', models.DateField(blank=True)),
                ('to_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('designation', models.TextField()),
                ('dob', models.DateField()),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male')])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.company')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('max_salary', models.FloatField(max_length=20)),
                ('min_salary', models.FloatField(max_length=20)),
                ('employment_type', models.IntegerField(choices=[(1, 'Fulltime'), (2, 'Parttime')])),
                ('max_experience', models.IntegerField()),
                ('min_experience', models.IntegerField()),
                ('location', models.TextField()),
                ('industry_type', models.IntegerField(choices=[(1, 'Computer and IT'), (2, 'Management')])),
                ('company', models.ManyToManyField(blank=True, to='naukri.company')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.applicant')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.company')),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naukri.company'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='job',
            field=models.ManyToManyField(to='naukri.job'),
        ),
    ]
