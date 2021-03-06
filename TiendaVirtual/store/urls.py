from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name="index"),
    #path('product/', views.producto, name="product"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('product/<product_id>/', views.producto, name="product"),
]