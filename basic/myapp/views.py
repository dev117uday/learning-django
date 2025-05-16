from django.shortcuts import render
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, template_name="base.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todo.html", {"todos": items})
