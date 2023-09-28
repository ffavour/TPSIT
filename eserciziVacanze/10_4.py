"""Scrivete una funzione di nome tronca che prenda una lista, la modifichi togliendo
il primo e l’ultimo elemento, e restituisca None. Esempio:
>> t = [1, 2, 3, 4]
>> tronca(t)
>> t
[2, 3]"""


def tronca(lista):
    l = lista[1:-1]
    return l


def main():
    t = [1, 2, 3, 4]
    print(tronca(t))


if __name__ == "__main__":
    main()
