from itertools import combinations
import re
from collections import Counter

def wczytaj_liste_slow(sciezka_pliku):
    with open(sciezka_pliku, 'r') as f:
        return [slowo.strip().lower() for slowo in f]

def czy_pasuje(slowo1, slowo2, slowo3, liczniki_liter):
    suma_licznik = Counter(slowo1) + Counter(slowo2) + Counter(slowo3)
    return suma_licznik == liczniki_liter

def znajdz_trojki_wyrazow(litery, lista_slow):
    czyste_litery = re.sub(r'[^a-zA-Z]', '', litery.lower())
    liczniki_liter = Counter(czyste_litery)
    dlugosc = len(czyste_litery)
    slowa_kandydaci = [slowo for slowo in lista_slow if len(slowo) <= dlugosc and not (Counter(slowo) - liczniki_liter)]
    wyniki = set()
    for slowo1, slowo2, slowo3 in combinations(slowa_kandydaci, 3):
        if len(slowo1) + len(slowo2) + len(slowo3) == dlugosc:
            if czy_pasuje(slowo1, slowo2, slowo3, liczniki_liter):
                wynik = tuple(sorted([slowo1, slowo2, slowo3]))
                wyniki.add(wynik)
    return wyniki

litery = "Jan Kowalski"
lista_slow = wczytaj_liste_slow("popularne_slowa2023.txt")
trojki = znajdz_trojki_wyrazow(litery, lista_slow)

if trojki:
    print("Znalezione trójki słów:")
    for trojka in sorted(trojki):
        print(" ".join(trojka))
else:
    print("Nie znaleziono pasujących trójek słów.")
