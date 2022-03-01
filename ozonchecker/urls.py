from django.contrib import admin
from django.urls import path
from links.views import home_view, update_prices, LinkDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('update/', update_prices, name="update-prices"),
    path('delete/<pk>/', LinkDeleteView.as_view(), name="delete"),
]
