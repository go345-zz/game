from termcolor import colored

print("\n")
print("\n")
print("\n")

siegpunkte = 0

gold = 25
stein = 25
eisen = 20
holz = 5
erde = 15
lehm = 5
stroh = 5
samen = 15
wolle = 0
korn = 0
mehl = 0
sand = 10
kohle = 0
wasser = 35
arbeiter = 20


felder = 0
forste = 0
gruben = 0
flüsse = 0
weiden = 0
mühlen = 0
minen = 0
wohnhäuser = 0
märkte = 0

runde = 0


while True:
	runde += 1

	print(colored(f"\n\nSiegpunkte: {siegpunkte}\nRunde: {runde}\n\n", 'yellow'))

	print("Gold:",gold)
	print("Stein:",stein)
	print("Eisen:",eisen)
	print("Holz:",holz)
	print("Erde:",erde)
	print("Lehm:",lehm)
	print("Stroh:",stroh)
	print("Samen:",samen)
	print("Wolle:",wolle)
	print("Getreide:",korn)
	print("Mehl:",mehl)
	print("Sand:",sand)
	print("Kohle:", kohle)
	print("Wasser:",wasser)
	print("Arbeiter:",arbeiter)

	print("\nFelder:",felder)
	print(f"Forste: {forste}")
	print(f"Gruben: {gruben}")
	print(f"Flüsse: {flüsse}")
	print(f"Weiden: {weiden}")
	print(f"Mühlen: {mühlen}")
	print(f"Minen: {minen}")
	print(f"Wohnhäuser: {wohnhäuser}")
	print(f"Märkte: {märkte}")

	print("\n1)Feld")
	print("2)Forst")
	print("3)Grube")
	print("4)Fluss")
	print("5)Weide")
	print("6)Mühle")
	print("7)Mine")
	print("8)Wohnhaus")
	print("9)Markt")



	if felder > 0:
		for i in range(felder):
			samen+=5
			korn+=10
			stroh+=3

	if forste > 0:
		for i in range(forste):
			holz += 7
			stein += 1
			stroh += 1
			samen += 2

	if gruben > 0:
		for i in range(gruben):
			erde += 3
			sand += 2
			stein += 1
			kohle += 1
			lehm += 4
		
	if flüsse > 0:
		for i in range(flüsse):
			wasser += 5
			samen += 1
			holz += 1
			sand += 1
			lehm += 1
		
	if weiden > 0:
		for i in range(weiden):
			wolle += 10

	if mühlen > 0:
		for i in range(mühlen):
			if korn >= 8:
				korn -= 8
				mehl += 6

	if minen > 0:
		for i in range(minen):
			gold += 3
			eisen += 10
			stein += 20
			sand += 5

	if märkte > 0:
		if mehl >= 20 and korn >= 5 and wasser >= 5:#=Brot
			mehl -= 20
			korn -= 5
			wasser -= 5
			siegpunkte += 0.2
		if stroh <= 10 and korn >= 5:#=Tierfutter
			stroh -= 10
			korn -= 5
			siegpunkte += 0.3
		if gold >= 10:#=Gold
			gold -= 10
			siegpunkte += 2
		if eisen >= 10:#=Eisen
			eisen -= 10
			siegpunkte += 0.5
		if wolle >= 15 and stein >= 5 and samen >= 5 and gold >= 3:#=Goldseide
			wolle -= 15
			stein -= 5
			samen -= 5
			gold -= 3
			siegpunkte += 1.5

	a=input("\nWas möchtest du bauen? ")


	if a == "1":#Feld
		if erde >= 5 and samen >= 10 and arbeiter >= 1 and wasser >=5:
			wasser -= 5
			erde -= 5
			samen-=10
			arbeiter-=1
			felder += 1
			siegpunkte += 1
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n5 Wasser, 5 Erde, 10 Samen, 1 Arbeiter")
	elif a == "2":#Forst
		if holz >= 3 and eisen >= 2 and samen >= 5 and stroh >= 2 and erde >= 5 and arbeiter >=3 and wasser >= 5:
			wasser -= 5
			holz -= 3
			eisen -= 2
			samen -= 5
			stroh -= 2
			erde -= 5
			arbeiter -= 3		
			forste += 1
			siegpunkte += 1.5
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n5 Wasser, 3 Holz, 2 Eisen, 5 Samen, 2 Stroh, 5 Erde, 3 Arbeiter")
	elif a == "3":#Grube
		if erde >=5 and sand >= 5 and eisen >= 2 and holz >= 40 and arbeiter >=2:
			erde -= 5
			sand -= 5
			eisen -= 2
			holz -= 40
			arbeiter -= 2
			gruben += 1
			siegpunkte += 1.5
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n5 Erde, 5 Sand, 2 Eisen, 40 Holz, 2 Arbeiter")
	elif a == "4":#Fluss
		if erde >= 10 and wasser >= 10 and samen >=5 and lehm >=5 and sand >= 5:
			erde -= 10
			wasser -= 10
			samen -= 5
			lehm -= 5
			sand -= 5
			flüsse += 1
			siegpunkte += 2
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n10 Erde, 10 Wasser 5 Samen, 5 Lehm, 5 Sand")
	elif a == "5":#Weide
		if erde >= 15 and wasser >= 5 and arbeiter >= 1 and holz >= 65 and samen >= 30:
			erde -= 15
			wasser -= 5
			arbeiter -= 1
			holz -= 65
			samen -= 30
			weiden += 1
			siegpunkte += 2.5
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n15 Erde, 5 Wasser, 1 Arbeiter, 65 Holz, 30 Samen")
	elif a == "6":#Mühle
		if stein >= 15 and holz >= 80 and lehm >= 35 and wolle >= 50 and sand >= 20 and wasser >= 35 and arbeiter >= 3:
			stein -= 15
			holz -= 80
			lehm -= 35
			wolle -= 50
			sand -= 20
			wasser -= 35
			arbeiter -= 3
			mühlen += 1
			siegpunkte += 3
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n15 Stein, 80 Holz, 35 Lehm, 50 Wolle, 20 Sand, 35 Wasser, 3 Arbeiter")
	elif a == "7":#Mine
		if eisen >= 5 and stein >= 40 and holz >= 150 and wolle >= 50 and arbeiter >= 5 and wasser >= 30:
			eisen -= 5
			stein -= 40
			holz -= 150
			wolle -= 50
			arbeiter -= 5
			wasser -= 30
			minen += 1
			siegpunkte += 4
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n5 Eisen, 40 Stein, 150 Holz, 50 Wolle, 5 Arbeiter, 30 Wasser")
	elif a == "8":#Wohnhaus
		if stein >= 50 and holz >= 100 and wolle >= 20 and wasser >= 70 and sand >= 60 and lehm >= 50:
			stein -= 50
			holz -= 100
			wolle -= 20
			wasser -= 70
			sand -= 60
			lehm -= 50
			wohnhäuser += 1
			arbeiter += 20
			siegpunkte += 3.5
		else:
			print("Dir fehlt etwas!\nDu brauchst:\n50 Stein, 50 Holz, 20 Wolle, 60 Sand, 50 Lehm")
	elif a == "9":#Markt
		if stein >= 100 and holz >= 80 and wolle >= 50 and gold >= 24 and stroh >= 50:
			stein -= 80
			holz -= 100
			wolle -= 50
			gold -= 24
			stroh -= 50
			märkte += 1
			siegpunkte += 5
		else:
			print("Dir fehlt etwas\nDu brauchst:\n100 Stein, 80 Holz, 50 Wolle, 24 Gold, 50 Stroh")

	if runde == 75:
		break

print(colored(f"Du hast {siegpunkte} Siegpunkte", "yellow"))