from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

from django.shortcuts import render 
from loja.models import Produto

def list_produto_view(request, id=None):

    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    

    produtos = Produto.objects.all()
    print(produtos)

    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if produto is not None:
        print(produto)
        produtos = produtos.filter(Produto=produto)
        print(produtos)
    if promocao is not None:
        print(promocao)
        produtos = produtos.filter(promocao=promocao)
        print(produtos)
    if destaque is not None:
        print(destaque)
        produtos = produtos.filter(destaque=destaque)
        print(produtos)
    if categoria is not None:
        print(categoria)
        produtos = produtos.filter(categoria__categoria=categoria)
        print(produtos)
    if fabricante is not None:
        print(fabricante)
        produtos = produtos.filter(fabricante__fabricante=fabricante)
        print(produtos)

    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)

    if id is not None:
        print(id)
        produtos = produtos.filter(id=id)

      
    context = {
        'produtos': produtos
    }

    return render(request, template_name='produto/produto.html', context=context, status=200)
    
   