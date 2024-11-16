# Generated by Django 5.1.2 on 2024-11-16 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('yebapp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('u_key', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='yebapp.user')),
                ('p_name', models.CharField(max_length=255)),
                ('p_email', models.EmailField(max_length=254)),
                ('p_phone', models.CharField(max_length=15)),
                ('school', models.CharField(max_length=255)),
                ('s_address', models.CharField(max_length=255)),
                ('s_city', models.CharField(max_length=100)),
                ('s_state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TG', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli and Daman and Diu'), ('LD', 'Lakshadweep'), ('DL', 'Delhi'), ('PY', 'Puducherry'), ('LA', 'Ladakh')], max_length=50)),
                ('marks', models.JSONField()),
                ('shirt_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large')], max_length=10)),
                ('shirt_color', models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Black', 'Black'), ('White', 'White')], max_length=10)),
            ],
        ),
    ]
