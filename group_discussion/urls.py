from group_discussion.views import GDViewSet, StdGDViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'gds', GDViewSet)
router.register(r'std-gd', StdGDViewSet)


urlpatterns = router.urls