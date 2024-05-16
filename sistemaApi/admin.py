from django.contrib import admin
from .models import Cliente, Produto

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

admin.site.register(Produto, Produtos)