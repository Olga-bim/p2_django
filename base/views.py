from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import serializers
from .models import Animals, Client, Students

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

# Сериализатор для модели Students
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'        

# API для списка животных и создания нового животного
@api_view(['GET', 'POST'])
def animals_list(request):
    if request.method == 'GET':
        animals = Animals.objects.all()
        serializer = AnimalsSerializer(animals, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AnimalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для получения информации о животном
@api_view(['GET'])
def animal_detail_get(request, pk):
    try:
        animal = Animals.objects.get(pk=pk)
    except Animals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AnimalsSerializer(animal)
    return Response(serializer.data)

# API для обновления информации о животном
@api_view(['PUT'])
def animal_detail_put(request, pk):
    try:
        animal = Animals.objects.get(pk=pk)
    except Animals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AnimalsSerializer(animal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для удаления животного
@api_view(['DELETE'])
def animal_detail_delete(request, pk):
    try:
        animal = Animals.objects.get(pk=pk)
    except Animals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    animal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# API для списка клиентов и создания нового клиента
@api_view(['GET', 'POST'])
def clients_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для получения информации о клиенте
@api_view(['GET'])
def client_detail_get(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client)
    return Response(serializer.data)

# API для обновления информации о клиенте
@api_view(['PUT'])
def client_detail_put(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для удаления клиента
@api_view(['DELETE'])
def client_detail_delete(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# API для списка студентов и создания нового студента
@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для получения информации о студенте
@api_view(['GET'])
def students_detail_get(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentsSerializer(student)
    return Response(serializer.data)

# API для обновления информации о студенте
@api_view(['PUT'])
def students_detail_put(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentsSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API для удаления студента
@api_view(['DELETE'])
def students_detail_delete(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)