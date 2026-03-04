from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


PROPERTIES = [
    {
        'id': 1,
        'image': 'website/images/property-1.jpg',
        'title': 'Modern City Apartment',
        'location': 'Downtown, New York',
        'price': '$2,500/month',
        'type': 'Rent',
        'beds': 2,
        'baths': 2,
        'sqft': 1200,
        'featured': True,
    },
    {
        'id': 2,
        'image': 'website/images/property-2.jpg',
        'title': 'Charming Family Home',
        'location': 'Suburbs, Chicago',
        'price': '$450,000',
        'type': 'Sale',
        'beds': 4,
        'baths': 3,
        'sqft': 2800,
        'featured': False,
    },
    {
        'id': 3,
        'image': 'website/images/property-3.jpg',
        'title': 'Luxury Villa with Pool',
        'location': 'Beverly Hills, LA',
        'price': '$8,500/month',
        'type': 'Rent',
        'beds': 5,
        'baths': 4,
        'sqft': 4500,
        'featured': True,
    },
    {
        'id': 4,
        'image': 'website/images/property-4.jpg',
        'title': 'Penthouse Suite',
        'location': 'Manhattan, New York',
        'price': '$1,200,000',
        'type': 'Sale',
        'beds': 3,
        'baths': 3,
        'sqft': 2200,
        'featured': True,
    },
    {
        'id': 5,
        'image': 'website/images/property-5.jpg',
        'title': 'Cozy Cottage',
        'location': 'Countryside, Vermont',
        'price': '$1,800/month',
        'type': 'Rent',
        'beds': 2,
        'baths': 1,
        'sqft': 900,
        'featured': False,
    },
    {
        'id': 6,
        'image': 'website/images/property-6.jpg',
        'title': 'Modern Minimalist Home',
        'location': 'Austin, Texas',
        'price': '$650,000',
        'type': 'Sale',
        'beds': 3,
        'baths': 2,
        'sqft': 1800,
        'featured': False,
    },
]

# Services data
SERVICES = [
    {
        'icon': 'home',
        'title': 'Property Sales',
        'description': 'Sell your property with confidence. We provide market analysis, professional photography, and strategic marketing to get you the best price.',
        'features': ['Market Value Assessment', 'Professional Staging', 'Targeted Marketing'],
        'color': 'blue',
    },
    {
        'icon': 'key',
        'title': 'House Rentals',
        'description': 'Find the perfect rental home or let us manage your property. We handle tenant screening, contracts, and maintenance.',
        'features': ['Tenant Screening', 'Lease Management', '24/7 Support'],
        'color': 'green',
    },
    {
        'icon': 'trending',
        'title': 'Investment Consulting',
        'description': 'Make smart real estate investments with our expert guidance. We analyze market trends and identify profitable opportunities.',
        'features': ['Market Analysis', 'ROI Projections', 'Portfolio Growth'],
        'color': 'orange',
    },
    {
        'icon': 'shield',
        'title': 'Property Management',
        'description': 'Full-service property management for landlords. From rent collection to maintenance, we handle it all.',
        'features': ['Rent Collection', 'Maintenance', 'Legal Compliance'],
        'color': 'purple',
    },
    {
        'icon': 'users',
        'title': 'Buyer Representation',
        'description': 'Let us be your advocate in the buying process. We negotiate on your behalf and ensure you get the best deal.',
        'features': ['Price Negotiation', 'Due Diligence', 'Closing Support'],
        'color': 'pink',
    },
    {
        'icon': 'file',
        'title': 'Legal Assistance',
        'description': 'Navigate the legal complexities of real estate with our expert guidance on contracts, permits, and regulations.',
        'features': ['Contract Review', 'Permit Guidance', 'Title Transfer'],
        'color': 'cyan',
    },
]

