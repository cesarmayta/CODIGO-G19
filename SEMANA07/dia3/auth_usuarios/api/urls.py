from django.urls import path

from . import views


urlpatterns=[
    path('',views.IndexView.as_view()),
    path('usuario',views.UsuarioView.as_view()),
    path('usuariotoken',views.TokenView.as_view()),
    path('logintoken',views.LoginTokenView.as_view())
]