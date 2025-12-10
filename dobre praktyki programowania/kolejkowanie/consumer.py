import time


def wykonanie_pracy():
    print("rozpoczynam wykonywanie pracy")
    time.sleep(10)
    print("praca wykonana")


while True:
    with open("praca_do_wykonania", "r") as file:
        pierwsza_linia = file.readline()
        if not pierwsza_linia:
            print("pusty")
            time.sleep(5)
            continue

    with open("praca_do_wykonania", "r") as file:
        lista_linii = file.readlines()
        for indeks, linia in enumerate(lista_linii):
            if "pending" in linia:
                lista_linii[indeks] = linia.replace("pending", "in_progress")
