from colorama import init
init()
from colorama import Fore, Back, Style
import random

#fonctions
def tourJoueur(motMystere):
	print(Style.RESET_ALL)
	motJoueur = input("Entrez un mot : ")
	print(motMystere)
	if len(motJoueur) > 6:
		print("Entrez un mot de 6 lettres")
	if len(motJoueur) < 6:
		print("Entrez un mot de 6 lettres")
	else:
		for i in range(0,6):
			if motJoueur[i] == motMystere[i]:
				print(Back.RED + motJoueur[i], end="")
			else:
				print(Back.BLUE + motJoueur[i], end="")
	return motJoueur


def lettresCommunes(motJoueur, motMystere):
	print("\n")
	for i in range(0,6):
		lettreCommune = motMystere[i]
		for j in range(0,6):
			if motJoueur[j] == lettreCommune:
				print(Back.YELLOW, lettreCommune, end="", sep="")
			if motJoueur[j] != lettreCommune:
				print(Back.BLUE, lettreCommune, end="", sep="")

def testVictoire(motJoueur, motMystere):
	if motJoueur == motMystere:
		victoire = True
	else:
		victoire = False
	return victoire

#main program
listeDeMot = ["castor","cinema","citron","cypres","basile","totoro","atouts","romain","bateau","macron"]
motAleatoire = random.randint(0,9)
motMystere = listeDeMot[motAleatoire]
tour = 1
victoire = False
print("motMystere = ", motMystere)

while tour < 9 and victoire != True:
	print(Style.RESET_ALL)
	print("\nTour n°", tour, sep="")
	motJoueur = tourJoueur(motMystere)
	lettresCommunes(motJoueur, motMystere)
	victoire = testVictoire(motJoueur, motMystere)
	tour = tour + 1

print(Style.RESET_ALL)

if victoire == False:
	print("\nPerdu ! Le mot était : ", motMystere)
if victoire == True:
	print("\nGagné !")
input()