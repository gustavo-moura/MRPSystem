


# Classe que organiza os itens que serão utilizados no MRP
class Item():
	def __init__(self, codigo, nome, nivel, tr, lote):
		self.codigo = codigo	# Código do item 
		self.nome = nome		# Nome descritivo
		self.nivel = nivel		# Nível na árvore de produto
		self.tr = tr 			# Tempo de Ressuprimento
		self.lote = lote		# Lote mínimo
		self.estoque = estoque


# O MRP em si. Um para cada item
class Item_MRP():
	# Trabalhando com MRP de 12 semanas

	def __init__(self, item):
		self.item = item
