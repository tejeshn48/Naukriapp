# Generated by Django 4.1.2 on 2022-11-23 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
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
                ("name", models.CharField(max_length=30)),
                (
                    "contact_no",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("address", models.TextField(max_length=100)),
                ("DOB", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("P", "Preferred not to say"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "availbility",
                    models.CharField(
                        choices=[
                            ("A", "Actively looking"),
                            ("N", "Not actively looking"),
                            ("O", "offers"),
                        ],
                        max_length=1,
                    ),
                ),
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
                ("name", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=255)),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("date_of_start", models.DateField()),
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
                ("name", models.CharField(max_length=30)),
                ("address", models.TextField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "mobile",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("designation", models.CharField(max_length=30)),
                ("dob", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("P", "Preferred not to say"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Application.company",
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
                ("from_date", models.DateField()),
                ("to_date", models.DateField()),
                (
                    "applicant",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="Application.applicant",
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
                ("title", models.CharField(max_length=30)),
                ("description", models.TextField(max_length=100)),
                ("max_salary", models.FloatField()),
                ("min_salary", models.FloatField()),
                ("employment_type", models.CharField(max_length=20)),
                ("max_experience", models.IntegerField(default=None)),
                ("min_experience", models.IntegerField(default=None)),
                ("city", models.CharField(max_length=255)),
                (
                    "location",
                    location_field.models.plain.PlainLocationField(max_length=63),
                ),
                ("industry_type", models.CharField(max_length=30)),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Application.company",
                    ),
                ),
                (
                    "posted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "skill_type",
                    models.ManyToManyField(blank=True, to="Application.skill"),
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
                ("project_name", models.CharField(max_length=30)),
                ("project_description", models.TextField(max_length=100)),
                ("experience_from", models.DateField()),
                ("experience_to", models.DateField()),
                (
                    "applicant",
                    models.ManyToManyField(blank=True, to="Application.applicant"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="Application.company",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="applicant",
            name="jobs",
            field=models.ForeignKey(
                default=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="Application.job",
            ),
        ),
        migrations.AddField(
            model_name="applicant",
            name="recruiter",
            field=models.ManyToManyField(blank=True, to="Application.recruiter"),
        ),
    ]