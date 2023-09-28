"""Scrivete una funzione di nome ordinata che prenda una lista come parametro e
restituisca True se la lista è ordinata in senso crescente, False altrimenti. Esempio:
>> ordinata([1, 2, 2])
True
>> ordinata(['b', 'a'])
False
"""


def ordinata(lista):
    return lista == sorted(lista)


def main():
    print(ordinata([1, 2, 2]))
    print(ordinata(['b', 'a']))


if __name__ == "__main__":
    main()
