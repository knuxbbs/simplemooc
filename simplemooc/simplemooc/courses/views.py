from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def index(request):
    courses = Course.objects.all()

    return render(request, 'courses/index.html', {'courses': courses})


def get_by_id(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, 'courses/details.html', {'course': course})


def get_by_slug(request, slug):
    course = get_object_or_404(Course, slug=slug)

    return render(request, 'courses/details.html', {'course': course})
