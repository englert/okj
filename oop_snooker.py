#Helyezes;Nev;Orszag;Nyeremeny
#    0   ; 1 ;   2  ;    3

class Snooker:
    def __init__( self, row ):
        r = row.strip().split(';')
        
        self.dij      = int( r[3] )
        self.helyezes =      r[0]
        self.nev      =      r[1]
        self.orszag   =      r[2]


#2.feladat
with open( "snooker.txt", encoding="latin2" ) as f:
    fejlec=f.readline()
    matrix=[ Snooker(s) for s in f ]

#3.feladat
print( f'3. feladat: A világranglistán { len( matrix ) } versenyző szerepel' )

#4.feladat
osszes = sum( [ sor.dij for sor in matrix ] ) 
print( f'4. feladat: A versenyzők átlagosan {osszes / len( matrix ):.2f} fontot kerestek' )

#5.feladat
kinaiak  = [ ( sor.dij, sor ) for sor in matrix if sor.orszag == "Kína" ]
dij, sor = max( kinaiak )
print( f'5. feladat: A legjobban kereső kínai versenyző:' )
print( f'        Helyezés: {sor.helyezes}'                )
print( f'        Név: {sor.nev}'                          )
print( f'        Ország: {sor.orszag}'                    )
print( f'        Nyeremény összege: { sor.dij * 380 } Ft' )

#6.feladat 
norvegok = [ sor.orszag for sor in matrix if sor.orszag == "Norvégia" ]

if len( norvegok ) > 0:
    print( "6. feladat: A versenyzők között van norvég versenyző."   )
else:
    print( "6. feladat: A versenyzők között nincs norvég versenyző." )
    
#7.feladat
    
orszagok = { sor.orszag : 0 for sor in matrix }

for sor in matrix:
    orszag = sor.orszag
    orszagok[ orszag ] += 1

[ print(f'  { orszag } { darab } ')  for orszag, darab in orszagok.items() if darab > 4]
        



