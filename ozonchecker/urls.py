from django.contrib import admin
from django.urls import path
from links.views import LinkDeleteView, home_view, update_price_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name="home"),
    path('update/<pk>', update_price_view, name="update"),
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),
]
