from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .forms import AddLinkForm
from .models import Link
from .utils import get_info


def home_view(request):
    """Home view"""
    discounted_items_count = 0
    error = None

    form = AddLinkForm(request.POST or None)

    # Add a URL
    if request.method == 'POST':
        try:
            form_name, form_current_price = get_info(product_name=form['url'].value().split('/')[4])
            form = form.save(commit=False)

            # Get a clean url
            form.url = "/".join(form.url.split('/')[:5])

            form.name, form.current_price = form_name, form_current_price
            form.save()
        except AttributeError as e:
            error = "Ой! Не удалось получить название или цену товара.."
        except Exception as e: 
            error = "Ой! Произошла неизвестная ошибка, стоит попробовать ещё раз."
    
    form = AddLinkForm()

    qs = Link.objects.all()
    items_count = qs.count()

    # Add item to discount list
    discount_list = []
    if items_count > 0:
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            discounted_items_count = len(discount_list)

    context = {
        'qs':qs,
        'items_count':items_count,
        'discounted_items_count':discounted_items_count,
        'discount_list': discount_list,
        'form':form,
        'error':error
    }

    return render(request, 'links/main.html', context)

class LinkDeleteView(DeleteView):
    """URL Deletion view"""
    model = Link
    success_url = reverse_lazy('home')

def update_price(request, pk):
    """Update a price view"""
    link_object = Link.objects.get(pk=pk)
    updated_info = get_info(product_name=link_object.url.split('/')[4])

    # Updating the prices in the database
    if updated_info[1] != link_object.current_price:
        link_object.old_price = link_object.current_price
        link_object.current_price = updated_info[1]
        diff = updated_info[1] - link_object.old_price
        link_object.price_difference = round(diff, 2)
        link_object.save()
    return redirect('home')
