# Generated by Django 3.2.3 on 2022-05-12 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_name', models.CharField(max_length=225, verbose_name='tutor_name')),
                ('timage', models.ImageField(blank=True, null=True, upload_to='tutors/', verbose_name='timage')),
                ('DOB', models.DateField(verbose_name='DOB')),
                ('Gender', models.CharField(max_length=225, verbose_name='Gender')),
                ('Qualification', models.CharField(max_length=225, verbose_name='Qualification')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('contactno', models.CharField(max_length=150, verbose_name='contactno')),
            ],
        ),
        migrations.CreateModel(
            name='userClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade', models.CharField(max_length=50, verbose_name='Grade')),
                ('fees', models.IntegerField(verbose_name='fees')),
                ('questionpaper', models.ImageField(blank=True, null=True, upload_to='qpaper/', verbose_name='questionpaper')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coachingapp.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Studentname', models.CharField(max_length=150, verbose_name='Studentname')),
                ('DOB', models.DateField(max_length=150, verbose_name='DOB')),
                ('Gender', models.CharField(max_length=150, verbose_name='Gender')),
                ('Parentname', models.CharField(max_length=150, verbose_name='Parentname')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('contactno', models.CharField(max_length=150, verbose_name='contactno')),
                ('simage', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='simage')),
                ('Grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coachingapp.userclass')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
