def wczytaj_plik(plik):
    otwarty_plik = open(plik, "r")
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

    return lista

def oblicz_liczbe_wartosci(lista):
    zbior1 = {}
    for j in range(len(lista[0])):
        lista2=[]
        for i in range(len(lista)):
            lista2.append(lista[i][j])
        wartosci = set(lista2)
        # print(f"Atrybut na pozycji {j} - {len(wartosci)} mozliwe wartosci")
        zbior1[j]= len(wartosci)
    return zbior1

def oblicz_liczbe_wystapien_wartosci(lista):
    zbior2 = {}
    for j in range(len(lista[0])):
        lista2 = []
        for i in range(len(lista)):
            lista2.append(lista[i][j])
        wartosci = set(lista2)

        lista_wystapien = []
        for k in wartosci:
            liczba_wystapien = lista2.count(k)
            # print(f"Wartosc atrybutu: {k}, liczba wystapien: {liczba_wystapien}")
            zbior3= {k: liczba_wystapien}
            print(zbior3)
            lista_wystapien.append(zbior3)
        zbior2[j] = lista_wystapien
    return zbior2


lista_z_plikiem = wczytaj_plik("gieldaLiczby.txt")

liczba_wartosci = oblicz_liczbe_wartosci(lista_z_plikiem)
liczba_wystapien_wartosci = oblicz_liczbe_wystapien_wartosci(lista_z_plikiem)

# print(liczba_wartosci)
# print(liczba_wystapien_wartosci)


# liczba_wystapien_wartosci = liczba_wystapien_wartosci.get(len(liczba_wystapien_wartosci)-1)
# print(liczba_wystapien_wartosci[0].get)






