def printMenu():
    print("1. citire lista")
    print("2. cea mai lunga subsecventa in care toate numerele sunt ordonate crescator")
    print("3. cea mai lunga subsecventa in care toate numerele au partea intreaga egala cu partea fractionara")
    print("4. cea mai lunga subsecventa in care toate numerele sunt prime")
    print("5. iesire")

def citire_termeni():
    list = []
    n = int(input(" dati numarul de termeni din lista, n = "))
    for i in range(n):
        list.append(int(input("list[ " + str(i) + " ] = ")))
    return list

#problema 4

def ordinecrescatoare(lst: list[int]):
    '''
    
    :param lst: o lista de numere intregi
    :return: True, daca elementele sunt ordonate crescator sau False, daca nu sunt
    
    '''

    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1] :
            return False
    return True

def test_ordinecrescatoare():
    assert ordinecrescatoare([3, 8, 9]) is True
    assert ordinecrescatoare([1, 2, 3]) is True
    assert ordinecrescatoare([3, 4, 5, 7]) is True
    assert ordinecrescatoare([8, 5, 9, 3]) is False


def get_longest_sorted_asc(lst: list[int]):
    '''
    
    :param lst: o lista de numere intregi
    :return: cea mai lunga secvente de numere ordonate crescator
    
    '''

    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if ordinecrescatoare(lst[i:j + 1]) is True and (len(lst[i:j + 1]) > len(subsecventaMax)):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 5, 6, 1, 3, 4, 5]) == [1, 3, 4, 5]
    assert get_longest_sorted_asc([1, 2, 3, 1, 0, 5, 6, 7]) == [0, 5, 6, 7]

#problema 14

def verificaree(n: float):
    '''

    :param n: un numar real
    :return: True daca un numar are partea intreaga egala cu partea fractionara, iar False in caz contrar

    '''
    m1= int(n)
    p=1
    while ( n - int(n) ) > 0:
        n = n * 10
        p = p * 10
    m2 = n % p
    if m1 == m2:
        return True
    else:
        return False

def test_verificaree():
    assert verificaree(23.24) is False
    assert verificaree(23.23) is True


def get_longest_equal_int_real(lst: list[float]):
    '''

    :param lst: o lista de numere reale
    :return: subsecventa cea mai lunga in care toate numerele au partea intreaga egala cu cea fractionara
    '''
    subsecventa_maxima = []
    len_subsecventa_curenta = 0
    len_subsecventa_maxima = 0
    verificare = 0

    for i in range(len(lst)):
        if verificaree(lst[i]):
            verificare = 1
            len_subsecventa_curenta = len_subsecventa_curenta + 1

        elif len_subsecventa_maxima < len_subsecventa_curenta:
            indice_final = i - 1
            indice_inceput = i - len_subsecventa_curenta
            len_subsecventa_maxima = len_subsecventa_curenta
            len_subsecventa_curenta = 0

    if len_subsecventa_maxima < len_subsecventa_curenta:
        indice_final = i
        indice_inceput = i - len_subsecventa_curenta + 1

    if verificare == 1:
        for i in range(indice_inceput, indice_final + 1):
            subsecventa_maxima.append(lst[i])
    else:
        return "Nu exista o asemenea subsecventa "
    return subsecventa_maxima



def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([345.345, 23.23, 56.34, 65.65]) == [345.345, 23.23]
    assert get_longest_equal_int_real([24.23, 65.65, 743.743, 892.892, 4165.4165, 76.87, 34.34]) == [65.65, 743.743, 892.892, 4165.4165]


#problema 2

def isPrime(n :int):
    '''
    
    :param n: Un numar intreg
    :return: True daca un numar este prim, respectiv False in caz contrar
    
    '''

    if n<2:
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            return False

    return True



def isPrimelst(lst: list[int]):
    for num in lst:
        if not isPrime(num):
            return False
    return True

def test_isPrimelst():
    assert isPrimelst([2, 7]) is True
    assert isPrimelst([4, 8, 6]) is False

def get_longest_all_primes(lst: list[int]):
    '''

    :param lst: o lista de numere intregi
    :return: subsecventa maxima in care toate numerele sunt prime

    '''
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if isPrimelst(lst[i:j + 1]) is True and (len(lst[i:j + 1]) > len(subsecventaMax)):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax

def test_get_longest_all_primes():
    assert get_longest_all_primes([2, 5, 7, 6, 8, 2, 7]) == [2, 5, 7]
    assert get_longest_all_primes([13, 11, 7, 2, 5, 8, 2, 3, 17]) == [13, 11, 7, 2, 5]


def main():

    list =[]
    while True:
        printMenu()
        optiune = input("dati optiunea: ")
        if optiune == '1':
            list = citire_termeni()
        elif optiune == '2':
            print(get_longest_sorted_asc(list))
        elif optiune == '3':
            print(get_longest_equal_int_real(list))
        elif optiune == '4':
            print(get_longest_all_primes(list))
        elif optiune == '5':
            break
        else:
            print("optiune gresita, reincercati!")

if __name__ == '__main__' :
    test_ordinecrescatoare()
    test_verificaree()
    test_get_longest_sorted_asc()
    test_get_longest_equal_int_real()
    test_isPrimelst()
    test_get_longest_all_primes()

    main()
