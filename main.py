def print_menu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu toate numerele prime")
    print("3. Determinare cea mai lungă subsecvență cu toate numerele sunt formate din cifre prime")
    print("4. Determinare cea mai lunga subsecventa cu toate numerele pare")
    print("5. Iesire")

def citire_lista():
    '''
    Functia citeste si returneaza o lista
    :return: lista
    '''
    l=[]
    string_citit = input("Dati lista: ")
    numere = string_citit.split(",")
    for x in numere:
        l.append(int(x))
    return l

def is_prime(n):
    '''
    Functia returneaza true daca e prim respectiv false contrar
    :param n: numarul citit
    :return: primalitatea
    '''
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False

def all_primes(l):
    '''
    determina daca toate elementele dintr-o lista sunt prime
    :param l: lista de numere intregi
    :return: True daca toate elementele din l sunt prime, False in caz contrar
    '''
    for x in l:
        if is_prime(x) is False:
            return False
    return True
def test_all_primes():
    assert all_primes([2,3,5]) is True
    assert all_primes([8,8,6]) is False

def get_longest_all_primes(l):
    '''
    Se determina cea mai lunga subsecventa cu numere prime
    :param lst: lista de numere intregi
    :return: se returneaza cea mai lunga subsecventa cu numere prime
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_primes(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_all_primes():
    assert get_longest_all_primes([4,5,6]) == [5]
    assert get_longest_all_primes([2,3,5]) == [2,3,5]
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([8,4,6]) == []
    assert get_longest_all_primes([2, 22, 4, 5, 22, 7, 4, 2, 2]) == [2, 2]


def all_digits_prime(x):
    '''
    Returneaza true daca un numar dat este alcatuit doar din cifre prime, false in caz contrar
    :param x: Un numar dat de la tastatura
    :return: true sau false
    '''
    while x != 0:
        c = x % 10
        if is_prime(c) is False:
            return False
        x = x // 10
    return True

def test_all_digits_prime():
    assert all_digits_prime(123) is False
    assert all_digits_prime(233) is True
    assert all_digits_prime(100) is False

def get_longest_prime_digits(l):
    '''
    Returneaza subsecventa cea mai lunga cu numere alcatuite doar din cifre prime
    :param l: o lista data de la tastatura
    :return: subsecventa cu proprietatea cautata
    '''
    subsecventa_maxima = []
    pozitie_actuala = 0
    lungime = 0
    pozitie_in_l = 0
    lungime_maxima = 0
    pozitie_maxima = 0
    for i in l:
        pozitie_in_l += 1
        if all_digits_prime(i) is True:
            lungime += 1
            if pozitie_actuala == 0:
                pozitie_actuala =pozitie_in_l
        elif lungime > lungime_maxima:
            lungime_maxima = lungime
            pozitie_maxima = pozitie_actuala
            lungime = 0
            pozitie_actuala = 0
    if lungime > lungime_maxima:
            lungime_maxima = lungime
            pozitie_maxima = pozitie_actuala
            lungime = 0
            pozitie_actuala = 0
    for element in range(pozitie_maxima-1,pozitie_maxima+lungime_maxima-1):
        subsecventa_maxima.append(l[element])
    return subsecventa_maxima

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([11, 22, 22, 33, 55, 66, 77]) == [22, 22, 33, 55]
    assert get_longest_prime_digits([11, 12, 13, 15]) == []
    assert get_longest_prime_digits([1, 2, 2, 3, 5, 4, 5]) == [2, 2, 3, 5]

def get_longest_all_even(l):
    '''
    Returneaza cea mai lunga subsecventa cu toate numerele pare
    :param l: lista data de la tastatura
    :return: subsecventa maxima de numere pare
    '''
    subsecventa_maxima = []
    pozitie_actuala = 0
    lungime = 0
    pozitie_in_l = 0
    lungime_maxima = 0
    pozitie_maxima = 0
    for i in l:
        pozitie_in_l += 1
        if i % 2 == 0:
            lungime += 1
            if pozitie_actuala == 0:
                pozitie_actuala = pozitie_in_l
        elif lungime > lungime_maxima:
            lungime_maxima = lungime
            pozitie_maxima = pozitie_actuala
            lungime = 0
            pozitie_actuala = 0
    if lungime > lungime_maxima:
        lungime_maxima = lungime
        pozitie_maxima = pozitie_actuala
        lungime = 0
        pozitie_actuala = 0
    for element in range(pozitie_maxima - 1, pozitie_maxima + lungime_maxima - 1):
        subsecventa_maxima.append(l[element])
    return subsecventa_maxima

def test_get_longest_all_even() :
    assert get_longest_all_even([2, 10, 6, 16, 5, 7, 8]) == [2, 10, 6, 16]
    assert get_longest_all_even([1, 3, 6, 5, 8]) == [6]
    assert get_longest_all_even([7, 5, 3, 9, 1, 11]) == []
    assert get_longest_all_even([4, 4, 4, 5, 6, 6 , 6, 6, 6]) ==[4, 4, 4]

def main():
    test_all_primes()
    test_get_longest_all_primes()
    test_all_digits_prime()
    test_get_longest_prime_digits()
    l = []
    while True:
        print_menu()
        exercitiu = int(input("Dati exercitiul: "))
        if exercitiu == 1:
            l = citire_lista()
        elif exercitiu == 2:
            print(get_longest_all_primes(l))
        elif exercitiu == 3:
            print(get_longest_prime_digits(l))
        elif exercitiu == 4:
            print(get_longest_all_even(l))
        elif exercitiu == 5:
            return 0
        else:
            print("Exercitiu gresit. Incercati un alt exercitiu: ")


main()
