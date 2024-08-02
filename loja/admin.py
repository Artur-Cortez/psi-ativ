from django.contrib import admin
from django.utils.html import format_html
from .models import * 

class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    search_fields = ('fabricante', )


class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    search_fields = ("categoria",)


class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
    list_display = ['name','image_tag',]

class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    date_hierarchy = 'criado_em'
    search_fields = ('produto',)

    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('produto', 'img_preview', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = "Vazio"
    search_fields = ('produto', )

admin.site.register(Fabricante, FabricanteAdmin) 
admin.site.register(Categoria, CategoriaAdmin) 
admin.site.register(Produto, ProdutoAdmin)

