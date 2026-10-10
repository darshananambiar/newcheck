from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Enhanced sample tea data
TEA_DATA = [
    {
        'id': 1,
        'name': 'Midnight Assam',
        'category': 'Signature',
        'price': 24,
        'description': 'Deep and smoky Assam leaves blended with a hint of cacao nibs.',
        'emoji_icon': '🌙'
    },
    {
        'id': 2,
        'name': 'Moonlit Oolong',
        'category': 'Exotic',
        'price': 32,
        'description': 'Floral, crisp, and lightly roasted for a luminous sip.',
        'emoji_icon': '✨'
    },
    {
        'id': 3,
        'name': 'Noir Spice',
        'category': 'Classic',
        'price': 28,
        'description': 'Warming blend of dark spices and premium black tea.',
        'emoji_icon': '🔥'
    },
    {
        'id': 4,
        'name': 'Black Jasmine',
        'category': 'Signature',
        'price': 30,
        'description': 'Silky black tea infused with delicate jasmine flowers.',
        'emoji_icon': '🌸'
    },
    {
        'id': 5,
        'name': 'Velvet Earl Grey',
        'category': 'Classic',
        'price': 22,
        'description': 'Classic Earl Grey with premium bergamot oil.',
        'emoji_icon': '👑'
    },
    {
        'id': 6,
        'name': 'Dark Pu-erh',
        'category': 'Exotic',
        'price': 38,
        'description': 'Aged Pu-erh tea with earthy notes and smooth finish.',
        'emoji_icon': '🍂'
    },
    {
        'id': 7,
        'name': 'Golden Matcha',
        'category': 'Signature',
        'price': 36,
        'description': 'Premium ceremonial grade matcha from Uji, Japan.',
        'emoji_icon': '🍵'
    },
    {
        'id': 8,
        'name': 'Royal Rooibos',
        'category': 'Classic',
        'price': 20,
        'description': 'Organic South African rooibos with natural sweetness.',
        'emoji_icon': '🌰'
    }
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tea_collections(request):
    return render(request, 'tea-collections.html')

def experience(request):
    return render(request, 'experience.html')

def franchise(request):
    return render(request, 'franchise.html')

def contact(request):
    return render(request, 'contact.html')

@require_http_methods(["GET"])
def get_teas(request):
    category = request.GET.get('category', '')
    
    if category:
        teas = [t for t in TEA_DATA if t['category'] == category]
    else:
        teas = TEA_DATA
    
    return JsonResponse({
        'status': 'success',
        'data': teas
    })
    
def franchise_enquiry(request):
    pass
