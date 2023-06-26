from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','precio','stock','tipo','imagen','created_at','updated_at']
    search_fields = ['nombre']
    list_per_page = 5
    list_filter = ['tipo']
    list_editable = ['precio','stock','tipo','imagen']

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ['id','descripcion','created_at','updated_at']
    search_fields = ['descripcion']
    list_per_page = 5
    list_filter = ['descripcion']

class CompraAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','fecha','created_at','updated_at']
    search_fields = ['usuario']
    list_per_page = 5
    list_filter = ['usuario']

class CarroItemAdmin(admin.ModelAdmin):
    list_display = ['id','producto','cantidad','usuario','created_at','updated_at']
    search_fields = ['producto']
    list_per_page = 5
    list_filter = ['producto']

class CompraItemAdmin(admin.ModelAdmin):
    list_display = ['id','compra','carro_item','created_at','updated_at']
    search_fields = ['compra']
    list_per_page = 5
    list_filter = ['compra']

class CarroComprasAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','created_at','updated_at']
    search_fields = ['usuario']
    list_per_page = 5
    list_filter = ['usuario']


admin.site.register(TipoProducto,TipoProductoAdmin)

admin.site.register(Producto,ProductoAdmin)

admin.site.register(CarroItem, CarroItemAdmin)

admin.site.register(Compra, CompraAdmin)

admin.site.register(CompraItem, CompraItemAdmin)

admin.site.register(CarroCompras, CarroComprasAdmin)