from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Animals, Client

# Сериализатор для модели Animals
class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = '__all__'

# Сериализатор для модели Client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# API для списка животных
@api_view(['GET'])
def animals_list(request):
    animals = Animals.objects.all()
    serializer = AnimalsSerializer(animals, many=True)
    return Response(serializer.data)

# API для списка клиентов
@api_view(['GET'])
def clients_list(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
