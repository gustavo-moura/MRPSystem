import math

# Classe que organiza os itens que serão utilizados no MRP
class Item():
	'''
	codigo = None
	nome = None
	tr = None
	lote = None
	emin = None
	eatual = None
	dependencias = []
	'''

	def __init__(self, codigo, nome, tr, lote, emin, eatual):
		self.codigo = codigo	# Código do item 
		self.nome = nome		# Nome descritivo
		# self.nivel = nivel		# Nível na árvore de produto
		self.tr = tr 			# Tempo de Ressuprimento
		self.lote = lote		# Lote mínimo
		self.emin = emin		# estoque mínimo para o produto
		self.eatual = eatual	# estoque atual inicial

		self.dependencias = []


	def addDependencia(self, item, qtd):
		dp = Dependencia(item, qtd)
		self.dependencias.append(dp)

	def getDependencias(self):
		for dp in self.dependencias:
			print (str(dp))

class Dependencia:

	def __init__(self, item, qtd):
		self.item = item 
		self.q = qtd

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

	def naoTem(self, codigo):
		for i in range(self.itens):
			if(self.itens[i].codigo == codigo):
				return False
		return True

# O MRP em si. Um para cada item
class Item_MRP():

	def __init__(self, item):
		self.item = item
		n = 1+12
		self.n = n       # Trabalhando com MRP de 1+12 semanas
		self.nb = [0]*n  # Necessidades Brutas
		self.rp = [0]*n  # Recebimento Programado
		self.ed = [0]*n  # Estoque Disponível
		self.lp = [0]*n  # Liberação de Pedido
		self.ed[0] = item.eatual
	
	def add_nb(self, semana, qtd):
		self.nb[semana] += qtd
		self.atualizar(semana)

	def set_nb(self, semana, qtd):
		self.nb[semana] = qtd
		self.atualizar(semana)

	def atualizar(self, inicio):
		lote = self.item.lote
		for i in range(inicio, self.n):
			nb = self.nb[i]
			ed = self.ed[i-1]
			qtd = math.ceil((nb - ed) / lote) * lote
			if ed >= nb or self.pedido(i, qtd):
				self.ed[i] = ed + self.rp[i] - nb
			else:
				self.ed[i] = ed + self.rp[i]
	
	def pedido(self, semana, qtd):
		'''
		Libera pedidos para atender a quantidade solicitada na semana atual,
		primeiro verificando os estoques de dependencias e atualizando seus MRPs
		'''
		lead = self.item.tr
		if semana - lead < 1:
			return False
		for dp in self.item.dependencias:
			dp_mrp = Item_MRP.find(dp.item)
			if dp_mrp.ed[semana] < qtd * dp.q:
				return False
		for dp in self.item.dependencias:
			Item_MRP.find(dp.item).add_nb(qtd * dp.q)
		self.lp[semana-lead] += qtd
		self.rp[semana] += qtd
		return True

	_db = {} # "base de dados"

	def find(item):
		try:
			return Item_MRP._db[item]
		except(KeyError):
			mrp = Item_MRP(item)
			Item_MRP._db[item] = mrp
			return mrp

