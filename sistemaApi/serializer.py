#from rest_framework import serializers
#from .models import Produto, Estoque, Pedido, Cliente, ItemPedido

#class ProdutoSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Produto
        #fields = '__all__'
        
#class EstoqueSerializer(serializers.ModelSerializer):
    #class Meta:
       # model = Estoque
        #fields = '__all__'
        
#class PedidoSerializer(serializers.ModelSerializer):
    #class Meta:
       # model = Pedido
       # fields = '__all__'
        
#class ClienteSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Cliente
        #fields = '__all__'
        
#class ItemPedidoSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = ItemPedido
       # fields = '__all__'
       
       
    
from rest_framework import serializers
from .models import Cliente, Produto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        
