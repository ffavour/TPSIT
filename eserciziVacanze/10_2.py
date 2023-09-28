"""Scrivete una funzione di nome somma_cumulata che prenda una lista di numeri
e restituisca la somma cumulata, cioè una nuova lista dove l’i-esimo elemento è la somma dei primi
i + 1 elementi della lista di origine. Per esempio:
>> t = [1, 2, 3]
>> somma_cumulata(t)
[1, 3, 6]"""


def somma_cumulata(lista):
    l = []
    somma = 0
    for numero in lista:
        somma += numero
        l.append(somma)

    return l


def main():
    t = [1, 2, 3]
    print(somma_cumulata(t))


if __name__ == "__main__":
    main()
