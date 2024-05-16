from django.http import JsonResponse
from rest_framework import viewsets
from .models import Cliente, Produto, Pedido
from .serializer import ClienteSerializer, ProdutoSerializer, PedidoSerializer


def clientes(request):
    if request.method == 'GET':
        cliente = {'id':1, 'nome':'Robério'}
        return JsonResponse(cliente)


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer