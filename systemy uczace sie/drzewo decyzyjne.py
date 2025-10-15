otwarty_plik = open("gieldaLiczby.txt", "r")
caly_tekst = otwarty_plik.read()

if caly_tekst[-1] == "\n":
    caly_tekst = caly_tekst[0:-1]

caly_tekst = caly_tekst.replace(",", "").split("\n")

lista=[]

for j in range(0, len(caly_tekst)):
    lista_tymczasowa = []
    for i in range(0, len(caly_tekst[j])):
        lista_tymczasowa.append(int(caly_tekst[j][i]))
    lista.append(lista_tymczasowa)

print(lista)

for j in range(len(lista[0])):
    lista2=[]
    for i in range(len(lista)):
        lista2.append(lista[i][j])
    wartosci = set(lista2)
    print(f"Atrybut na pozycji {j} - {len(wartosci)} mozliwe wartosci")

    for k in wartosci:
        liczba_wystapien = lista2.count(k)
        print(f"Wartosc atrybutu: {k}, liczba wystapien: {liczba_wystapien}")

    print()

