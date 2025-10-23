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
    zbior2 = []
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
            # lista3= [liczba_wystapien]
            # print(lista3)
            lista_wystapien.append(liczba_wystapien)
        zbior2.append(lista_wystapien)

    return zbior2

def oblicz_entropie(lista_wystapien_wartosci, index = None):
    if index is not None:
        lista_wystapien_wartosci = lista_wystapien_wartosci[index]
    # print(lista_wystapien_wartosci)

    suma = 0
    suma2 = 0
    lista_wartosci = []

    for i in lista_wystapien_wartosci:
        suma += i
        lista_wartosci.append(i)
    lista_prawdopodobienstw = [i/suma for i in lista_wartosci]
    # print(lista_prawdopodobienstw)

    for i in lista_prawdopodobienstw:
        if i == 0:
            continue
        suma2 += i * math.log2(i)
    suma2 = suma2*(-1)
    return suma2

def oblicz_entropie_klas_decyzyjnych(lista, index):
    nowa_lista = []
    lista_wartosci1 = []
    for i in range(len(lista)):
        lista_tymczasowa = [lista[i][index], lista[i][-1]]
        nowa_lista.append(lista_tymczasowa)
        lista_wartosci1.append(lista_tymczasowa[0])

    lista_wartosci1 = set(lista_wartosci1)
    lista1 = [[0, 0] for _ in range(len(lista_wartosci1))]
    # print(lista1)
    for i in range(len(nowa_lista)):
        k = 0
        for j in lista_wartosci1:
            if nowa_lista[i][0] == j:
                if nowa_lista[i][1] == 0:
                    lista1[k][0] += 1
                elif nowa_lista[i][1] == 1:
                    lista1[k][1] += 1
            k += 1

    # print(lista1)

    lista_wartosci2 = []
    for i in range(len(lista1)):
        lista_wartosci2.append(oblicz_entropie(lista1, index=i))

    suma = 0
    for i in lista1:
        for j in i:
            suma += j

    liczniki = []
    suma_tymczasowa = 0
    for i in lista1:
        for j in i:
            suma_tymczasowa += j
        liczniki.append(suma_tymczasowa)
        suma_tymczasowa=0
    # print(liczniki)

    funkcja_informacji = 0
    for i in range(len(liczniki)):
        funkcja_informacji += (liczniki[i] / suma) * lista_wartosci2[i]

    return funkcja_informacji

def oblicz_gain_informacji(entropia, index):
    return entropia - oblicz_entropie_klas_decyzyjnych(lista_z_plikiem, index)

lista_z_plikiem = wczytaj_plik("gieldaLiczby.txt")

liczba_wartosci = oblicz_liczbe_wartosci(lista_z_plikiem)
liczba_wystapien_wartosci = oblicz_liczbe_wystapien_wartosci(lista_z_plikiem)

# print(lista_z_plikiem)
# # print(liczba_wartosci)
# print("--------------")
# print(liczba_wystapien_wartosci)


entropia = oblicz_entropie(liczba_wystapien_wartosci, 3)
# print(entropia)




# liczba_wystapien_wartosci = liczba_wystapien_wartosci.get(0)
# print(liczba_wystapien_wartosci)
#
# lista_wartosci = []
# suma = 0
# for i in liczba_wystapien_wartosci:
#     suma += i[-1]
#     lista_wartosci.append(i[-1])
#
# lista_prawdopodobienstw = [i/suma for i in lista_wartosci]
# print(lista_prawdopodobienstw)


print(oblicz_entropie_klas_decyzyjnych(lista_z_plikiem, 0))
# print(oblicz_liczbe_wystapien_wartosci(oblicz_entropie_klas_decyzyjnych(lista_z_plikiem)))

print(oblicz_gain_informacji(entropia, 2))