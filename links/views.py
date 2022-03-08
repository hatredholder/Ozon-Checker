from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import AddLinkForm
from .models import Link
from django.views.generic import DeleteView


def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Oops! Couldn't get the name or the price.."
        except: 
            error = "Oops! Something went wrong.."
    
    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    discount_list = []
    if items_no > 0:
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs':qs,
        'items_no':items_no,
        'no_discounted':no_discounted,
        'discount_list': discount_list,
        'form':form,
        'error':error
    }

    return render(request, 'links/main.html', context)

class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')