""". Due parole sono anagrammi se potete ottenerle riordinando le lettere di cui sono
composte. Scrivete una funzione di nome anagramma che riceva due stringhe e restituisca True se
sono anagrammi"""


def isAnagramma(stringa1, stringa2):
    lista1 = list(stringa1)
    lista2 = list(stringa2)

    if len(lista1) != len(lista2):
        return False

    lista1.sort()
    lista2.sort()

    return lista1 == lista2


def main():
    print(isAnagramma("anna", "nana"))


if __name__ == "__main__":
    main()
