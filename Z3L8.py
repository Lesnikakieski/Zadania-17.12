from itertools import combinations
import re


with open('popularne_slowa2023.txt', encoding='utf-8') as file:
    popularne_slowa = set(line.strip().lower() for line in file)

def znajdz_pare(imie_nazwisko):
    czysty_tekst = re.sub(r'[^a-zA-Z]', '', imie_nazwisko.lower())
    dlugosc = len(czysty_tekst)
    slowa_kandydaci = [slowo for slowo in popularne_slowa if len(slowo) <= dlugosc]

    for slowo1, slowo2 in combinations(slowa_kandydaci, 2):
        if len(slowo1) + len(slowo2) == dlugosc:
            if sorted(slowo1 + slowo2) == sorted(czysty_tekst):
                return slowo1, slowo2
    return None


imie_nazwisko = "Jan Kowalski"  
para = znajdz_pare(imie_nazwisko)
if para:
    print(f"Znaleziono parę słów: {para[0]} + {para[1]}")
else:
    print("Nie znaleziono pasującej pary słów.")
