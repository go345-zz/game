class Gut:
	def __init__(self, spiel):
		self.preis = 0
		self.spiel = spiel
	
	def kaufen(self):
		if self.spiel.geld >= self.preis:
			self.spiel.geld -= self.preis

	def ernten(self):
		pass


class feld(Gut):
	def __init__(self, spiel):
		self.preis.erde = 5
		self.preis.samen = 10
		self.preis.arbeiter = 1
		self.preis.wasser = 5
		self.spiel = spiel
		

	def kaufen(self):
		if self.spiel.erde >= self.preis.erde and self.spiel.samen >= self.preis.samen and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.wasser >= self.preis.wasser:
			self.spiel.erde -= self.preis.erde
			self.spiel.samen -= self.preis.samen
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.wasser -= self.preis.wasser
			self.spiel.gekauft.append(self)

	def ernten(self):
		self.spiel.samen += 5
		self.spiel.korn += 10
		self.spiel.stroh += 3


class forst(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 5
		