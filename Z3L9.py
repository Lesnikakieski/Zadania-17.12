from collections import defaultdict

def zlicz_liczby_dzielnikow(n):
    dzielniki = [0] * (n + 1)  
    wynik = defaultdict(int)    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            dzielniki[j] += 1 
    for liczba_dzielnikow in dzielniki[1:]:
        wynik[liczba_dzielnikow] += 1
    return sorted(wynik.items())

n = 10**6  
wynik = zlicz_liczby_dzielnikow(n)
print(wynik)
