from django.urls import path

from products.views import products, basket_add, basket_remove
from . import views
app_name = 'products'

urlpatterns = [
    path('', products, name = 'index'),
    path('category/<int:category_id>/', products, name = 'category'),
    path('page/<int:page_number>/', products, name = 'paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name = 'basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name = 'basket_remove'),
    path('<int:pk>/', views.productcardview.as_view(), name = 'productcard')
]
 