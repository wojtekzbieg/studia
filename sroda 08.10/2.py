import pytest


def palindrome(slowo):
    slowo = slowo.replace(" ", "").lower()
    odwrocone=slowo[::-1]

    if odwrocone == slowo:
        return True
    else:
        return False

# def test_palindrome():
#     assert palindrome("kajak") == True
#     assert palindrome("Kobyła ma mały bok") == True
#     assert palindrome("python") == False
#     assert palindrome("") == True
#     assert palindrome("A") == True



def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    elif n < 0:
        raise ValueError

    return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    with pytest.raises(ValueError):
        fibonacci(-1)



# def count_vowels(slowo):
#     slowo = slowo.lower()
#     return slowo.count("a") + slowo.count("e") + slowo.count("i") + slowo.count("o") + slowo.count("u") + slowo.count("y")
#
# def test_count_vowels():
#     assert count_vowels("Python") == 2
#     assert count_vowels("AEIOUY") == 6
#     assert count_vowels("bcd") == 0
#     assert count_vowels("") == 0
#     assert count_vowels("Próba żółwia") == 3



def calculate_discount(price, discount):
    if 0 > discount or discount > 1:
        raise ValueError("Wystąpił błąd")
    return price * (1 - discount)

# def test_calculate_discount():
#     assert calculate_discount(100,0.2) == 80.0
#     assert calculate_discount(50,0) == 50.0
#     assert calculate_discount(200,1) == 0.0
#     with pytest.raises(ValueError):
#         calculate_discount(100, -0.1)
#     with pytest.raises(ValueError):
#         calculate_discount(100, 1.5)



# def flatten_list(lista):
#     pusta_lista=[]
#     for i in lista:
#         if isinstance(i, list):
#             pusta_lista.extend(flatten_list(i))
#         else:
#             pusta_lista.append(i)
#     return pusta_lista
#
# def test_flatten_list():
#     assert flatten_list([1,2,3]) == [1,2,3]
#     assert flatten_list([1, [2, 3], [4, [5]]]) == [1,2,3,4,5]
#     assert flatten_list([]) == []
#     assert flatten_list([[[1]]]) == [1]
#     assert flatten_list([1, [2, [3, [4]]]]) == [1,2,3,4]


# def word_frequencies(tekst: str):
#     znaki = [",", ".", ":", ";", "!", "?"]
#
#     for i in znaki:
#         tekst = tekst.replace(i, "")
#
#     tekst = tekst.lower()
#     lista = tekst.split()
#
#     slownik = {}
#
#     for i in lista:
#         if i in slownik:
#             slownik[i] += 1
#         else:
#             slownik[i] = 1
#
#     return slownik
#
#
# def test_word_frequencies():
#     assert word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}
#     assert word_frequencies("Hello, hello!") == {"hello": 2}
#     assert word_frequencies("") == {}
#     assert word_frequencies("Python Python python") == {"python": 3}
#     assert word_frequencies("Ala ma kota, a kot ma Ale.") == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}

def is_prime(liczba):
    if liczba < 2:
        return False

    pierwiastek = liczba ** (1/2)
    pierwiastek //= 1
    lista=[]

    for i in range(2, int(pierwiastek)+1):
        if liczba % i == 0:
            lista.append(i)
        if len(lista) > 0:
            return False

    return True

# def test_is_prime():
#     assert is_prime(2) == True
#     assert is_prime(3) == True
#     assert is_prime(4) == False
#     assert is_prime(0) == False
#     assert is_prime(1) == False
#     assert is_prime(5) == True
#     assert is_prime(97) == True



