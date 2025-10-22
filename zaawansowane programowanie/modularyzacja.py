import pakiet_testowy
from pakiet_testowy import *
from pakiet_testowy import module1
from pakiet_testowy.module1 import  b
from pakiet_testowy.module1 import potegowanie

print(module1.a)
print(b)
print(potegowanie(3,2))
print(module1.pierwiastkowanie(9,2))

azor = module1.Pies("azor")
print(azor.podaj_imie())
print(module1.Pies.ile_lap())
print(module1.Pies.zaszczekaj())

# print(module2.logarytm_binarny(2))
