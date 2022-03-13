from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from consumer.serializers import UserSerializer, LogSerializer
from rest_framework.permissions import IsAuthenticated
import requests
from django.conf import settings
from drf_api_logger.models import APILogsModel


class ListUsers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        
        try:
            req = requests.get(settings.URL_GET)
            users = req.json()[:5]
            serializer = UserSerializer(data=users, many=True)
            if serializer.is_valid():
                return Response(serializer.data)
            return Response({'error': f'reason: {serializer.errors}'}, status=400)
        except Exception as e:
            return Response({'error': f'reason: {e}'}, status=400)


class LogListView(generics.ListAPIView):
    queryset = APILogsModel.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]