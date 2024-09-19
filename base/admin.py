from django.contrib import admin
from .models import Animals, Client, Students

# Register your models here.

admin.site.register(Animals)
admin.site.register(Client)
admin.site.register(Students)
