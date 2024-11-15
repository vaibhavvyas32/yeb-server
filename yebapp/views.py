from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from .models import User,UserDetail,Achievement,YebOffer,YebApplication, Accommodation, Announcement, ChatMessage, Schedule, Feedback, Submission, Assignment, Payment, Fee, ParticipantTeam, GroupMessage
from .serializers import UserSerializer, UserDetailSerializer, AchievementSerializer, YebApplicationSerializer, YebOfferSerializer, AccomodationSerializer, AnnouncementSerializer, ChatMessageSerializer, ScheduleSerializer, FeedbackSerializer, SubmissionSerializer, AssignmentSerializer, PaymentSerializer, FeeSerializer, ParticipantTeamSerializer, GroupMessageSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


class RegisterView(APIView):
    def post(self,request):
        u_name = request.data.get("u_name")
        password = request.data.get("password")

        if User.objects.filter(u_name=u_name).exists():
            return Response({"error":" Username already exists"},status= status.HTTP_400_BAD_REQUEST)
        
        # user =  User.objects.create_user(u_name=u_name,password=password)
        user = User(u_name=u_name)
        user.set_password(password)
        user.save()

        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
    



    
class LoginView(APIView):
    def post(self,request):

        u_name = request.data['u_name']
        password = request.data['password']

        user = User.objects.filter(u_name=u_name)

        try:
            user = User.objects.get(u_name=u_name)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        
        payload = {
            'id': user.u_name,
            'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload,'django-insecure-$=v-ffi*=!^zpd$15w47x^o!0b1!sz21o0t!btq)c3u$*b9i)r',algorithm='HS256')


        
        return Response({
            'message': 'Login Successful',
            'token': token
        })

class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

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

# class GDViewSet(viewsets.ModelViewSet):
#     queryset = GD.objects.all()
#     serializer_class = GdSerializer

# class StdGDViewSet(viewsets.ModelViewSet):
#     queryset = StdGD.objects.all()
#     serializer_class = StdGDSerializer

# class TravelViewSet(viewsets.ModelViewSet):
#     queryset = Travel.objects.all()
#     serializer_class = TravelSerializer

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