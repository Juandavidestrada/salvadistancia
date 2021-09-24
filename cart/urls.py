from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = []
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list')
]