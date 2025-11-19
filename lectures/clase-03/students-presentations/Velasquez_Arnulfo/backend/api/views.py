# backend/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .llm_service import adaptar_contenido_con_gemini # Importamos la función síncrona
# Ya no necesitamos 'asyncio'

class AdaptarContenidoView(APIView):
    """
    Endpoint de API para adaptar contenido usando Gemini.
    """
    
    # El método 'post' es síncrono (normal)
    def post(self, request, *args, **kwargs):
        titulo = request.data.get('titulo')
        contenido = request.data.get('contenido')

        if not titulo or not contenido:
            return Response(
                {"error": "Se requieren 'titulo' y 'contenido'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Llamada directa síncrona (sin asyncio.run)
            resultado = adaptar_contenido_con_gemini(titulo, contenido)
            
            if "error" in resultado:
                return Response(resultado, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
            return Response(resultado, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"Error interno del servidor: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )