import operator
class Irodalom:
    def __init__(self, szerzo, idezet, hossz):
        self.szerzo = szerzo
        self.idezet = idezet
        self.hossz  = hossz
    
with open('morzeabc.txt','r', encoding='latin2') as morzeabc_txt:
    morzeabc_txt.readline()                    # eldobjuk az első sort
    morze2abc = dict()
    abc2morze = dict()
    for sor in morzeabc_txt:
        x=sor.strip().split('\t')
        morze2abc[x[1]] = x[0]                 # szótár  morze2abc
        abc2morze[x[0]] = x[1]                 # szótár  abc2szotar

# 3. feladat ##########################################################
print( '3. feladat: A morze abc', len(morze2abc), 'db karakter kódját tartalmazza.' )

# 4. feladat ##########################################################
be = input('4. feladat: Kérek egy karaktert: ')
if be in abc2morze:
    print('A',be, 'karakter morze kódja:', abc2morze[be] )

# 5. feladat ##########################################################
with open('morze.txt','r', encoding='latin2') as morze_txt:
    sorok = morze_txt.read().split('\n')
        
# 6. feladat ##########################################################
def morze2szoveg(morze):
    szoveg = ''
    betu   = ''
    space  = 0
    for c in morze:
        if c == ' ':
            space += 1
        if space == 7:
            szoveg += ' '
            space = 0
            betu  = ''
        if c == '.' or c =='-':
            betu += c
            space = 0
        elif betu !='' and c == ' ':
            szoveg += morze2abc[betu]
            betu = ''
    return szoveg

# 7. feladat ##########################################################
lista = []
for s in sorok:
    sor = s.split(';')
    szerzo = morze2szoveg( sor[0] )
    idezet = morze2szoveg( sor[1] )
    lista.append(     Irodalom( szerzo, idezet, len(idezet) )     )
    
print( '7. feladat: Az első idézet szerzője:', lista[0].szerzo )

# 8. feladat ##########################################################
maxi = max( lista, key = operator.attrgetter('hossz'))
print( '8. feladat: A leghosszabb idézet szerzője és az idézet:', maxi.szerzo+':', maxi.idezet+'.')

# 9. feladat ##########################################################
print( '9. feladat: Arisztotelész idézetei:')
x = [print('          - '+sor.idezet+'.') for sor in lista if sor.szerzo =='ARISZTOTELÉSZ']

# 10. feladat ##########################################################
with open('forditas.txt','w', encoding='utf-8') as output_file:
    for sor in lista:
        print( sor.szerzo+':', sor.idezet+'.' , file=output_file)
    