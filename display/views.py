from django.template import loader

# Create your views here.
from django.http import HttpResponse

from display.models import Coins

CACHE_ID: int = 7919


def home(request):
    display = 'INSERT COINS'

    # retrieve what's in the cache
    try:
        cache = Coins.objects.get(pk=CACHE_ID)
    except Coins.DoesNotExist:
        cache = None
    if cache is None:
        cache = Coins(id=CACHE_ID, quarters=0)
        cache.save()
    quarters = cache.quarters

    money: float = 0.25 * quarters
    if money >= 1.0:
        display = 'SELECT PRODUCT'

    template = loader.get_template('index.html')
    context = {
        'quarters': quarters,
        'show_money': f'${money:.2f}',
        'display': display
    }
    return HttpResponse(template.render(context, request))


def insert_coin(request):
    # Add a quarter to the cache
    cache = Coins.objects.get(pk=CACHE_ID)
    quarters = cache.quarters
    if quarters is None:
        quarters = 1
    else:
        quarters = quarters + 1
    cache.quarters = quarters
    cache.save()

    return home(request)


def coin_return(request):
    cache = Coins.objects.get(pk=CACHE_ID)
    quarters = cache.quarters
    cache.quarters = 0
    cache.save()
    template = loader.get_template('return.html')
    context = {
        'quarters': quarters
    }
    return HttpResponse(template.render(context, request))


def dispense_product(request):
    money: float = 1.0
    display = 'THANK YOU'
    cache = Coins.objects.get(pk=CACHE_ID)
    quarters = cache.quarters
    if quarters >= 4:
        quarters = quarters - 4
    else:
        display = 'Error!!!'
    cache.quarters = 0
    cache.save()
    template = loader.get_template('dispense.html')
    context = {
        'quarters': quarters,
        'show_money': f'${money:.2f}',
        'display': display
    }
    return HttpResponse(template.render(context, request))
