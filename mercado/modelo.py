import os
from peewee import *

arq = "compras.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
	class Meta():
		database = db

class Produto():
	def __init__(self, codigo, preco):
		self.codigo = codigo 
		self.preco = preco

class Item():
	def __init__(self, produto, quantidade):
		self.produto = produto
		self.quantidade = quantidade

class Carrinho():
	def __init__(self):
		self.itens = []
		self.preco_total = 0

	def adicionar_item(self, item):
		self.itens.append(item)

	def calcular_preco(self):
		for i in self.itens:
			self.preco_total += i.quantidade * i.produto.preco
		return self.preco_total

cafe = Produto(123, 3)
maca = Produto(222, 5)
item = Item(cafe, 2)
item_maca = Item(maca, 9)
carrinho = Carrinho()
carrinho.adicionar_item(item)
carrinho.adicionar_item(item_maca)
print(carrinho.calcular_preco())