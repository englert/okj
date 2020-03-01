#Év;Elem;Vegyjel;Rendszám;Felfedező
# 0   1     2       3         4
#Ókor;Szén;C;6;Ismeretlen
#1250;Arzén;As;33;Albertus Magnus

class Kemia:
    def __init__(self, row):
        r = row.strip().replace(u'\xa0', u' ').split(';')
        self.ev        = r[0]
        self.elem      = r[1]
        self.vegyjel   = r[2]
        self.rendszam  = r[3]
        self.felfedezo = r[4]

with open( 'felfedezesek.csv', 'r' ) as f:
    fejlec  = f.readline()
    lista   = [ Kemia(sor) for sor in f ]

# 3. 
print( f'3. feladat: Elemek száma: { len(lista) }' )

# 4. 
okor = [ sor for sor in lista if sor.ev == 'Ókor' ]
print( f'4. feladat: Felfedezések száma az ókorban: { len(okor) }' )

# 5. 
while True:
    be = input( f'5. feladat: Kérek egy vegyjelet: ' )
    if ( 0 < len(be) <3 ) and be.isalpha():
        vegyjel = be.upper()
        break

# 6. #
print(     f'6. feladat: Keresés'                        )
elemek = { sor.vegyjel.upper() : sor for sor in lista }
if vegyjel in elemek:
    elem = elemek[ vegyjel ]
    print( f'        Az elem vegyjele: { elem.vegyjel }' )
    print( f'        Az elem neve:     { elem.elem }'    )
    print( f'        Rendszáma:        { elem.rendszam}' ) 
    print( f'        Felfedezés éve:   { elem.ev}'       )
    print( f'        Felfedező:        { elem.felfedezo}')
else:
    print( f'        Nincs ilyen elem az adatforrásban!' ) 

# 7. #
okor_utan  = [ int( sor.ev    ) for sor in  lista if  sor.ev != 'Ókor']
evek_szama =   len( okor_utan )
dif  = [ okor_utan[ i+1 ] - okor_utan[ i ] for i in range( evek_szama-1 ) ]
print(f'7. feladat: { max(dif) }, év volt a leghosszabb időszak két elem felfedezése között.' )

# 8. #

print(  f'8. feladat: Statisztika'               )
[ print(f'       { ev }: { okor_utan.count( ev ) } db') for ev in set( okor_utan )  if  okor_utan.count( ev ) > 3 ]
    