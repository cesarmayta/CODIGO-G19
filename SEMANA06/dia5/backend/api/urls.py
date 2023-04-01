from django.urls import path

from . import views

urlpatterns = [
    path('producto',views.ProductoView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('cliente',views.ClienteView.as_view()),
    path('cliente/<int:cliente_id>',views.ClienteDetailView.as_view()),
    path('factura',views.FacturaView.as_view()),
    path('factura/<int:factura_id>',views.FacturaDetailView.as_view()),
    path('facturadetalle',views.FacturaDetalleView.as_view()),
    path('facturadetalle/<int:factura_detalle_id>',views.FacturaDetalleDetailView.as_view())
]