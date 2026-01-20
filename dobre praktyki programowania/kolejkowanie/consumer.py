import time


def wykonanie_pracy(id):
    print(f"rozpoczynam wykonywanie zadania numer {id}")
    time.sleep(10)
    print(f"zadanie {id} wykonane")


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
                lista_linii[indeks] = linia.replace("pending", "in progress")
                task_index = indeks
                task_id = linia.strip().split(" ")[0]
                break
            else:
                task_index = -1

    if task_index != -1:
        with open("praca_do_wykonania", "w") as file:
            file.writelines(lista_linii)

        wykonanie_pracy(task_id)

        with open("praca_do_wykonania", "r") as file:
            lista_linii = file.readlines()
            lista_linii[task_index] = lista_linii[task_index].replace("in progress", "done")
        with open("praca_do_wykonania", "w") as file:
            file.writelines(lista_linii)

    else:
        time.sleep(5)
        print("Czekam na zadania!")


# with open("praca_do_wykonania", "r") as file:
#     print(file.read())

