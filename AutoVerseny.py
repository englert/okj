'''https://infojegyzet.hu/vizsgafeladatok/okj-programozas/rendszeruzemelteto-koridok/
autoverseny.csv:
csapat;versenyzo;eletkor;palya;korido;kor
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1
'''
class AutóVerseny:
    def __init__( self, sor ):
        csapat,versenyzo, eletkor, palya, korido, kor = sor.strip().split( ';' )
        self.csapat       = csapat  
        self.versenyzo    = versenyzo 
        self.eletkor      = int(eletkor)
        self.palya        = palya 
        self.korido       = korido
        self.korido_split = [ int(i)  for i in korido.split( ':' ) ]
        self.korido_sec   = 3600 * int( korido[:2] ) + 60 * int( korido[3:5] ) + int( korido[6:] ) 
        self.kor          = int(kor)
        
with open( 'autoverseny.csv', 'r', encoding='utf-8-sig' ) as f:
    fejléc = f.readline()
    matrix = [AutóVerseny( sor ) for sor in f]

#3    
print( f'3. feladat: { len( matrix ) }')

#4. 
t = [sor.korido_sec for sor in matrix if sor.versenyzo == 'Fürge Ferenc' and sor.palya == 'Gran Prix Circuit' and sor.kor == 3 ][0]
print( f'4. feladat: { t } másodperc' )

#5.
print( f'5. feladat:')
print( f'Kérem egy versenyző nevét:' )
nev = input()
if nev not in  [ sor.versenyzo for sor in matrix ]:
    print( f'    Nincs ilyen versenyző az állományban!' )
else:
    res = { sor.korido_sec:sor for sor in matrix if sor.versenyzo == nev }
    ido, sor = min(res.items())
    print( f'6. feladat: {sor.palya}, {sor.korido}')
