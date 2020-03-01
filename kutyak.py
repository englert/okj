# 1. feladat: hozzon létre konzol alkalmazást kutyak azonosítóval.

#------------------------------------------------------------
# 2. feladat: Olvassa be a KutyaNevek.csv állományt és tárolja le egy megfelelő adatszerkezetben.

# KutyaNevek.csv
#id;kutyanév
#1;Akina
        
with open( 'KutyaNevek.csv', 'r', encoding='utf-8-sig' ) as f:
    kutya_nevek_fejlec = f.readline()
    kutya_nevek = dict()
    for sor in f:
        s                    = sor.strip().split( ';' )
        index                = int( s[0] )
        kutya_nevek[ index ] =      s[1] # kutya neve
    
#------------------------------------------------------------
# 3. feladat: Határozza meg és írja ki, hogy hány kutyanév található az állományban.
print( f'3. feladat: Kutyanevek száma: { len( kutya_nevek) }' )

#------------------------------------------------------------
# 4. feladat: Olvassa be a KutyaFajtak.csv állományt és tárolja le egy megfelelő adatszerkezetben.
#KutyaFajtak.csv
#id;név;eredeti név
#1;Abruzzói juhászkutya;Cane da pastore Maremmano-Abruzzese
#2;Afgán agár;Afghan Hound

with open( 'KutyaFajtak.csv', 'r', encoding='utf-8-sig' ) as f:
    fajta_fejlec = f.readline()
    fajta_nevek          = dict()
    fajta_eredeti_nevek  = dict()
    for sor in f:
        s  = sor.strip().split( ';' )
        index                          = int( s[0] )
        fajta_nevek[ index ]           =      s[1]   # fajta_név
        fajta_eredeti_nevek[ index ]   =      s[2]   # fajta_eredeti_név
    
#------------------------------------------------------------
# 5. feladat: Olvassa be a Kutyak.csv állományt és tárolja le egy megfelelő adatszerkezetben.

#Kutyak.csv
#id;fajta_id;név_id;életkor;utolsó orvosi ellenőrzés
#1;307;107;14;2017.11.27
class Kutya:
    def __init__( self, row ):
        r = row.strip().split( ';' )
        self.id        = int( r[0] )
        self.fajta_id  = int( r[1] )
        self.név_id    = int( r[2] )
        self.életkor   = int( r[3] )
        self.orvosi    =      r[4]
        
with open( 'Kutyak.csv', 'r', encoding='utf-8-sig' ) as f:
    kutyak_fejlec = f.readline()
    kutyak = [ Kutya( sor ) for sor in f ]

#------------------------------------------------------------
# 6. feladat: Írja ki mennyi a kutyák átlagéletkora (2 tizedesjegy)

átlag = sum( sor.életkor for sor in kutyak ) / len( kutyak )
print( f'6. feladat: Kutyák átlag életkora: {átlag:.2f}')

#------------------------------------------------------------
# 7. feladat: Legidősebb kutya neve és fajtája:

életkor, név_id, fajta_id = max( (kutya.életkor, kutya.név_id, kutya.fajta_id)  for kutya in kutyak )
print( f'7. feladat: Legidősebb kutya neve és fajtája: { kutya_nevek[ név_id ] }, { fajta_nevek[ fajta_id ] }' )

#------------------------------------------------------------
# 8. feladat: Január 10.-én vizsgált kutya fajták és azok száma:
import collections
cnt = collections.Counter()

január10 =  [ sor  for sor in kutyak if sor.orvosi[5:] == '01.10' ]

for kutya in január10:
    cnt[kutya.fajta_id] += 1
    
print(   f'8. feladat: Január 10.-én vizsgált kutya fajták:' )
[ print( f'        { fajta_nevek[fajta_id] }: { darab } kutya') for fajta_id, darab in  cnt.items() ]

#------------------------------------------------------------
#9. feladat: Legjobban leterhelt nap: {}: {} kutya
import collections
cnt = collections.Counter()

for kutya in kutyak:
    cnt[kutya.orvosi] += 1
    
datum, darab = max(cnt.items(), key=lambda x: x[1])

print( f'9. feladat: Legjobban leterhelt nap: {datum}: {darab} kutya')

#------------------------------------------------------------
#10. feladat: névstatisztika.txt néven hozzon létre állományt. A leggyakoribb név legyen elöl
#Szofi;6
import collections
cnt = collections.Counter()

for kutya in kutyak:
    cnt[kutya.név_id] += 1
    
statisztika = sorted( cnt.items(), key=lambda x: x[1], reverse=True )
with open( 'névstatisztika.txt', 'w' ) as f:
    [ print( f'{ kutya_nevek[sor[0]] };{ sor[1] }', file=f ) for sor in statisztika ]



    
