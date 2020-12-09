from colorama import init
init()
from colorama import Fore, Back, Style
import random

#fonctions
def tourJoueur(motMystere):
	motJoueur = input("Entrez un mot : ")
	print(motJoueur)
	if len(motJoueur) > 6:
		print("Entrez un mot de 6 lettres")
	else:
		for i in range(0,6):
			if motJoueur[i] == motMystere[i]:
				print(Back.RED + motJoueur[i], end="")

#main program
listeDeMot = ["castor","cinema","citron","cypres","basile","totoro","atouts","romain","projet","macron"]
motAleatoire = random.randint(0,9)
motMystere = listeDeMot[motAleatoire]
print("motMystere = ", motMystere)

tourJoueur(motMystere)
input()