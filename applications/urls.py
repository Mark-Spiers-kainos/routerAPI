from applications.views import ApplicationViewSet
from rest_framework.routers import DefaultRouter


app_name = 'application'

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='application')
urlpatterns = router.urls
