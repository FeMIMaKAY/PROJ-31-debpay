# Generated by Django 4.0.5 on 2022-08-13 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0025_school_session_alter_school_founded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='Founded',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Number_of_students',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Number_of_teachers',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Permanent_address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Phone_numnber',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Reg_number',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Registered_session',
        ),
        migrations.RemoveField(
            model_name='school',
            name='School_owner',
        ),
        migrations.RemoveField(
            model_name='school',
            name='Session',
        ),
        migrations.RemoveField(
            model_name='school',
            name='current_address',
        ),
        migrations.CreateModel(
            name='School_owner_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_owner', models.CharField(max_length=255)),
                ('School_owner_pics', models.ImageField(default='fixed.jpg', upload_to='school_owner_pics')),
                ('Phone_numnber', models.IntegerField(null=True)),
                ('Number_of_students', models.IntegerField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School_info_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number_of_teachers', models.IntegerField(null=True)),
                ('Founded', models.CharField(max_length=100, null=True)),
                ('Session', models.CharField(max_length=100, null=True)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School_info_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_number', models.CharField(max_length=255)),
                ('Registered_session', models.CharField(max_length=255, null=True)),
                ('current_address', models.CharField(max_length=255, null=True)),
                ('Permanent_address', models.CharField(max_length=255, null=True)),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
