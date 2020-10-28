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
		self.preis.wasser = 5
		self.preis.holz = 0
		self.preis.eisen = 0
		self.preis.samen = 10
		self.preis.gold = 0
		self.preis.arbeiter = 1
		self.preis.stein = 0
		self.preis.erde = 5
		self.preis.lehm =0
		self.preis.wolle = 0
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 0
		self.preis.kohle = 0
		self.preis.stroh = 0
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.preis.stein and self.spiel.erde >= self.preis.erde and self.spiel.lehm >= self.preis.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.spip	el.sand and self.spiel.kohle >= self.preis.kohle:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle

			self.spiel.gekauft.append(feld)
			self.spiel.siegpunkte += 1
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0

class forst(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 5
		self.preis.holz = 3
		self.preis.eisen = 2
		self.preis.samen = 5
		self.preis.gold = 0
		self.preis.arbeiter = 3
		self.preis.stein = 0
		self.preis.erde = 5
		self.preis.lehm =0
		self.preis.wolle = 0
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 0
		self.preis.kohle = 0
		self.preis.stroh = 2
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.spiel.stein and self.spiel.erde >= self.spiel.erde and self.spiel.lehm >= self.spiel.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.preis.sand and self.spiel.kohle >= self.preis.kohle and self.spiel.stroh >= self.preis.stroh:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle
			self.spiel.stroh -= self.preis.stroh

			self.spiel.gekauft.append(forst)
			self.spiel.siegpunkte +=1.5
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0

class grube(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 0
		self.preis.holz = 40
		self.preis.eisen = 2
		self.preis.samen = 0
		self.preis.gold = 0
		self.preis.arbeiter = 2
		self.preis.stein = 0
		self.preis.erde = 5
		self.preis.lehm =0
		self.preis.wolle = 0
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 5
		self.preis.kohle = 0
		self.preis.stroh = 0
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.spiel.stein and self.spiel.erde >= self.spiel.erde and self.spiel.lehm >= self.spiel.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.preis.sand and self.spiel.kohle >= self.preis.kohle and self.spiel.stroh >= self.preis.stroh:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle
			self.spiel.stroh -= self.preis.stroh

			self.spiel.gekauft.append(grube)
			self.spiel.siegpunkte += 1.5
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0

class fluss(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 10
		self.preis.holz = 0
		self.preis.eisen = 0
		self.preis.samen = 5
		self.preis.gold = 0
		self.preis.arbeiter = 0
		self.preis.stein = 0
		self.preis.erde = 10
		self.preis.lehm =5
		self.preis.wolle = 0
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 5
		self.preis.kohle = 0
		self.preis.stroh = 0
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.spiel.stein and self.spiel.erde >= self.spiel.erde and self.spiel.lehm >= self.spiel.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.preis.sand and self.spiel.kohle >= self.preis.kohle and self.spiel.stroh >= self.preis.stroh:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle
			self.spiel.stroh -= self.preis.stroh

			self.spiel.gekauft.append(fluss)
			self.spiel.siegpunkte += 2
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0

class weide(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 5
		self.preis.holz = 65
		self.preis.eisen = 0
		self.preis.samen = 30
		self.preis.gold = 0
		self.preis.arbeiter = 1
		self.preis.stein = 0
		self.preis.erde = 15
		self.preis.lehm =0
		self.preis.wolle = 0
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 0
		self.preis.kohle = 0
		self.preis.stroh = 0
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.spiel.stein and self.spiel.erde >= self.spiel.erde and self.spiel.lehm >= self.spiel.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.preis.sand and self.spiel.kohle >= self.preis.kohle and self.spiel.stroh >= self.preis.stroh:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle
			self.spiel.stroh -= self.preis.stroh

			self.spiel.gekauft.append(weide)
			self.spiel.siegpunkte += 2.5
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0

class mühle(Gut):
	def __init__(self, spiel):
		self.preis.wasser = 35
		self.preis.holz = 80
		self.preis.eisen = 0
		self.preis.samen = 0
		self.preis.gold = 0
		self.preis.arbeiter = 3
		self.preis.stein = 15
		self.preis.erde = 0
		self.preis.lehm = 35
		self.preis.wolle = 50
		self.preis.korn = 0
		self.preis.mehl = 0
		self.preis.sand = 20
		self.preis.kohle = 0
		self.preis.stroh = 0
		self.spiel = spiel
	def kaufen(self):
		if self.spiel.wasser >= self.preis.wasser and self.spiel.holz >= self.preis.holz and self.spiel.eisen >= self.preis.eisen and self.spiel.samen >= self.preis.samen and self.spiel.gold >= self.preis.gold and self.spiel.arbeiter >= self.preis.arbeiter and self.spiel.stein >= self.spiel.stein and self.spiel.erde >= self.spiel.erde and self.spiel.lehm >= self.spiel.lehm and self.spiel.wolle >= self.preis.wolle and self.spiel.korn >= self.preis.korn and self.spiel.mehl >= self.preis.mehl and self.spiel.sand >= self.preis.sand and self.spiel.kohle >= self.preis.kohle and self.spiel.stroh >= self.preis.stroh:
			self.spiel.wasser -= self.preis.wasser
			self.spiel.holz -= self.preis.holz
			self.spiel.eisen -= self.preis.eisen
			self.spiel.samen -= self.preis.samen
			self.spiel.gold -= self.preis.gold
			self.spiel.arbeiter -= self.preis.arbeiter
			self.spiel.stein -= self.preis.stein
			self.spiel.erde -= self.preis.erde
			self.spiel.lehm -= self.preis.lehm
			self.spiel.wolle -= self.preis.wolle
			self.spiel.korn -= self.preis.korn
			self.spiel.mehl -= self.preis.mehl
			self.spiel.sand -= self.preis.sand
			self.spiel.kohle -= self.preis.kohle
			self.spiel.stroh -= self.preis.stroh

			self.spiel.gekauft.append(mühle)
			self.spiel.siegpunkte += 3
	def ernten(self):
		self.spiel.wasser += 0
		self.spiel.holz += 0
		self.spiel.eisen += 0
		self.spiel.samen += 0
		self.spiel.gold += 0
		self.spiel.arbeiter += 0
		self.spiel.stein += 0
		self.spiel.erde += 0
		self.spiel.lehm += 0
		self.spiel.wolle += 0
		self.spiel.korn += 0
		self.spiel.mehl += 0
		self.spiel.sand += 0
		self.spiel.kohle += 0
