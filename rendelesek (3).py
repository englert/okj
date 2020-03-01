# rendeles.csv
with open( 'rendeles.csv', 'r', encoding='latin2' ) as f:                   # megnyitjuk a rendeles.csv-t mint f
    rendeles_matrix = [ sor.strip().split(';') for sor in f ]               # feltöltjük a rendeles_matrixot a rendeles.csv soraival
                                                                            # a sorokbol a strip()-el eltávolítjuk a \n sorvég jeleket
                                                                            # a sorokat split(';') segítségével listává szeleteljük
                                                                            # a [ sor for sor in f] egy  Python List Comprehension,
                                                                            #  magától felépít egy új listát,
                                                                            # kiértékelve a megadott lista összes elemére a kifejezést.
    
with open( 'raktar.csv', 'r', encoding='latin2' ) as f:                     # megnyitjuk a raktar.csv-t mint f
    raktar_matrix = [ sor.strip().split(';') for sor in f ]                 # feltöltjük az raktar_matrixot a raktar.csv soraival
                                                                 
#raktar.csv:    # termék_kod, termék_nev, termek_ar,  raktar_keszlet
                #     0            1          2             3
raktar_keszlet = { sor[0]      : int(sor[3])  for sor in raktar_matrix }    # létrehozzuk a raktar_keszlet szótárt a raktar_matrixból
                                                                            # kulcs = termek_kod, érték = raktar_keszlet 
                                                                                
termek_ar      = { sor[0]      : int(sor[2])  for sor in raktar_matrix }    # létrehozzuk a termek_ar szótárt a raktar_matrixból
                                                                            # kulcs = termek_kod, érték = termek_ar                                                                           
#rendeles.csv   # sor típus,  rendelés dátuma,   rendeles száma,     email
#                     0             1                   2              3

rendelesek   = { int(sor[2]) : sor[3] for sor in rendeles_matrix if sor[0] =='M'}    # létrehozzuk a rendelesek szótárt a rendeles_matrix-ból
                                                                                     # kulcs = rendeles_szam, érték = email
                                                                                     
rendelesi_tetelek = { int(sor[2]) : [] for sor in rendeles_matrix if sor[0] == 'M' } # létrehozzuk a rendelesi_tetelek szótárt a rendeles_matrix-ból
                                                                                     # kulcs = rendeles_szam, érték = üres lista a leendő rendelési tételeknek
# rendeles.csv ha a sortípus 'T'
# sortipus, rendeles_szam, termek_kod, rendelt_mennyiseg
#    0         1               2                3

for sor in rendeles_matrix:                                                          # végigmegyünk a rendeles_matrix-on soronként
    sor_tipus = sor[0]
    if sor_tipus == 'T':                                                             # ha a sor típus 'T' akkor
        rendeles_szama     = int(sor[1])                                    
        termek_kod = sor[2]
        rendelt_mennyiseg  = int(sor[3])
        rendelesi_tetelek[ rendeles_szama ].append([termek_kod, rendelt_mennyiseg])  # A rendelési tételt hozzáfűzzük a megfelelő rendeléshez, a rendeles_szam alapján.

levelek_csv   = open('levelek.csv','w') # --------------------megnyitjuk a levelek.csv fájlt írásra -----------------------------
teljesitetlen_rendeles = dict()                               # létrehozzuk az üres teljesitetlen_rendeles szótárt

for rendeles_szama, tetelek in rendelesi_tetelek.items():     # Végigmegyünk a rendelesi_tetelek-en és ciklusonként megkapjuk:
                                                              #      a rendeles_szama-t és az adott rendeléshez tartozo teteleket 
    rendeles_teljesitheto = True                              # a rendeles_teljesítheto-t True ra állítjuk
    
    for termek_kod, rendelt_mennyiseg in tetelek:             # végigmegyünk az adott rendeles tételein
        
        if raktar_keszlet[ termek_kod ] < rendelt_mennyiseg:  # ha a raktárban kevesebb áru van mint a rendelés, akkor
            rendeles_teljesitheto = False                     # a rendeles_teljesitheto-t False-ra állítjuk
            
            if termek_kod in teljesitetlen_rendeles:          # ha a termék már benne van a teljesitetlen_rendeles szótárban, akkor
                teljesitetlen_rendeles[ termek_kod ] = teljesitetlen_rendeles[ termek_kod ] + rendelt_mennyiseg     #  módosítjuk a rendelt mennyiség értékét
            else:                                             # egyébként felvesszük a teljesitetlen_rendeles szótárba a termek_kod-ot és a hozzá tartozó rendelt mennyiséget
                teljesitetlen_rendeles[ termek_kod ] = rendelt_mennyiseg 
    
    #Ha a rendelés nem teljesíthető akkor ez a kódrészlet nem kerül végrehajtásra
    if rendeles_teljesitheto:                                                              # Ha a rendelés teljesíthető akkor
        rendeles_erteke = 0                                                                # a rendeles_erteke jelenleg 0
        
        for termek_kod, rendelt_mennyiseg in tetelek:                                      # végigmegyünk az adott rendeles tételein
            raktar_keszlet[ termek_kod ] -= rendelt_mennyiseg                              # a raktár_keszlet-et csökkentjük a rendelt mennyiséggel
            rendeles_erteke              += termek_ar[ termek_kod ] * rendelt_mennyiseg    # a rendelés értékét növeljük az aktuális tételdarab értékével
            
        email  = rendelesek[ rendeles_szama ]                                              # kiírjuk a sikeres teljesítésről szóló üzenetet.
        print(f'{email};A rendelését két napon belül szállítjuk. A rendelés értéke: {rendeles_erteke} Ft ', file = levelek_csv)
    
    else:                                                                                  # ha a rendelés nem teljesíthető, akkor értesítést adunk a függő állapotról
        email  = rendelesek[ rendeles_szama ] 
        print(f'{email};A rendelése függő állapotba került. Hamarosan értesítjük a szállítás időpontjáról.', file = levelek_csv)    

levelek_csv.close()                   # ------------------------------------------------- lezárjuk a  levelek.csv fájlt -------------------

with open('beszerzes.csv','w') as beszerzes_csv:                                          # megnyitjuk a beszerzes.csv fájlt írásra 
    for termek_kod, rendelt_mennyiseg in sorted(teljesitetlen_rendeles.items()):          # végigmegyünk a teljesitetlen_rendelesek szótáron
                                                                                          # minden ciklusban kapunk egy termek_kod-ot és egy rendelt_mennyiseg-et
                                                                                          # a rendelt_mennyiseg-et csökkentve a raktar_keszlet-el kiírhatjuk a fájlt
        print( f'{ termek_kod };{ rendelt_mennyiseg - raktar_keszlet[ termek_kod ] }', 'file = beszerzes_csv')
    
        
        
    
    
    
    