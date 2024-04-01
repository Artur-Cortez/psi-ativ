from django.contrib import admin

from .models import * 

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    search_fields = ('produto',)
    exclude = ('msgPromocao',)

admin.site.register(Fabricante, FabricanteAdmin) 
admin.site.register(Categoria) 
admin.site.register(Produto, ProdutoAdmin) 
