from multiprocessing import Pool
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .forms import AddLinkForm
from .models import Link
from .utils import get_info

def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            form_name, form_current_price = get_info(form['url'].value())
            form = form.save(commit=False)
            form.url = "/".join(form.url.split('/')[:5])[1:]
            form.name, form.current_price = form_name, form_current_price
            form.save()
        except AttributeError:
            error = "Ой! Не удалось получить название или цену товара.."
        except: 
            error = "Ой! Ссылка которую вы ввели недействительна.."
    
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
    links = []

    for i in qs:
        links.append(i.url)
    p = Pool(processes=len(links))
    result = p.map(get_info, links)
    p.close()
    num = 0
    for i in qs:
        if result[num][1] != i.current_price:
            i.old_price = i.current_price
            i.current_price = result[num][1]
            diff = result[num][1] - i.old_price
            i.price_difference = round(diff, 2)
            i.save()
        num += 1
    return redirect('home')