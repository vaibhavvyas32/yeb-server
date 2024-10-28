from django.shortcuts import render
from rest_framework import viewsets
from .models import User,UserDetail,Achievement,YebOffer,YebApplication,GD,StdGD, Travel, Accommodation, Announcement, ChatMessage, Schedule, Feedback, Submission, Assignment, Payment, Fee, ParticipantTeam, GroupMessage
from .serializers import UserSerializer, UserDetailSerializer, AchievementSerializer, YebApplicationSerializer, YebOfferSerializer, GdSerializer,StdGDSerializer, TravelSerializer, AccomodationSerializer, AnnouncementSerializer, ChatMessageSerializer, ScheduleSerializer, FeedbackSerializer, SubmissionSerializer, AssignmentSerializer, PaymentSerializer, FeeSerializer, ParticipantTeamSerializer, GroupMessageSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class YebOfferViewSet(viewsets.ModelViewSet):
    queryset = YebOffer.objects.all()
    serializer_class = YebOfferSerializer

class YebApplicationViewSet(viewsets.ModelViewSet):
    queryset = YebApplication.objects.all()
    serializer_class = YebApplicationSerializer

class GDViewSet(viewsets.ModelViewSet):
    queryset = GD.objects.all()
    serializer_class = GdSerializer

class StdGDViewSet(viewsets.ModelViewSet):
    queryset = StdGD.objects.all()
    serializer_class = StdGDSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccomodationSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class ParticipantTeamViewSet(viewsets.ModelViewSet):
    queryset = ParticipantTeam.objects.all()
    serializer_class = ParticipantTeamSerializer

class GroupMessageViewSet(viewsets.ModelViewSet):
    queryset = GroupMessage.objects.all()    
    serializer_class = GroupMessageSerializer