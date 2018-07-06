import numpy as np

# Ordem de Produção
class OrdemProducao():

	def __init__(self, sem, qtd):
		self.sem = sem
		self.qtd = qtd

# O MRP em si. Um para cada item
class Item_MRP():
	# Trabalhando com MRP de 12 sems + uma posição 0 inicial

	def __init__(self, item, ordens):
		self.item = item
		self.NB = np.zeros(13)	# excluir o primeiro para exibição
		self.RP = np.zeros(13)
		self.ED = np.zeros(13)
		self.ED[0] = item.eatual
		self.LP = np.zeros(13)

		# insere ordens
		for ordem in ordens:

			# verifica se será possível produzir a tempo
			if(ordem.sem-item.tr>=1):
				self.NB[ordem.sem] = ordem.qtd
				if(ordem.qtd>=item.lote):
					self.LP[ordem.sem-item.tr] = ordem.qtd
					self.RP[ordem.sem] = ordem.qtd
				else:
					self.LP[ordem.sem-item.tr] = item.lote
					self.RP[ordem.sem] = item.lote
			else:
				print("ordem infactível")

		# preenchimento do estoque disponível para cada sem
		for i in range(1,13):
			self.ED[i] = self.ED[i-1]+self.RP[i]-self.NB[i] 


# Exemplo
item = Item("cod do item", "nome do item", 3, 100, 20, 30)
ordem = [OrdemProducao(6, 40)]
mrp = Item_MRP(item, ordem)
