from django.urls import path

from . import views

urlpatterns = [
    path('',views.TareaView.as_view()),
    path('<int:pk>',views.TareaDetailView.as_view())
]