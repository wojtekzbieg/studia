class WezelJednokierunkowy:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaJednokierunkowa:
    def __init__(self):
        self.head = None

    def dodaj_na_poczatku(self, data):
        nowy_wezel = WezelJednokierunkowy(data)

        if self.head is None:
            self.head = nowy_wezel
            return

        nowy_wezel.next = self.head
        self.head = nowy_wezel

    def dodaj_na_koncu(self, data):
        nowy_wezel = WezelJednokierunkowy(data)

        if self.head is None:
            self.head = nowy_wezel
            return

        aktualny_wezel = self.head

        while aktualny_wezel.next is not None:
            aktualny_wezel = aktualny_wezel.next

        aktualny_wezel.next = nowy_wezel


    def dodaj_w_wybranym_miejscu(self, data, index):
        nowy_wezel = WezelJednokierunkowy(data)

        aktualny_wezel = self.head
        licznik = 0

        while licznik != index-1:
            aktualny_wezel = aktualny_wezel.next
            licznik += 1

        nowy_wezel.next = aktualny_wezel.next
        aktualny_wezel.next = nowy_wezel



    def usun_na_poczatku(self):
        if self.head is None:
            print("lista jest pusta")

        aktualny_wezel = self.head
        self.head = self.head.next
        aktualny_wezel.next = None

    def usun_w_wybranym_miejscu(self, index):
        licznik = 0
        aktualny_wezel = self.head

        while licznik != index-1:
            aktualny_wezel = aktualny_wezel.next
            licznik += 1

        aktualny_wezel.next = aktualny_wezel.next.next


    def usun_na_koncu(self):
        if self.head is None:
            print("lista jest pusta")

        aktualny_wezel = self.head

        while aktualny_wezel.next.next is not None:
            aktualny_wezel = aktualny_wezel.next

        aktualny_wezel.next = None

    def wyswietl_od_poczatku(self):
        aktualny_wezel = self.head

        while aktualny_wezel is not None:
            print(aktualny_wezel.data)
            aktualny_wezel = aktualny_wezel.next




class WezelDwukierunkowy:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class ListaDwukierunkowa:
    def __init__(self):
        self.head = None


    def dodaj_na_poczatku(self, data):
        nowy_wezel = WezelDwukierunkowy(data)

        if self.head is None:
            self.head = nowy_wezel
            return

        nowy_wezel.next = self.head
        self.head.previous = nowy_wezel
        self.head = nowy_wezel


    def dodaj_na_koncu(self, data):
        nowy_wezel = WezelDwukierunkowy(data)

        if self.head is None:
            self.head = nowy_wezel
            return

        aktualny_wezel = self.head

        while aktualny_wezel.next is not None:
            aktualny_wezel = aktualny_wezel.next

        aktualny_wezel.next = nowy_wezel
        nowy_wezel.previous = aktualny_wezel


    def dodaj_w_wybranym_miejscu(self, data, index):
        nowy_wezel = WezelDwukierunkowy(data)

        aktualny_wezel = self.head
        licznik = 0

        while licznik != index-1:
            aktualny_wezel = aktualny_wezel.next
            licznik += 1

        nowy_wezel.next = aktualny_wezel.next
        aktualny_wezel.next = nowy_wezel

        nowy_wezel.previous = aktualny_wezel
        if nowy_wezel.next is not None:
            nowy_wezel.next.previous = nowy_wezel


    def usun_na_poczatku(self):
        if self.head is None:
            print("lista jest pusta")

        aktualny_wezel = self.head
        self.head = self.head.next
        aktualny_wezel.next = None
        self.head.previous = None


    def usun_w_wybranym_miejscu(self, index):
        licznik = 0
        aktualny_wezel = self.head

        while licznik != index:
            aktualny_wezel = aktualny_wezel.next
            licznik += 1

        aktualny_wezel.previous.next = aktualny_wezel.next
        aktualny_wezel.next.previous = aktualny_wezel.previous
        aktualny_wezel.next = None
        aktualny_wezel.previous = None


    def usun_na_koncu(self):
        if self.head is None:
            print("lista jest pusta")

        aktualny_wezel = self.head

        while aktualny_wezel.next.next is not None:
            aktualny_wezel = aktualny_wezel.next

        aktualny_wezel.next.previous = None
        aktualny_wezel.next = None


    def wyswietl_od_poczatku(self):
        aktualny_wezel = self.head

        while aktualny_wezel is not None:
            print(aktualny_wezel.data)
            aktualny_wezel = aktualny_wezel.next


    def wyswietl_od_konca(self):
        aktualny_wezel = self.head

        while aktualny_wezel.next is not None:
            aktualny_wezel = aktualny_wezel.next

        while aktualny_wezel is not None:
            print(aktualny_wezel.data)
            aktualny_wezel = aktualny_wezel.previous




lista1 = ListaJednokierunkowa()

lista1.dodaj_na_poczatku(4)
lista1.dodaj_na_poczatku(2)
lista1.dodaj_na_poczatku(1)
lista1.dodaj_w_wybranym_miejscu(3,2)
lista1.dodaj_na_koncu(5)

lista1.usun_na_koncu()
lista1.usun_na_poczatku()
lista1.usun_w_wybranym_miejscu(1)




lista2 = ListaDwukierunkowa()

lista2.dodaj_na_poczatku(1)
lista2.dodaj_na_koncu(4)
lista2.dodaj_w_wybranym_miejscu(2, 1)
lista2.dodaj_w_wybranym_miejscu(3, 2)

lista2.usun_na_poczatku()
lista2.usun_na_koncu()
lista2.dodaj_w_wybranym_miejscu(4,2)
lista2.usun_w_wybranym_miejscu(1)

lista2.wyswietl_od_poczatku()
print("___________")
lista2.wyswietl_od_konca()
