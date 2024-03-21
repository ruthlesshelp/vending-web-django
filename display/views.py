from django.template import loader

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from display.models import Cache

CACHE_ID: int = 7919


def home(request):
    display = 'INSERT COINS'

    # retrieve what's in the cache
    try:
        cache = Cache.objects.get(pk=CACHE_ID)
    except Cache.DoesNotExist:
        cache = None
    if cache is None:
        cache = Cache(id=CACHE_ID, quarters=0)
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
    if request.method != "POST":
        return HttpResponseRedirect('.')

    # Add a quarter to the cache
    cache = Cache.objects.get(pk=CACHE_ID)
    quarters = cache.quarters
    if quarters is None:
        quarters = 0

    display = 'INSERT COINS'
    money: float = 0.25 * quarters
    if money >= 1.0:
        display = 'SELECT PRODUCT'

    template = loader.get_template('index.html')
    context = {
        'quarters': quarters,
        'show_money': f'${money:.2f}',
        'display': display,
    }

    # Retrieve value from the POST
    try:
        inserted_quarters = int(request.POST.get('inserted_quarters'))

        if inserted_quarters > 0:
            quarters = quarters + inserted_quarters
        else:
            raise ValueError()

        cache.quarters = quarters
        cache.save()

        print("Inserted quarters: {}".format(inserted_quarters))
    except Exception as exc_info:
        context['error_message'] = 'Please enter the number of quarters, greater than zero.'

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('.')


def coin_return(request):
    cache = Cache.objects.get(pk=CACHE_ID)
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
    cache = Cache.objects.get(pk=CACHE_ID)
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
