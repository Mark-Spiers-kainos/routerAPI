from good.views import GoodViewSet
from rest_framework.routers import DefaultRouter


app_name = 'good'

router = DefaultRouter()
router.register(r'', GoodViewSet, basename='application')
urlpatterns = router.urls
