from rest_framework import serializers


class PoligonoSerializer(serializers.Serializer):
    """ serializador para poligonos """

    campo1 = serializers.CharField()
    campo2 = serializers.CharField()
