import przepisy as p
from colorama import Fore, Back, Style


# colorama - https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

def x():
	return (len(p.thisdict))

def y():
	return (list(p.thisdict.keys()))

def liczbaprzepisow():
	print ("≧◉ᴥ◉≦<" +Fore.BLACK+Back.LIGHTWHITE_EX+ "(Aktualnie dostepne na liscie sa " + str(x()) + " przepisy.)"+ Style.RESET_ALL)

print(Style.DIM +Fore.BLACK+Back.LIGHTMAGENTA_EX+ "$"*10 +"  KSIAZKA KUCHARSKA MARYSIA!!!! sza "+ "$"*10 + Style.RESET_ALL)
liczbaprzepisow()

print("≧◉ᴥ◉≦<" +Back.BLUE + "(Oto spis tresci)"+Style.RESET_ALL)
print( "-"*40)

for elem in y(): print(Fore.RED+ "-->" + str(elem))
print(Style.RESET_ALL + "-"*40)

print(Style.RESET_ALL +Style.BRIGHT+ "≧◉ᴥ◉≦<" +Fore.LIGHTWHITE_EX+Back.BLACK+ "(Jakiego przepisu chcesz uzyc?) Wpisz nazwe bez polskich znakow: " + Style.DIM + Fore.LIGHTCYAN_EX)
x = input()


#https://www.datacamp.com/community/tutorials/elif-statements-python
if x=="szarlotka":
	for elem in p.thisdict["szarlotka"]:
		for letter in elem:
			print(letter, end='')
			if letter == ':':
				print()
			if letter == '.':
				print()

elif x=="platki z mlekiem":
	for elem in p.thisdict["platki z mlekiem"]:
		for letter in elem:
			print(letter, end='')
			if letter == ':':
				print()
			if letter == '.':
				print()
			
elif x=="zupa pomidorowa":
		for elem in p.thisdict["zupa pomidorowa"]:
			for letter in elem:
				print(letter, end='')
				if letter == ':':
					print()
				if letter == '.':
					print()
else:
	print("≧◉ᴥ◉≦< \n"+ Fore.RED + "(Ups! Nie mam jeszcze tego przepisu!)")
