import datetime

from django.db import connection
from django.http.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import PoligonoSerializer


class Lista_Poligonos(ListAPIView):
    #permission_classes = (IsAuthenticated, )
    serializer_class = PoligonoSerializer

    def get_queryset(self):
        cursor = connection.cursor()
        sql = 'SELECT * FROM dev.sectorial;'

        cursor.execute(sql)
        queryset = cursor.fetchall()

        serializer = PoligonoSerializer(queryset, many=True)
        return Response(serializer.data)
