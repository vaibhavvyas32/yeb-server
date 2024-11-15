from django.db import models
from yebapp.models import User


class UserDetail(models.Model):
    SHIRT_SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]
    SHIRT_COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Black', 'Black'),
        ('White', 'White'),
    ]
    STATE_CHOICES = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UT', 'Uttarakhand'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('LD', 'Lakshadweep'),
    ('DL', 'Delhi'),
    ('PY', 'Puducherry'),
    ('LA', 'Ladakh'),
    ]

    u_key = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    p_name = models.CharField(max_length=255)
    p_email = models.EmailField()
    p_phone = models.CharField(max_length=15)
    school = models.CharField(max_length=255)
    s_address = models.CharField(max_length=255)
    s_city = models.CharField(max_length=100)
    s_state = models.CharField(max_length=50, choices=STATE_CHOICES)
    marks = models.JSONField()
    shirt_size = models.CharField(max_length=10, choices=SHIRT_SIZE_CHOICES)
    shirt_color = models.CharField(max_length=10, choices=SHIRT_COLOR_CHOICES)
