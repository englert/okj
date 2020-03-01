#név;első;utolsó;súly;magasság
# 0    1    2     3      4
#Jim Abbott;1989-04-08;1999-07-21;200;75
class Basseball:
    def __init__( self, row ):
        r             = row.strip().split(';')
        self.név      =      r[0]
        self.első     =      r[1]
        self.utolsó   =      r[2]
        self.súly     = int( r[3] )
        self.magasság = int( r[4] )

with open( 'balkezesek.csv', 'r', encoding='latin2' ) as forras:
    forras.readline()
    lista = [ Basseball( sor ) for sor in forras ]
    
print(f"3. feladat: { len( lista ) }")

print(  f"4. feladat:")
[print( f"        {sor.név}, { sor.magasság * 2.54:.2f} cm") for sor in lista if sor.utolsó[:7] == '1999-10']

print(f"5. Feladat:")
while True:
    evszam = int( input('Kérek egy 1990 és 1999 közötti évszámot:') )
    if (1990 <= evszam <= 1999):
        break
    else:
        print('Hibás adat!',end='')

sulyok = [sor.súly for sor in lista if sor.első[:4] <=str(evszam) <= sor.utolsó[:4]]
atlag = sum(sulyok)/ len(sulyok)

print(f"6. feladat: {atlag:.2f} font")