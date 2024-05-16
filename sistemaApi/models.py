#from django.db import models

#class Produto(models.Model):
 #   nome = models.CharField(max_length=100)
   # preco = models.DecimalField(max_digits=10, decimal_places=2)
    #quantidade = models.IntegerField()

#class Estoque(models.Model):
    #produto = models.CharField(max_length=100)
    #quantidade = models.IntegerField()
    
#class Pedido(models.Model):
    #produto = models.ManyToManyField(Produto, through='ItemPedido')
    #cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
   # status = models.CharField(max_length=50)

#class Cliente(models.Model):
    #nome = models.CharField(max_length=100)
   #email = models.EmailField()
    
#class ItemPedido(models.Model):
    #produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    #pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    #quantidade = models.IntegerField()
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, default='xxx')
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
        
class Pedido(models.Model):
    produto = models.ManyToManyField(Produto, through='ItemPedido')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.status
        
class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    


