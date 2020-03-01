# fuvar.csv:
#taxi_id;indulas;             idotartam; tavolsag; viteldij; borravalo; fizetes_modja
#   0        1                    2         3         4        5           6
#5240   ;2016-12-15 23:45:00;    900;      2,5;    10,75;    2,45;       bankkártya

class Fuvar:
    def __init__( self, row ):
        r = row.strip().replace(',','.').split(';')
        self.taxi_id       =   int( r[0] )
        self.indulas       =        r[1]
        self.idotartam     =   int( r[2] )
        self.tavolsag      = float( r[3] )
        self.viteldij      = float( r[4] )
        self.borravalo     = float( r[5] )
        self.fizetes_modja =        r[6]
         
with open('fuvar.csv', 'r', encoding = 'utf-8-sig') as f:
    elsosor = f.readline()
    lista   = [ Fuvar( sor ) for sor in f ]

# 3. Hány utazás van?
print( f"3. feladat: { len( lista ) } fuvar")

# 4. a 6185-ös azonosítójú taxisnak mennyi volt a bevétele, és ez hány fuvarból állt?
bevetel = [ sor.viteldij + sor.borravalo  for sor in lista if sor.taxi_id == 6185 ]
print( f"4. feladat: { len(bevetel) } fuvar alatt: { sum(bevetel)} $")

# 5. határozza meg a fizetési módokat,  az egyes fizetési módokat hányszor választották az utak során?
import collections
cnt = collections.Counter()

for sor in lista:
    cnt[ sor.fizetes_modja ] += 1
    
statisztika = sorted( cnt.items(), key=lambda x: x[1], reverse=True )
print(   f'5. feladat:'                          ) 
[ print( f'        { sor[ 0 ] }: { sor[1]} fuvar') for sor in statisztika ]

# 6. Összesen hány km-t tettek meg a taxisok 2 tizedes pontossággal (1 mérföld 1,6 km)
km = [ sor.tavolsag for sor in lista ]
print(f'6. feladat:{ sum( km ) * 1.6 :.2f} km')

# 7. az időben leghosszabb fuvar adatai:
maxi = max(lista, key = lambda x: x.idotartam )
print(f'17. feladat: Leghosszabb'                                 )
print(f'        Fuvar hossza: {     maxi.idotartam} másodperc'    )
print(f'        Taxi azonosító: {   maxi.taxi_id }'               )
print(f'        Megtett távolság: { 1.6 * maxi.tavolsag :.2f} km' )
print(f'        Viteldíj: {         maxi.viteldij } $'            )

'''
8. Hozzon létre hibak.txt néven egy UTF-8 kódolású szöveges állományt.
Hibás sornak tekintjük azokat az eseteket, amelyekben az utazás időtartama és a viteldíj egy nullánál nagyobb érték,
de a hozzá tartozó megtett távolság értéke nulla.
A sorok indulási időpont szerint növekvő rendben legyenek az állományban!
'''
print( "8. feladat: hibak.txt" )
with open('fuvar.csv', 'r', encoding = 'utf-8-sig') as file:
    elsosor = file.readline()
    fuvarlista   = [sor.strip() for sor in file ]
    
with open('hibak.txt','w',encoding = 'utf-8') as output:
     output.writelines(elsosor)
     hibak = [ (sor.indulas, i) for i, sor in enumerate(lista) if (sor.idotartam != 0 and sor.viteldij != 0.0) and sor.tavolsag ==0.0 ]
     hibak_rendezve = sorted( hibak )
     [ print( fuvarlista[i], file = output ) for indulas , i in hibak_rendezve]



