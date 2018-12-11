# Skrifið Python forrit sem les inn tvær heiltölur frá notanda. 
# Fyrri talan stendur fyrir upphafsgildi á röð og seinni talan stendur fyrir mismun á sérhverjum samliggjandi gildum raðarinnar. 
# Forritið skrifar síðan út sérhvert gildi raðarinnar (með einu bili á milli gilda) þangað til summa gildanna er orðin >= 100. 
# Í lokin skrifast jafnframt út summan.
# Inntak/úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.

n = int(input('Initial value: '))
step = int(input('Step: '))

total = 0

while total < 100:
    print(n,end=' ')
    total += n
    n += step

print('')
print('Sum of series: {}'.format(total))