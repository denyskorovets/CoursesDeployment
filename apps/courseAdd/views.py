from django.shortcuts import render, redirect
from .models import Course, Description
# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all(),
        "descriptions": Description.objects.all()
    }
    return render(request, 'courseAdd/index.html', context)


def addcourse(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')


def remove(request, id):
    course = Course.objects.get(id=id)
    context = {
        "toBeDeleted": course
    }
    return render(request, 'courseAdd/delete.html', context)


def delete(request):
    Course.objects.get(id=request.POST["id"]).delete()
    return redirect('/')