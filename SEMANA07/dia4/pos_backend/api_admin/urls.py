from rest_framework.routers import DefaultRouter

from . import views

router  = DefaultRouter()

router.register(r'mesa',views.MesaViewSet,basename='mesas')
router.register(r'categoria',views.CategoriaViewSet,basename='categorias')
router.register(r'plato',views.PlatoViewSet,basename='platos')

urlpatterns = router.urls