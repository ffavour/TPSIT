""" Scrivete una funzione di nome somma_nidificata che prenda una lista di liste di
numeri interi e sommi gli elementi di tutte le liste nidificate. Esempio:
>> t = [[1, 2], [3], [4, 5, 6]]
>> s"""


def somma_nidificata(lista_di_liste):
    somma = 0
    for lista in lista_di_liste:
        for elemento in lista:
            somma += elemento
    return somma


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(somma_nidificata(t))


if __name__ == "__main__":
    main()
