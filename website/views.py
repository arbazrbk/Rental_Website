from django.shortcuts import render
from .models import Property, feedback, register
from django.views.decorators.csrf import csrf_exempt


from .forms import FeedbackForm

def home(request):
    return render(request, 'website/index.html')


def properties(request):
    properties = Property.objects.all()
    return render(request, 'website/properties.html', {'properties': properties})


def services(request):
    return render(request, 'website/services.html')


def about(request):
    return render(request, 'website/about.html')


def testimonials(request):
    feedbacks = feedback.objects.order_by('-id')
    return render(request, 'website/testimonials.html', {'feedback': feedbacks})


def contact(request):
    return render(request, 'website/contact.html')


def feedback_page(request):
    form = FeedbackForm(request.POST or None)
    success = False
    feedback_items = feedback.objects.order_by('-id')[:6]

    if request.method == 'POST' and form.is_valid():
        form.save()
        form = FeedbackForm()
        success = True
        feedback_items = feedback.objects.order_by('-id')[:6]

    return render(request, 'website/feedback.html', {'form': form, 'success': success, 'feedback_items': feedback_items})


def submit_feedback(request):
    return feedback_page(request)