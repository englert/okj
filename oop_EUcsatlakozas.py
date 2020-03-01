# EUcsatlakozas.txt
# Ausztria;1995.01.01
# Belgium;1958.01.01

class EU_csatlakozas:
    def __init__(self, row):
        r = row.strip().split(';')
        self.orszag = r[0]
        self.datum  = r[1]
        
with open( 'EUcsatlakozas.txt', 'r', encoding='latin2' ) as f:
    lista = [ EU_csatlakozas( sor ) for sor in f ]

# 3.
print( f' 3.feladat: EU tagállamainak szama: { len( lista ) } db')

# 4.
ketezerhetben = [ sor.orszag for sor in lista if sor.datum[:4] == '2007']
print( f' 4.feladat: 2007-ben { len( ketezerhetben ) } ország csatlakozott.'       )

# 5.
csatlakozas = [ print( f' 5.feladat: Magyarország csatlakozásának dátuma: { sor.datum }') for sor in lista if sor.orszag == 'Magyarország' ]

# 6.
majusban = [ sor.orszag for sor in lista if sor.datum[ 5:7 ] == '05' ]
if len( majusban ) > 0:
    print( f' 6.feladat: Májusban volt csatlakozás!'             )
else:
    print( f' 6.feladat: Májusban nem volt csatlakozás!'         ) 

# 7.
csatlakozas = [ ( sor.datum, sor ) for sor in lista ]
datum, sor = max( csatlakozas )                
                     
print( f' 7.feladat: Legutoljára csatlakozott ország: {sor.orszag}'   )

#8.
evek = { sor.datum[:4] : 0 for sor in lista }

for sor in lista:
    evek[ sor.datum[:4] ] += 1

print(     f' 8.feladat: Statisztika' )

#for datum, db in evek.items():
[ print( f'        { datum[:4] } - { db } ország') for datum, db in evek.items()]




