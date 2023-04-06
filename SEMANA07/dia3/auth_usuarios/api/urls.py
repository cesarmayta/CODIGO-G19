from django.urls import path

from . import views


urlpatterns=[
    path('',views.IndexView.as_view()),
    path('usuario',views.UsuarioView.as_view())
]