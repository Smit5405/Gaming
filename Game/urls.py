from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('contact/',contact,name='contact'),
    path('logout/',logout,name='logout'),
    path('about/',about,name='about'),
    path('shop/',shop,name='shop'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:game_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('checkout/', checkout, name='checkout'),

]
