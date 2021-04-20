from django.urls import path
from . import views
urlpatterns =[
    path('', views.index),
    path('cart',views.cart),
    path('products/show/<int:id>', views.buypage),
    path('dashboard',views.dashboard),
    path('dashboard/products/<int:id>/edit', views.product_edit),
    path('dashboard/products', views.products),
    path('dashboard/orders/show', views.showproduct),
    path('dashboard/products/add', views.new_product),

    # path('upload_image', views.upload_img),
]