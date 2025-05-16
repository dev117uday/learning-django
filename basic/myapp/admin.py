from django.contrib import admin

# from . import models
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)
