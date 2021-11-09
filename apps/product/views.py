from django.http import HttpResponse
from django.template import loader


# Create your views here.
def all_products(request):
    template = loader.get_template('products/all_products.html')
    context = {}
    return HttpResponse(template.render(context, request))
