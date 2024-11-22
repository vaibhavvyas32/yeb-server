from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserDetailViewSet

router = DefaultRouter()
router.register(r'user-details', UserDetailViewSet)

urlpatterns = router.urls