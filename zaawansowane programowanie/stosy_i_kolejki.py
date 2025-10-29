class Stos:
    def __init__(self):
        self.stos = []

    def push(self, element):
        self.stos.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.stos.pop()

    def is_empty(self):
        return len(self.stos) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stos[-1]


class Kolejka:
    def __init__(self):
        self.kolejka = []

    def enqueue(self, element):
        self.kolejka.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.kolejka.pop(0)

    def is_empty(self):
        return len(self.kolejka) == 0

    def __len__(self):
        return len(self.kolejka)


class MenadzerHistorii:
    def __init__(self):
        self.stos = Stos()

    def wykonaj_akcje(self, opis):
        self.stos.push(opis)

    def cofnij(self):
        print(self.stos.pop())

    def aktualny_stan(self):
        print(self.stos.peek())


menadzer = MenadzerHistorii ()
menadzer.wykonaj_akcje ( "operacja 1" )
menadzer.wykonaj_akcje ( "operacja 2" )
menadzer.aktualny_stan()
menadzer.cofnij()
menadzer.cofnij()


class SystemZgloszen:
    def __init__(self):
        self.kolejka = Kolejka()

    def dodaj_zgloszenie(self, klient_id):
        self.kolejka.enqueue(klient_id)

    def obsluz_nastepne(self):
        print("Obsługuje: " + str(self.kolejka.dequeue()))

    def liczba_oczekujacych(self):
        print("Liczba oczekujących: " + str(len(self.kolejka)))


system = SystemZgloszen()
system.dodaj_zgloszenie(10)
system.dodaj_zgloszenie(20)
system.liczba_oczekujacych()
system.obsluz_nastepne()
system.obsluz_nastepne()