# Testimonials data
TESTIMONIALS = [
    {
        'id': 1,
        'name': 'Sarah Johnson',
        'role': 'Home Buyer',
        'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&h=150&fit=crop&crop=face',
        'content': 'DreamHome Realty made our home buying experience absolutely wonderful. They listened to our needs and found us the perfect family home within our budget. Highly recommended!',
        'rating': 5,
    },
    {
        'id': 2,
        'name': 'Michael Chen',
        'role': 'Property Investor',
        'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face',
        'content': 'As an investor, I need a team that understands the market. DreamHome has consistently helped me identify profitable properties and maximize my returns. Exceptional service!',
        'rating': 5,
    },
    {
        'id': 3,
        'name': 'Emily Rodriguez',
        'role': 'First-time Renter',
        'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face',
        'content': 'Being a first-time renter was scary, but the team at DreamHome guided me through every step. They found me a beautiful apartment and made the process so smooth.',
        'rating': 5,
    },
    {
        'id': 4,
        'name': 'David Thompson',
        'role': 'Home Seller',
        'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face',
        'content': 'Sold my house in just two weeks! The marketing strategy and professional photography they provided made all the difference. Got above asking price too!',
        'rating': 5,
    },
    {
        'id': 5,
        'name': 'Lisa Park',
        'role': 'Property Owner',
        'image': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&h=150&fit=crop&crop=face',
        'content': 'Their property management service is top-notch. I have been working with them for 3 years and my properties are always well-maintained with great tenants.',
        'rating': 5,
    },
    {
        'id': 6,
        'name': 'James Wilson',
        'role': 'Relocating Professional',
        'image': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop&crop=face',
        'content': 'Moving to a new city for work was stressful, but DreamHome made finding a rental so easy. They understood my timeline and found exactly what I needed.',
        'rating': 5,
    },
]

# Contact info
CONTACT_INFO = [
    {
        'icon': 'map',
        'title': 'Visit Us',
        'details': ['123 Real Estate Avenue', 'New York, NY 10001'],
    },
    {
        'icon': 'phone',
        'title': 'Call Us',
        'details': ['+1 (555) 123-4567', '+1 (555) 987-6543'],
    },
    {
        'icon': 'mail',
        'title': 'Email Us',
        'details': ['info@dreamhome.com', 'support@dreamhome.com'],
    },
    {
        'icon': 'clock',
        'title': 'Office Hours',
        'details': ['Mon - Fri: 9AM - 6PM', 'Sat: 10AM - 4PM'],
    },
]


def home(request):
    """Home page view with all sections"""
    context = {
        'properties': PROPERTIES,
        'services': SERVICES,
        'testimonials': TESTIMONIALS,
        'contact_info': CONTACT_INFO,
        'hero_image': 'website/images/hero-house.jpg',
    }
    return render(request, 'website/index.html', context)


def properties(request):
    """Properties page view"""
    filter_type = request.GET.get('type', 'All')
    
    if filter_type == 'All':
        filtered_properties = PROPERTIES
    else:
        filtered_properties = [p for p in PROPERTIES if p['type'] == filter_type]
    
    context = {
        'properties': filtered_properties,
        'filter_type': filter_type,
        'filter_options': ['All', 'Rent', 'Sale'],
    }
    return render(request, 'website/properties.html', context)


def services(request):
    """Services page view"""
    context = {
        'services': SERVICES,
    }
    return render(request, 'website/services.html', context)


def about(request):
    """About page view"""
    context = {
        'achievements': [
            'Over 10 years of industry experience',
            '500+ properties sold and rented',
            'Award-winning customer service',
            'Expert local market knowledge',
        ],
        'stats': [
            {'value': '500+', 'label': 'Properties'},
            {'value': '300+', 'label': 'Happy Clients'},
            {'value': '15+', 'label': 'Awards Won'},
        ],
    }
    return render(request, 'website/about.html', context)


def testimonials(request):
    """Testimonials page view"""
    context = {
        'testimonials': TESTIMONIALS,
    }
    return render(request, 'website/testimonials.html', context)


def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        # For now, just return success
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    
    context = {
        'contact_info': CONTACT_INFO,
    }
    return render(request, 'website/contact.html', context)
