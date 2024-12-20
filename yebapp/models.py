from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self,u_name,password=None,**extra_fields):
#         if not u_name:
#             raise ValueError("the username must be set")
#         # extra_fields.setdefault('is_active')
#         user = self.model(u_name=u_name,**extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
    
#     def create_superuser(self, u_name, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=true")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
        
#         return self.create_user(u_name, password, **extra_fields)
    






class User(AbstractBaseUser):
    u_key = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    mobile_no = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    USERNAME_FIELD = 'u_name'

class Achievement(models.Model):
    u_key = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ach1 = models.CharField(max_length=255)
    ach2 = models.CharField(max_length=255)
    ach3 = models.CharField(max_length=255)


class AchievementPDF(models.Model):
    u_key = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pdf_file = models.FileField(upload_to='achievement_pdfs/')


class StartupQuestion(models.Model):
    u_key = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    startup_name = models.CharField(max_length=255)
    challenges = models.TextField()
    about = models.TextField()


class YebOffer(models.Model):
    yeb_key = models.AutoField(primary_key=True)
    short_desc = models.CharField(max_length=255)
    large_desc = models.TextField()
    campus = models.CharField(max_length=255)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    application_fee = models.IntegerField()
    register_fee = models.IntegerField()
    application_deadline = models.DateField()
    active = models.BooleanField(default=True)


class YebApplication(models.Model):
    u_key = models.ForeignKey(User, on_delete=models.CASCADE)
    yeb_key = models.ForeignKey(YebOffer, on_delete=models.CASCADE)
    application_datetime = models.DateTimeField()
    status = models.CharField(max_length=50)

class Accommodation(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    r_no = models.CharField(max_length=10)
    yeb_event = models.CharField(max_length=255)
    in_date = models.DateField()
    out_date = models.DateField()
    instructions = models.TextField()


class Announcement(models.Model):
    a_id = models.AutoField(primary_key=True)
    states = models.CharField(max_length=255)
    message = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)
    file = models.FileField(upload_to='announcements/', null=True, blank=True)
    link = models.URLField()


class ChatMessage(models.Model):
    c_id = models.AutoField(primary_key=True)
    send_message = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=True)


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    yeb_id = models.ForeignKey(YebOffer, on_delete=models.CASCADE)
    information = models.TextField()
    speaker = models.CharField(max_length=255)
    ppt_link = models.URLField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='schedule_pics/', null=True, blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField()
    active = models.BooleanField(default=True)


class Feedback(models.Model):
    schedule_id = models.OneToOneField(Schedule, on_delete=models.CASCADE, primary_key=True)
    feedback_msg = models.TextField()
    date = models.DateField()
    time = models.TimeField()

class Submission(models.Model):
    a_id = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    s_id = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    link = models.URLField()


class Assignment(models.Model):
    a_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    yeb = models.ForeignKey(YebOffer, on_delete=models.CASCADE)


class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    transaction_id = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Fee(models.Model):
    fee_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    amount = models.IntegerField()
    yeb = models.ForeignKey(YebOffer, on_delete=models.CASCADE)


class ParticipantTeam(models.Model):
    g_id = models.AutoField(primary_key=True)
    yeb_name = models.ForeignKey(YebOffer, on_delete=models.CASCADE)


class GroupMessage(models.Model):
    s_id = models.ForeignKey(ParticipantTeam, on_delete=models.CASCADE)
    message_text = models.TextField()
    active = models.BooleanField(default=True)
    expire_on = models.DateField()

