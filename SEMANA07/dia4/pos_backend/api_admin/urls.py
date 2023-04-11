from rest_framework.routers import DefaultRouter

from . import views

router  = DefaultRouter()

router.register(r'mesa',views.MesaViewSet,basename='mesas')

urlpatterns = router.urls