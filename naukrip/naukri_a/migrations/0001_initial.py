# Generated by Django 4.1.3 on 2022-11-25 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=100)),
                ("email", models.EmailField(max_length=30)),
                (
                    "mobile_no",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("date_of_birth", models.DateField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "M"), ("F", "F"), ("N", "N")],
                        default=1,
                        max_length=1,
                    ),
                ),
                ("availability", models.CharField(max_length=1)),
                ("jobs", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=20)),
                ("date_of_start", models.DateField(max_length=10)),
                ("description", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(max_length=100)),
                (
                    "applicant",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="naukri_a.applicant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recruiter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=100)),
                ("email", models.EmailField(max_length=30)),
                (
                    "mobile_no",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("designation", models.CharField(max_length=20)),
                ("date_of_birth", models.DateField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "M"), ("F", "F"), ("N", "N")],
                        default=1,
                        max_length=10,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Qualification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField(max_length=100)),
                ("from_start", models.DateField(max_length=10)),
                ("to_end", models.DateField(max_length=10)),
                (
                    "applicant",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.applicant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("description", models.TextField(max_length=100)),
                ("max_salary", models.FloatField()),
                ("min_salary", models.FloatField()),
                ("employment_type", models.CharField(max_length=20)),
                ("max_experience", models.IntegerField()),
                ("min_experience", models.IntegerField()),
                ("location", models.CharField(max_length=50)),
                ("industry_type", models.CharField(max_length=20)),
                (
                    "applicant",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.applicant",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.company",
                    ),
                ),
                (
                    "posted_by",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "skills",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.skill",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=20)),
                ("project_description", models.TextField(max_length=100)),
                ("from_start", models.DateField(max_length=10)),
                ("to_end", models.DateField(max_length=10)),
                (
                    "applicant",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.applicant",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="naukri_a.company",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="applicant",
            name="company",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="naukri_a.company",
            ),
        ),
    ]