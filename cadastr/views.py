from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CadastrRecordSerializer
from .models import CadastrRecord


class CadastrRecordAPICreate(generics.CreateAPIView):
    serializer_class = CadastrRecordSerializer


class CadastrAllRecordsAPIList(generics.ListAPIView):
    serializer_class = CadastrRecordSerializer

    def get_queryset(self):
        cadastral_number = self.request.query_params.get(
            'cadastral_number', None
        )
        if cadastral_number:
            return CadastrRecord.objects.filter(
                cadastral_number=cadastral_number
            )
        return CadastrRecord.objects.all()


class PingView(APIView):
    def get(self, request):
        return Response(
            {"message": "Server is running"}, status=status.HTTP_200_OK
        )


class HistoryRecordsAPIList(generics.ListAPIView):
    queryset = CadastrRecord.objects.all()
    serializer_class = CadastrRecordSerializer
