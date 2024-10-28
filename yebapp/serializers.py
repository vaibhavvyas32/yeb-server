from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,UserDetail,Achievement,YebOffer,YebApplication,GD,StdGD, Travel, Accommodation, Announcement, ChatMessage, Schedule, Feedback, Submission, Assignment, Payment, Fee, ParticipantTeam, GroupMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate_username(self,value):
        print("validating username:", value)
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        return value
    
    









class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'
    

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class YebOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = YebOffer
        fields = '__all__'

class YebApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = YebApplication
        fields = '__all__'

class GdSerializer(serializers.ModelSerializer):
    class Meta:
        model = GD
        fields = '__all__'

class StdGDSerializer(serializers.ModelSerializer):
    user_marks = serializers.SerializerMethodField()

    class Meta:
        model = StdGD
        fields = ['gd_id','student_id','marks','user_marks']

    def get_user_marks(self,obj):
        user_detail = UserDetail.objects.filter(u_key=obj.student_id).first()
        return user_detail.marks if user_detail else None

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'


class ParticipantTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantTeam
        fields = '__all__'

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = '__all__'

