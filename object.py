# Classe que organiza os itens que serão utilizados no MRP
class Item():
	def __init__(self, codigo, nome, nivel, tr, lote, emin, eatual):
		self.codigo = codigo	# Código do item 
		self.nome = nome		# Nome descritivo
		self.nivel = nivel		# Nível na árvore de produto
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
	NP: Necessidades Prevista	[0..12]
	RP: Recebimento Programado	[1..12]
	ED: Estoque Disponível		[1..12]
	NL: Necessidade Líquida		[1..12]
	LP: Liberação de Pedido		[1..12]
	'''

	# Receber NP de cada item pra cada semana

	# Definir o estoque mínimo
	ED[0] = self.item.eatual

	for i in range(1, 12):

		if(NP[i]>0):
			NL[i] = NP[i] - ED[i-1]

			if(NL[i]>0):
				teste = i-self.item.tr

				if(teste<0):
					# Erro: O pedido de compra do <item> deve ser realizado |<teste>| dias antes do início da execução do plano

				else:
					LP[i-self.item.tr] = NL[i]

		ED[i] = ED[i-1] + RP[i] - NP[i]




