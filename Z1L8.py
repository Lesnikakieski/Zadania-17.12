import random
from collections import defaultdict, Counter


pol_ang = defaultdict(list)
for line in open('pol_ang.txt', encoding='utf-8'):
    line = line.strip()
    parts = line.split('=')
    if len(parts) == 2:
        pol, ang = parts
        pol_ang[pol].append(ang)


brown_words = Counter()
for line in open('BROWN.txt'):
    words = line.strip().lower().split()
    brown_words.update(words)

print(brown_words)

def tlumacz(polskie):
    tlumaczenia_historia = defaultdict(int)
    wynik = []
    for s in polskie:
        if s in pol_ang:
            mozliwe_tlumaczenia = sorted(pol_ang[s], key=lambda w: -brown_words[w.lower()])
            indeks = tlumaczenia_historia[s] % len(mozliwe_tlumaczenia)
            wynik.append(mozliwe_tlumaczenia[indeks])
            tlumaczenia_historia[s] += 1
        else:
            wynik.append('[?]')
    return ' '.join(wynik)


zdanie = 'chłopiec chłopiec z dziewczyna kino dziewczyna pójść pójść do kino'.split()

print(tlumacz(zdanie))
