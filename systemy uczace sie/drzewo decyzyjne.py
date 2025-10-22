import math


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
        # print(lista2)
        lista_wystapien = []
        for wartosc in wartosci:
            liczba_wystapien = lista2.count(wartosc)
            # print(f"Wartosc atrybutu: {wartosc}, liczba wystapien: {liczba_wystapien}")
            lista3= [wartosc, liczba_wystapien]
            # print(lista3)
            lista_wystapien.append(lista3)
        zbior2[j] = lista_wystapien
    return zbior2

def oblicz_entropie(lista_wystapien_wartosci):
    lista_wystapien_wartosci = lista_wystapien_wartosci.get(len(lista_wystapien_wartosci)-1)
    # print(lista_wystapien_wartosci)

    suma = 0
    suma2 = 0
    lista_wartosci = []

    for i in lista_wystapien_wartosci:
        suma += i[-1]
        lista_wartosci.append(i[-1])
    lista_prawdopodobienstw = [i/suma for i in lista_wartosci]
    # print(lista_prawdopodobienstw)

    for i in lista_prawdopodobienstw:
        suma2 += i * math.log2(i)
    suma2 = suma2*(-1)
    return suma2


lista_z_plikiem = wczytaj_plik("gieldaLiczby.txt")

liczba_wartosci = oblicz_liczbe_wartosci(lista_z_plikiem)
liczba_wystapien_wartosci = oblicz_liczbe_wystapien_wartosci(lista_z_plikiem)

# print(liczba_wartosci)
# print(liczba_wystapien_wartosci)







entropia = oblicz_entropie(liczba_wystapien_wartosci)
print(entropia)

