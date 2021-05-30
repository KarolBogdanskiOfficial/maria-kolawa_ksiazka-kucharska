import przepisy as p
import pprint
    
def x():
    print(len(p.thisdict))

def y():
    print(list(p.thisdict.keys()))

def liczbaprzepisow():
    print ("≧◉ᴥ◉≦<(Aktualnie dostepne na liscie sa " + 'x()' + " przepisy.)")
    #probowalem tu zrobic cos zeby ta liczba przepisow pokazala sie w jednym zdaniu ale zrobilem tak jak nizej >:(



print ("≧◉ᴥ◉≦<(Hej, Aktualna liczba przepisow na liscie to: ")
x() #tu bym chcial zeby ta liczba wlasnie byla u gory :( leeee

print("≧◉ᴥ◉≦<(Oto spis tresci)")

y() #jak zrobic zeby to sie wyswietlalo jako lista tak ze spacjami? a nie w jednej linii

print("≧◉ᴥ◉≦<(Jakiego przepisu chcesz uzyc?) Wpisz nazwe bez polskich znakow: ")
#x = input()
x = "szarlotka"
if x=="szarlotka":
    # print(p.thisdict["szarlotka"])   #jak zrobic zeby wyszukalo te przepisy niezaleznie od rozmiaru liter jakie ktos wpisze?
    pp = pprint.PrettyPrinter(indent=10)
    pprint.pformat(pp, indent=1, width=80, depth=None, compact=False, sort_dicts=True)
    pp.pprint(p.thisdict["szarlotka"])

if x=="platki z mlekiem":
    print(p.thisdict["platki z mlekiem"])
elif x=="zupa pomidorowa":
    print(p.thisdict["zupa pomidorowa"])
else:
    print("≧◉ᴥ◉≦<(Ups! Nie mam jeszcze tego przepisu!)")
