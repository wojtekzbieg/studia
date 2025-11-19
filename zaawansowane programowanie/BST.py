class Wezel:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewy = None
        self.prawy = None


class BSTree:
    def __init__(self):
        self.root = None

    def wstaw_iteracyjnie(self, liczba):
        nowy_wezel = Wezel(liczba)

        if self.root is None:
            self.root = nowy_wezel
            return

        aktualny_wezel = self.root
        poprzedni_wezel = None

        while aktualny_wezel is not None:
            poprzedni_wezel = aktualny_wezel

            if liczba < aktualny_wezel.wartosc:
                aktualny_wezel = aktualny_wezel.lewy
            else:
                aktualny_wezel = aktualny_wezel.prawy

        if liczba < poprzedni_wezel.wartosc:
            poprzedni_wezel.lewy = nowy_wezel
        else:
            poprzedni_wezel.prawy = nowy_wezel

    def wstaw_rekurencyjnie(self, liczba):
        def rekurencja(wezel, liczba):
            if wezel is None:
                return Wezel(liczba)

            if liczba < wezel.wartosc:
                wezel.lewy = rekurencja(wezel.lewy, liczba)
            elif liczba > wezel.wartosc:
                wezel.prawy = rekurencja(wezel.prawy, liczba)

            return wezel

        self.root = rekurencja(self.root, liczba)

    def usun(self, liczba):
        def rekurencja(wezel, liczba):
            if wezel is None:
                return None

            if liczba < wezel.wartosc:
                wezel.lewy = rekurencja(wezel.lewy, liczba)
            elif liczba > wezel.wartosc:
                wezel.prawy = rekurencja(wezel.prawy, liczba)
            else:
                if wezel.lewy is None and wezel.prawy is None:
                    return None

                elif wezel.lewy is None:
                    return wezel.prawy
                elif wezel.prawy is None:
                    return wezel.lewy

                else:
                    nastepny_wezel = wezel.prawy
                    while nastepny_wezel.lewy:
                        nastepny_wezel = nastepny_wezel.lewy

                    wezel.wartosc = nastepny_wezel.wartosc
                    wezel.prawy = rekurencja(wezel.prawy, nastepny_wezel.wartosc)

            return wezel

        self.root = rekurencja(self.root, liczba)

    def wypisz_VLR(self):
        def rekurencja(wezel):
            if wezel:
                print(wezel.wartosc, end=" ")
                rekurencja(wezel.lewy)
                rekurencja(wezel.prawy)
        rekurencja(self.root)

    def wypisz_LVR(self):
        def rekurencja(wezel):
            if wezel:
                rekurencja(wezel.lewy)
                print(wezel.wartosc, end=" ")
                rekurencja(wezel.prawy)
        rekurencja(self.root)

    def wypisz_LRV(self):
        def rekurencja(wezel):
            if wezel:
                rekurencja(wezel.lewy)
                rekurencja(wezel.prawy)
                print(wezel.wartosc, end=" ")
        rekurencja(self.root)
