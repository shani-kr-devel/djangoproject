from django.shortcuts import render

# Create your views here.
def sale_view(request):
    return render(request, 'sale/sale.html')
