# yebapp/urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserDetailViewSet, AchievementViewSet, YebOfferViewSet, 
    YebApplicationViewSet, GDViewSet, TravelViewSet, AccommodationViewSet, 
    AnnouncementViewSet, ChatMessageViewSet, ScheduleViewSet, FeedbackViewSet, 
    SubmissionViewSet, AssignmentViewSet, PaymentViewSet, FeeViewSet, 
    ParticipantTeamViewSet, GroupMessageViewSet
)




router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-details', UserDetailViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'yeb-offers', YebOfferViewSet)
router.register(r'yeb-applications', YebApplicationViewSet)
router.register(r'gds', GDViewSet)
router.register(r'travels', TravelViewSet)
router.register(r'accommodations', AccommodationViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'chat-messages', ChatMessageViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'participant-teams', ParticipantTeamViewSet)
router.register(r'group-messages', GroupMessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]