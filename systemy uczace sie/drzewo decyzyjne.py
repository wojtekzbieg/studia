import math


def wczytaj_plik(plik):
    otwarty_plik = open(plik, "r")
    caly_tekst = otwarty_plik.read()

    linie = [linia for linia in caly_tekst.split("\n") if linia.strip() != ""]

    lista = []
    for linia in linie:
        elementy = linia.split(",")
        lista_tymczasowa = [element.strip() for element in elementy]
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

def oblicz_informacje_atrybutu_warunkowego(dane, index_atrybutu):
    wartosci_atrybutu = set([wiersz[index_atrybutu] for wiersz in dane])

    info = 0
    liczba_wszystkich = len(dane)

    for wartosc in wartosci_atrybutu:
        podzbior = [wiersz for wiersz in dane if wiersz[index_atrybutu] == wartosc]

        decyzje_w_podzbiorze = [wiersz[-1] for wiersz in podzbior]

        unikalne_decyzje = set(decyzje_w_podzbiorze)
        liczebnosci = [decyzje_w_podzbiorze.count(d) for d in unikalne_decyzje]

        waga = len(podzbior) / liczba_wszystkich
        info += waga * oblicz_entropie(liczebnosci)
    # print(f"Info: {info}")
    return info

def oblicz_gain_informacji(dane, index):
    wszystkie_wystapienia = oblicz_liczbe_wystapien_wartosci(dane)
    wystapienia_decyzji = wszystkie_wystapienia[-1]
    startowa_entropia = oblicz_entropie(wystapienia_decyzji)

    gain = startowa_entropia - oblicz_informacje_atrybutu_warunkowego(dane, index)
    # print(f"Gain: {gain}")
    return gain

def oblicz_zrownowazony_gain_informacji(dane, gain, index):
    wszystkie_wystapienia = oblicz_liczbe_wystapien_wartosci(dane)
    split_info = oblicz_entropie(wszystkie_wystapienia, index=index)
    if split_info == 0:
        return 0
    zrownowazony_gain = gain/split_info
    # print(f"Gain Ratio: {zrownowazony_gain}")
    return zrownowazony_gain

def znajdz_najlepszy_atrybut(dane):
    slownik = {}
    for i in range(len(dane[0])-1):
        gain = oblicz_gain_informacji(dane, i)
        slownik[i] = oblicz_zrownowazony_gain_informacji(dane, gain, i)
    najlepszy_atrybut = max(slownik, key=slownik.get)

    if slownik.get(najlepszy_atrybut) > 0:
        return najlepszy_atrybut
    else:
        return None

def wybierz_klase_wiekszosciowa(dane):
    decyzje = [wiersz[-1] for wiersz in dane]
    return max(decyzje, key=decyzje.count)

def buduj_drzewo(dane):
    najlepszy_atrybut = znajdz_najlepszy_atrybut(dane)

    if najlepszy_atrybut is None:
        return wybierz_klase_wiekszosciowa(dane)

    drzewo = {
        "atrybut": najlepszy_atrybut,
        "galaz": {}
    }

    wartosci_atrybutu = set([wiersz[najlepszy_atrybut] for wiersz in dane])

    for wartosc in wartosci_atrybutu:
        podzbior = [wiersz for wiersz in dane if wiersz[najlepszy_atrybut] == wartosc]

        drzewo["galaz"][wartosc] = buduj_drzewo(podzbior)

    return drzewo

def rysuj_drzewo(drzewo, wciecie=0):
    if not isinstance(drzewo, dict):
        print("    " * wciecie + f"==> Decyzja: {drzewo}")
        return

    indeks_atrybutu = drzewo["atrybut"]
    print("    " * wciecie + f"[Wezel: a{indeks_atrybutu + 1}]")

    for wartosc, poddrzewo in drzewo["galaz"].items():
        print("    " * wciecie + f"  -- gdy {wartosc} --> ", end="")

        if not isinstance(poddrzewo, dict):
            print(f"Decyzja: {poddrzewo}")
        else:
            print()
            rysuj_drzewo(poddrzewo, wciecie + 1)

def pokaz_statystyki_korzenia(dane):
    print("--- SZCZEGÓŁOWE OBLICZENIA DLA KORZENIA ---")

    wszystkie_wystapienia = oblicz_liczbe_wystapien_wartosci(dane)
    liczebnosci_decyzji = wszystkie_wystapienia[-1]
    entropia_startowa = oblicz_entropie(liczebnosci_decyzji)

    print(f"Entropia zbioru: {entropia_startowa}")
    print("Gain(X,T) = Entropia zbioru - Info(X,T)\n")

    najlepszy_index = -1
    najlepszy_ratio = -1.0

    liczba_atrybutow = len(dane[0]) - 1

    for i in range(liczba_atrybutow):
        info = oblicz_informacje_atrybutu_warunkowego(dane, i)
        gain = entropia_startowa - info
        ratio = oblicz_zrownowazony_gain_informacji(dane, gain, i)

        print(f"Info(A{i+1},T) = {info}")
        print(f"Gain(A{i+1},T) = {gain}")
        print(f"GainRatio(A{i+1},T) = {ratio}")

        if ratio > najlepszy_ratio:
            najlepszy_ratio = ratio
            najlepszy_index = i

    print(f"\nWybrany atrybut A{najlepszy_index+1}, bo w tym przypadku najwyższa jest wartość GainRatio: {najlepszy_ratio}")
    print("---------------------------------------------")



lista_z_plikiem = wczytaj_plik("breast-cancer_klasa_na_koncu.data")

# lista_wystapien_wartosci = oblicz_liczbe_wystapien_wartosci(lista_z_plikiem)
#
# znajdz_najlepszy_atrybut(lista_z_plikiem)


pokaz_statystyki_korzenia(lista_z_plikiem)

drzewo_wynikowe = buduj_drzewo(lista_z_plikiem)

rysuj_drzewo(drzewo_wynikowe)