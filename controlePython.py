from colorama import init
init()
from colorama import Fore, Back, Style
import random

#fonctions
def tourJoueur(motMystere):
	motJoueur = int(input("Entrez un mot : "))
	print(motJoueur)
	for i in range(0,6):
		if motJoueur[i] == motMystere[i]:
			print("test")

#main program
listeDeMot = ["castor","cinema","citron","cypres","basile","totoro","atouts","romain","projet","macron"]
motAleatoire = random.randint(0,9)
motMystere = listeDeMot[motAleatoire]

tourJoueur(motMystere)