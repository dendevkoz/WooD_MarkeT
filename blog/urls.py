from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/<int:key_id>/', views.index, name='index'),
    path('<int:articles_id>/', views.detail, name='detail'),
    path('contact/', views.get_name, name='get_name'),
    path('thanks/', views.thank_you, name='thank_you'),
]

