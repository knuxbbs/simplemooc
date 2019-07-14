from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactForm

# Create your views here.


def index(request):
    courses = Course.objects.all()

    return render(request, 'courses/index.html', {'courses': courses})


def get_by_id(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    context = {
        'course': course,
        'form': ContactForm()
    }

    return render(request, 'courses/details.html', context)


def get_by_slug(request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactForm()
    else:
        form = ContactForm()

    context['form'] = form

    return render(request, 'courses/details.html', context)
