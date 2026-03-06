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
    feedbacks = feedback.objects.all()
    return render(request, 'website/testimonials.html', {'feedback': feedbacks})


def contact(request):
    return render(request, 'website/contact.html')

def submit_feedback(request):
    if request.method == 'POST':    
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'website/contact.html', {'form': form})
        else:
            return render(request, 'website/contact.html', {'success': False, 'message': 'Invalid form data.'})