from django.urls import path

from . import views

urlpatterns = [
    path('producto',views.ProductoView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view())
]