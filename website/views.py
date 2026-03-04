from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from dreamhome.website.forms import FeedbackForm

def home(request):
    return render(request, 'website/index.html')


def properties(request):
    """Properties page view"""
    return render(request, 'website/properties.html')


def services(request):
    return render(request, 'website/services.html')


def about(request):
    return render(request, 'website/about.html')


def testimonials(request):
    user = request.user
    feedback = feedback.objects.filter(user=user)
    return render(request, 'website/testimonials.html', {'feedback': feedback})


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