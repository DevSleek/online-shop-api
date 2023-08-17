from rest_framework import routers
from .views import ProductSerializerViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductSerializerViewSet)

urlpatterns = router.urls