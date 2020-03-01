#nobel.csv
#év;típus;keresztnév;vezetéknév
# 0    1      2          3
#2017;fizikai;Rainer;Weiss
class Nobel:
    def __init__(self, row):
        r = row.strip().split(';')
        self.ev          = int( r[0] )
        self.tipus       =      r[1]
        self.keresztnev  =      r[2]
        self.vezeteknev  =      r[3]
# 2.
with open('nobel.csv','r', encoding='utf-8-sig') as f:
    fejlec = f.readline()
    lista = [ Nobel( sor ) for sor in f ]

# 3. Milyen díjat kapott  Arthur B. McDonald?
[ print( f"3. feladat: { sor.tipus }" ) for sor in lista if sor.keresztnev=='Arthur B.' and sor.vezeteknev == 'McDonald' ]

# 4. Ki kapott 2017-ben irodalmi Nobelt?
[ print( f'4. feladat: { sor.keresztnev } { sor.vezeteknev }') for sor in lista if sor.ev == 2017 and sor.tipus == 'irodalmi' ]

# 5. Mely szervezetek kaptak Nobelt 1990-től napjainkig.
# Ha szervezet kap díjat, akkor a vezeteknev üres.
print(   f'5. feladat:' )
[ print( f'        { sor.ev }: { sor.keresztnev }' ) for sor in lista if sor.vezeteknev == '' and sor.ev > 1989 ]

# 6. A Curie család díjai:
print(  f'6. feladat:')
[print( f'        { sor.ev }: { sor.keresztnev } { sor.vezeteknev }( {sor.tipus })' ) for sor in lista if 'Curie' in sor.vezeteknev ]

# 7. Melyik díjból, hány darab?
dijak =  { sor.tipus: 0 for sor in lista }
print(   f'7. feladat:' )

for sor in lista:
    dijak[sor.tipus] += 1
    
[ print( f'        {dij:15} { darab:6} db' ) for dij, darab in dijak.items() ]

# 8. Orvosi Nobel díjak:  orvosi.txt
with open('orvosi.txt', 'w') as orvosi_txt:
    [ print( f"{sor.ev};{sor.keresztnev} {sor.vezeteknev}", file = orvosi_txt ) for sor in lista if sor.tipus == 'orvosi' ]