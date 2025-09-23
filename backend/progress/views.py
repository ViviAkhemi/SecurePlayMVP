# progress/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Exemplo simples de resposta
        data = {"progress": "Aqui vai o progresso do usuário"}
        return Response(data)
