from rest_framework.routers import DefaultRouter
from .views import TravelViewSet, UTravelViewSet

router = DefaultRouter()
router.register(r'travels', TravelViewSet)
router.register(r'utravel', UTravelViewSet)

urlpatterns = router.urls