from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_category, name='product_category'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('cat/<int:category_id>/', views.product_category, name='product_category'),
    # path('gp/<int:image_id>/', views.gallery_product, name='gallery_product'),

]
