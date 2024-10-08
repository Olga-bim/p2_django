from django.db import models

# Модель животных
class Animals(models.Model):
    category = models.CharField(max_length=20, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)  # Увеличил длину для описания
    price = models.DecimalField(max_digits=7, decimal_places=2)  # Увеличил макс. цифры для цены
    createdTime = models.DateTimeField(auto_now_add=True)
    fields = ['category','desc','price']

    def __str__(self):
        return self.desc  # Отображаем описание животного

# Модель клиента
class Client(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    telefon = models.CharField(max_length=10, null=True, blank=True)  # Телефон обычно короче
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)  # Связь с животным
    createdTime = models.DateTimeField(auto_now_add=True)
    fields = ['name','telefon','animal']

    def __str__(self):
        return self.name  # Отображаем имя клиента

# Модель студентов
class Students(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)  
    age = models.CharField(max_length=20, null=True, blank=True)  
    fields = ['name','email','age']

    def __str__(self):
        return self.email  # Отображаем имя клиента
