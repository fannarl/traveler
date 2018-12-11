# Skrifið Python forrit sem skrifar út margföldunartöfluna fyrir tölurnar 1-10 (báðar meðtaldar).
# Úttak forritsins á að vera nákvæmlega eins og fram kemur í dæminu hér fyrir neðan.
# Breidd sérhverrar tölu er 5 og sérhver tala er hægri jöfnuð.

MAX = int(input('mult table:'))

for i in range(1, MAX + 1):
    for j in range(1, MAX + 1):
        print('{:>5d}'.format(i * j), end="")
    print('')