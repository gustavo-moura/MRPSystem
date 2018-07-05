

# Classe que organiza os itens que serão utilizados no MRP
class Item():
	codigo = None
	nome = None
	tr = None
	lote = None
	emin = None
	eatual = None

	dependencias = []

	def __init__(self, codigo, nome, tr, lote, emin, eatual):
		self.codigo = codigo	# Código do item 
		self.nome = nome		# Nome descritivo
		# self.nivel = nivel		# Nível na árvore de produto
		self.tr = tr 			# Tempo de Ressuprimento
		self.lote = lote		# Lote mínimo
		self.emin = emin		# estoque mínimo para o produto
		self.eatual = eatual	# estoque atual inicial


	def addDependencia(self, item):
		self.dependencias.append(item)



# Classe que armazena uma coleção de itens
class Biblioteca():
	itens = []

	def __init__(self):
		self.itens = []

	# retorna true se o item foi inserido corretamente, false cc
	def addItem(self, item):
		self.itens.append(item)

		if(self.itens.index(item)):
			return True
		else: return False

	# Retorna o item da biblioteca referente ao Índice passado como entrada
	def getItem_index(self, index):
		return self.itens[index]

	# Retorna o item da biblioteca referente ao item passado como entrada
	def getItem_item(self, item):
		return self.itens[self.itens.index(item)]

	# Retorna o array de itens da biblioteca
	def getItems(self):
		retorno = []

		for x in range(len(self.itens)):
			retorno.append(self.itens[x].codigo + " - " + self.itens[x].nome)

		return retorno

	def estaVazia(self):
		if(self.itens == []):
			return True
		else: return False

	def lenght(self):
		return len(self.itens)


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