from django.contrib import admin
from .models import (
    User,
    UserDetail,
    Achievement,
    AchievementPDF,
    StartupQuestion,
    YebOffer,
    YebApplication,
    # GD,
    # StdGD,
    # Travel,
    # UTravel,
    Accommodation,
    Announcement,
    ChatMessage,
    Schedule,
    Feedback,
    Submission,
    Assignment,
    Payment,
    Fee,
    ParticipantTeam,
    GroupMessage,
)
from .forms import MarksForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'u_name', 'first_name', 'last_name', 'dob', 'active')
    search_fields = ('u_name', 'first_name', 'last_name')

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'p_name', 'p_email', 'p_phone', 'school')
    exclude = ['marks']
    form = MarksForm
    search_fields = ('p_name', 'p_email')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'ach1', 'ach2', 'ach3')

@admin.register(AchievementPDF)
class AchievementPDFAdmin(admin.ModelAdmin):
    list_display = ('u_key',)

@admin.register(StartupQuestion)
class StartupQuestionAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'startup_name', 'challenges', 'about')

@admin.register(YebOffer)
class YebOfferAdmin(admin.ModelAdmin):
    list_display = ('yeb_key', 'short_desc', 'campus', 'event_start_date', 'active')
    search_fields = ('short_desc', 'campus')

@admin.register(YebApplication)
class YebApplicationAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'yeb_key', 'application_datetime', 'status')

# @admin.register(GD)
# class GDAdmin(admin.ModelAdmin):
#     list_display = ('gd_id', 'date', 'time', 'link')

# @admin.register(StdGD)
# class StdGDAdmin(admin.ModelAdmin):
#     list_display = ('gd_id', 'student_id', 'marks')
#     form = MarksForm
#     exclude = ['marks']


# @admin.register(Travel)
# class TravelAdmin(admin.ModelAdmin):
#     list_display = ('t_id', 'u_id', 'yeb_event', 'from_location', 'to_location', 'amount')
#     search_fields = ('yeb_event', 'from_location', 'to_location')

# @admin.register(UTravel)
# class UTravelAdmin(admin.ModelAdmin):
#     list_display = ('u_id', 't_id')

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('u_id', 'r_no', 'yeb_event', 'in_date', 'out_date')

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('a_id', 'title', 'active')
    search_fields = ('title', 'message')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'send_message', 'message', 'date', 'time')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_id', 'yeb_id', 'information', 'speaker', 'time_start', 'active')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('schedule_id', 'feedback_msg', 'date', 'time')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('a_id', 's_id', 'datetime', 'link')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('a_id', 'title', 'deadline', 'yeb')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'transaction_id', 'amount', 'date', 'time', 'status')

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('fee_id', 'description', 'amount', 'yeb')

@admin.register(ParticipantTeam)
class ParticipantTeamAdmin(admin.ModelAdmin):
    list_display = ('g_id', 'yeb_name')

@admin.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('s_id', 'message_text', 'active', 'expire_on')
