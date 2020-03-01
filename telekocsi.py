
# 1. olvassa be és tárolja az autok.csv fájl tartalmát
# autok.csv
#Indulás;Cél;Rendszám;Telefonszám;Féröhely
#  0      1     2        3          4
#Eger;Salgótarján;PQA-209;30/771-8574;5
class Autok:
    def __init__(self, row):
        r    = row.strip().split(';')
        self.indulás     =     r[0]
        self.cél         =     r[1]
        self.rendszám    =     r[2]
        self.telefonszám =     r[3] 
        self.féröhely    = int(r[4]) 
        
with open( 'autok.csv', 'r', encoding='latin2') as f:
    autok_fejléc = f.readline()
    autók = [ Autok( sor ) for sor in f ]
    
# 2. Hány hirdető adata van az autok.csv-ben
print( f'2. feladat')
print( f'   {len(autók)} autós hirdet fuvart')

# 3. Budapestről Miskolcra hány férőhelyet hírdettek
bp2miskolc = [autó for autó in autók if autó.indulás == 'Budapest' and autó.cél == 'Miskolc']
print( f'3. feladat')
print( f'   Összesen { len(bp2miskolc)} férőhelyet hírdettek az autósok Budapestről Miskolcra')

# 4. Melyik volt az az útvonal, amelyhez a legtöbb férőhelyet ajánlották fel.
import collections

cnt = collections.Counter()
for autó in autók:
    útvonal = autó.indulás + '-' + autó.cél
    cnt[útvonal] += 1

csökkenő = sorted(cnt.items(), key = lambda x: x[1], reverse=True)    
print( f'4. feladat')
print( f'   A  legtöbb férőhelyet ({csökkenő[0][1]}-et) a {csökkenő[0][0]} útvonalon ajánlották fel a hirdetők')

#5. Az igenyek.csv beolvasásával  határozza meg és írja ki az igényekre a választ
# igenyek.csv
#Azonosító;Indulás;Cél;Személyek
#    0        1     2      3
#B34019;Brassó;Gyula;3
class Igenyek:
    def __init__(self, row):
        r = row.strip().split(';')
        self.azonosító =      r[0]
        self.indulás   =      r[1]
        self.cél       =      r[2]
        self.személyek = int( r[3] )
       
with open( 'igenyek.csv', 'r', encoding='latin2') as f:
    igenyek_fejléc = f.readline()
    igenyek = [ Igenyek( sor ) for sor in f ] 


output = open( 'utasuzenetek.txt', 'w') 
print( f'5. feladat')

for sor in igenyek:
    azonosító = sor.azonosító
    indulás   = sor.indulás
    cél       = sor.cél
    személyek = sor.személyek
    res = [autó for autó in autók if autó.indulás == indulás and autó.cél == cél and autó.féröhely >= személyek  ]
    if len( res ) > 0:
        print( f'{azonosító} => {res[0].rendszám}' )
        
# 6. Készítsen utasüzenetek.txt fájlt
        print( f'{azonosító}: Rendszám: {res[0].rendszám}, Telefonszám: {res[0].telefonszám}' , file = output)
    else:
        print( f'{azonosító}: Sajnos nem sikerült autót találni', file = output )
        
output.close()