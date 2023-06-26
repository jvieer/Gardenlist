from django.urls import path, include
from .views import *
from rest_framework import routers

#RUTAS DEL API
router = routers.DefaultRouter()
router.register('productos',ProductoViewset)


urlpatterns = [
    #API
    path('api/', include(router.urls)),


    path('blog/', blog, name="blog"),
  
    path('category/', category, name="category"),
    path('checkout/', checkout, name="checkout"),
    path('confirmation/', confirmation, name="confirmation"),
    path('contact/', contact, name="contact"),
    path('indexApi/', indexApi, name="indexApi"),
    path('', index, name="index"),
    path('singleblog/', singleblog, name="singleblog"),
    path('singleproduct/<id>', singleproduct, name="singleproduct"),
    path('trackingorder/', trackingorder, name="trackingorder"),
  
    path('perfil/', perfil, name="perfil"),
    path('wishlist/', wishlist, name= "wishlist"),
    path('add/', add, name="add"),
    path('update/<id>/', update, name="update"),
    path('delete/<id>/', delete, name="delete"),
    path('cart/', cart, name="cart"),
    path('cartadd/<id>/', cartadd, name="cartadd"),
    path('cart/cartdel/<id>/', cartdel, name="cartdel"),
    path('cart/cartadd/<id>',cartadd, name="cartaddd"),
    path('cart/cartdelete/<id>',cartdelete, name="cartdelete"),
    path('add_compra/', add_compra, name="add_compra"),
    path('miscompras/', miscompras, name = "miscompras"),
    path('detalle/<id>', detalle, name="detalle")
]
