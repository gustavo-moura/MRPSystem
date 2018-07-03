


# Classe que organiza os itens que serão utilizados no MRP
class Item():
	def __init__(self, codigo, nome, tr, lote, emin, eatual):
		self.codigo = codigo	# Código do item 
		self.nome = nome		# Nome descritivo
		# self.nivel = nivel		# Nível na árvore de produto
		self.tr = tr 			# Tempo de Ressuprimento
		self.lote = lote		# Lote mínimo
		self.emin = emin		# estoque mínimo para o produto
		self.eatual = eatual	# estoque atual inicial


# O MRP em si. Um para cada item
class Item_MRP():
	# Trabalhando com MRP de 12 semanas

	def __init__(self, item):
		self.item = item



	'''
	NB: Necessidades Brutas
	RP: Recebimento Programado
	ED: Estoque Disponível
	NL: Necessidade Líquida
	LP: Liberação de Pedido
	'''