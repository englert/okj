#csapat;       versenyzo;    eletkor; palya;             korido;   kor
#   0               1           2        3                 4        5
#Versenylovak; Fürge Ferenc; 29;      Gran Prix Circuit; 00:01:11; 1

class AutóVerseny:
    def __init__( self, sor ):
        s                 = sor.strip().split( ';' )
        self.csapat       =      s[0]
        self.versenyzo    =      s[1]
        self.eletkor      = int( s[2] )
        self.palya        =      s[3]
        self.korido_split =[ int(i)  for i in s[4].split( ':' ) ]
        self.korido       =      s[4]
        self.korido_sec   = 3600 * int( s[4][:2] ) + 60 * int( s[4][3:5] ) + int( s[4][6:] ) 
        self.kor          = int( s[5] )
        
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
