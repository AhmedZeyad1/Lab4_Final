from django.shortcuts import render

def default_view(request):
    return render(request, 'tax/default.html')


def calculate_total(request, number):
    price = float(number)
    tax_rate = 0.15
    total = price + (price * tax_rate)
    context = {'total': total}
    return render(request, 'tax/total.html', context)


def display_tax_rate(request):
    tax_rate = 0.15
    context = {'tax_rate': tax_rate}
    return render(request, 'tax/tax_rate.html', context)