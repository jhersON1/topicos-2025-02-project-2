from django.urls import path
from .views import AdaptarContenidoView

urlpatterns = [
    path('adaptar/', AdaptarContenidoView.as_view(), name='adaptar-contenido'),
]