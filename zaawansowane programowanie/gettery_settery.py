class Zwierze:
    def __init__(self, imie):
        self._imie = imie

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, wartosc):
        if not wartosc:
            raise ValueError("Imię nie może być puste")
        self._imie = wartosc

    def przedstaw_sie(self):
        print(f"Jestem {self._imie}")




# Zadanie 1

class Kot(Zwierze):
    def __init__(self, imie, ulubione_jedzenie):
        super().__init__(imie)
        self._ulubione_jedzenie = ulubione_jedzenie

    @property
    def ulubione_jedzenie(self):
        return self._ulubione_jedzenie

    @ulubione_jedzenie.setter
    def ulubione_jedzenie(self, nowe_ulubione_jedzenie):
        if nowe_ulubione_jedzenie:
            self._ulubione_jedzenie = nowe_ulubione_jedzenie
        else:
            raise ValueError("To pole nie może być puste")

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, moje ulubione jedzenie to {self.ulubione_jedzenie}")

kot1 = Kot("Puszek", "karma dla kotów")
kot1.przedstaw_sie()





# Zadanie 2

class Pies(Zwierze):
    def __init__(self, imie, rasa, czy_szczeka_czesto, wiek, kolor_siersci):
        super().__init__(imie)
        self._rasa = rasa
        self._czy_szczeka_czesto = czy_szczeka_czesto
        self._wiek = wiek
        self._kolor_siersci = kolor_siersci

    @property
    def rasa(self):
        return self._rasa

    @rasa.setter
    def rasa(self, wartosc):
        if not wartosc:
            raise ValueError("Rasa nie może być pusta")
        self._rasa = wartosc

    @property
    def czy_szczeka_czesto(self):
        return self._czy_szczeka_czesto

    @czy_szczeka_czesto.setter
    def czy_szczeka_czesto(self, wartosc):
        if not isinstance(wartosc, bool):
            raise ValueError("Wartość dla 'czy szczeka często' musi być typu boolean (True/False)")
        self._czy_szczeka_czesto = wartosc

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        if (not isinstance(nowy_wiek, int)) or (nowy_wiek < 0):
            raise ValueError("Wiek musi być liczbą całkowitą większą bądź równą zero")
        self._wiek = nowy_wiek

    @property
    def kolor_siersci(self):
        return self._kolor_siersci

    @kolor_siersci.setter
    def kolor_siersci(self, nowy_kolor_siersci):
        if nowy_kolor_siersci:
            self._kolor_siersci = nowy_kolor_siersci
        else:
            raise ValueError("Podaj kolor siersci")

    def przedstaw_sie(self):
        szczeka_info = "szczekam często" if self.czy_szczeka_czesto else "nie szczekam często"
        print(f"Jestem {self.imie}, a moja rasa to {self.rasa}, i {szczeka_info}. Mam {self.wiek} lat, "
                f"kolor mojej sierści to {self.kolor_siersci}")


pies1 = Pies("Azor", "Owczarek Niemiecki", True, 5, "brązowy")
pies1.przedstaw_sie()