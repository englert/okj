#sikeres.csv    A .csv  (comma-separated values:vesszővel elválasztott értékek ) formátum lehetővé teszi,
# a kölönböző rendszerek közötti szabványos adat átadást, pl az Excel - a LibreOffice Calc - bármely programozási nyelv esetén.

# Célszerű a feladat megoldása során a forrás fájl első két sorát rögtön a kódunk elejére írni, így látjuk annak szerkezetét.
# Célszerű az eggyes mezők alá írni az indexeket, így gyorsabban dolgozhatunk, kevesebb hibával.

# nyelv;2009;2010;2011;2012;2013;2014;2015;2016;2017;2018
#   0     1    2    3    4   5    6    7    8    9    10
# angol;116;441;709;620;656;445;471;480;695;554

with open('sikeres.csv','r', encoding='latin2') as sikeres_csv: # Olvasásra megnyitja a 'sikeres.csv' fájlt latin2-es kódolással sikeres_csv -ként.
    sikeres_matrix =[ sor.strip().split(';') for sor in sikeres_csv ]  # A .strip() leszedi az újsor karaktereket '\n', a .split(';') listává darabol
                                                                # a ';' mentén. A listákat (tömböket) betolja a sikeresek listába,
                                                                # így az egy kétdimenziós lista (tömb) lesz, azaz mátrix.
                                                                # A with utasítás blokkot elhagyva az automatikusan lezárja a nyitott fájlt.
  
with open('sikertelen.csv','r', encoding='latin2') as sikertelen_csv:
    sikertelen_matrix =[ sor.strip().split(';') for sor in sikertelen_csv ]

# A forrás fájlokban (sikeres.csv, sikertelen.csv) levő adatok szövegként vabnnak tárolva,
# így jelenleg a (sikeres, sikertelen) mátrixban is célszerű ezeket számokká alakítani: 
for i in     range(0, len(sikeres_matrix) ):                   # minden soron végigmegy
    for j in range(1, len(sikeres_matrix[0]) ):                # kihagyja az első oszlopot (nyelv) 
        sikeres_matrix[i][j] = int( sikeres_matrix[i][j] )     # int-re alakitja az str-ben levő adatokat 
    
for i in     range(0, len(sikertelen_matrix) ):
    for j in range(1, len(sikertelen_matrix[0]) ):
        sikertelen_matrix[i][j] = int( sikertelen_matrix[i][j] )
        
fejlec = sikeres_matrix[0]   
del sikeres_matrix[0]
del sikertelen_matrix[0]

# 2. feladat: Kilenc év sikeres és sikertelen vizsgáit összegezve melyik 3 nyelv volt a legnépszerűbb!        
osszes_vizsga_nyelvenkent     = []
for i in range( 0, len(sikeres_matrix) ):
    nyelv = sikeres_matrix[i][0]
    sikeres    = sum(sikeres_matrix[i][1:])
    sikertelen = sum(sikertelen_matrix[i][1:])
    osszes       = sikeres + sikertelen        # a nyelv kilenc év alatti összes vizsga száma 
    
    osszes_vizsga_nyelvenkent.append( ( osszes, nyelv ) )

res = sorted(osszes_vizsga_nyelvenkent, reverse=True)[:3]
print( f'2. feladat: a legnépszerübb nyelvek:' )
[print(f'     { sor[1] }')  for sor in res]

# 3. feladat:
print( f'3. feladat:')
while True:
    ev = int(input('Kérek egy évet 2009 és 2017 között:'))
    if 2008 < ev < 2018:
        break

# 4. feladat: A bekért évben melyik volt az a nyelv, amely esetében a legnagyobb volt a sikertelen vizsgák aránya!
# (Az arány meghatározásánál vegye figyelembe a sikertelen és az összes vizsga számát!)
# A nyelv mellett – két tizedesjegy pontossággal – írja ki azt is, hogy mekkora volt a sikertelen vizsgák aránya!
ind = fejlec.index(ev)
sikeres_vizsgak    = [((sor[ind]), sor[0]) for sor in sikeres_matrix   ] 
sikertelen_vizsgak = [((sor[ind]), sor[0]) for sor in sikertelen_matrix]
osszes_vizsga = list(zip( sikertelen_vizsgak,sikeres_vizsgak))
sikertelen_aranyok = [(sor[0][0] / (sor[0][0] + sor[1][0]), sor[0][1]) for sor in osszes_vizsga if (sor[0][0] + sor[1][0]) != 0]
legnagyobb_sikertelen_arany = sorted( sikertelen_aranyok, reverse=True)[:1][0]
print( f'4. feladat:')
print( f'     {ev}-ben {legnagyobb_sikertelen_arany[1]} nyelvből a sikertelen vizsgák aránya {100*legnagyobb_sikertelen_arany[0]:.2f}%')

# 5. feladat: Írja ki a képernyőre azon nyelveket, amelyekből a 3. feladatban megadott évben nem volt egyetlen vizsgázó sem.
# Ha nem volt ilyen nyelv, akkor írja ki, hogy „ Minden nyelvből volt vizsgázó".
print( f'5. feladat')
nem_volt_vizsga = [  sor[0][1] for sor in osszes_vizsga if (sor[0][0] + sor[1][0]) == 0]

if len(nem_volt_vizsga) == 0:
    print( f'  Minden nyelvből volt vizsgázó')
else:
    [print(f'     {sor}') for sor in nem_volt_vizsga]
    
# 6. feladat
# Készítsen összesítést az adatokból, amelynek eredményét mentse osszesites.csv állományba!
# Az állomány minden sora – pontosvesszővel elválasztva – tartalmazza:
# a nyelvet, # a kilenc év alatti összes vizsga számát, a sikeres vizsgák arányát két tizedesjegyre kerekítve
#

with open('osszesítes.csv','w') as fajl:
    for i in range( len(sikeres_matrix) ):         
        nyelv        = sikeres_matrix[i][0]
        sikeres    = sum(sikeres_matrix[i][1:])
        sikertelen = sum(sikertelen_matrix[i][1:])
        osszes       = sikeres + sikertelen       
        sikeres_arany= sikeres / osszes
        print( f'{ nyelv };{ osszes };{ 100*sikeres_arany:.2f}%', file=fajl) 


