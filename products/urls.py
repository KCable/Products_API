from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('<pk>/', views.product_detail),
    path('<str:make>', views.products_by_title)
]