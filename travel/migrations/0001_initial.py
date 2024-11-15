# Generated by Django 5.1.2 on 2024-11-15 06:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('yeb_event', models.CharField(max_length=255)),
                ('from_location', models.CharField(max_length=255)),
                ('to_location', models.CharField(max_length=255)),
                ('pickup', models.CharField(max_length=255)),
                ('drop', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('staff', models.CharField(max_length=255)),
                ('instructions', models.TextField()),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UTravel',
            fields=[
                ('u_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('t_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.travel')),
            ],
        ),
    ]
