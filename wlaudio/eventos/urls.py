from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView, EventAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/',AvaliacaoAPIView.as_view(),name='avaliacoes'),
    path('events/',EventAPIView.as_view(), name="eventos" )
]