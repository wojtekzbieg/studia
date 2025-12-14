from random import randint


task_id = randint(1000, 9999)

with open("praca_do_wykonania", "a") as file:
    file.write(f"{task_id} - pending\n")