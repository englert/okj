#név;első;utolsó;súly;magasság
# 0    1    2     3      4
#Jim Abbott;1989-04-08;1999-07-21;200;75

with open('balkezesek.csv', 'r', encoding='latin2') as forras:
    forras.readline()
    matrix = [sor.strip().split(';') for sor in forras ]
    
print(f"3.Feladat: {len(matrix)}")

print(f"4.Feladat:")
[print(f"       {sor[0]}, {int(sor[4])*2.54:.2f} cm")for sor in matrix if sor[2][:7] == '1999-10']

print(f"5.Feladat:")

evszam = int(input('Kérek egy évszámot:'))
if 1990 <= evszam <= 1999:
    pass
else:
    while True:
        evszam = int(input('Hibás adat! Kérek egy 1990 és 1999 közötti évszámot:'))
        if 1990<=evszam<=1999:
            break
sulyok = [int(sor[3]) for sor in matrix if sor[1][:4] <=str(evszam)<=
          sor[2][:4]]
atlag = sum(sulyok)/ len(sulyok)
print(f"6.Feladat: {atlag:.2f} font")
