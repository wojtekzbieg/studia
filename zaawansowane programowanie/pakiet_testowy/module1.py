a = 10
b = 20

def potegowanie(x,y):
    return x ** y

def pierwiastkowanie(x,y):
    return x ** (1/y)

class Pies:
    liczba_lap = 4

    def __init__(self, imie):
        self.imie = imie

    def podaj_imie(self):
        return self.imie

    @classmethod
    def ile_lap(cls):
        return cls.liczba_lap

    @staticmethod
    def zaszczekaj():
        return "hał hał"