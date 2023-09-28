"""Scrivete una funzione di nome mediani che prenda una lista e restituisca una
nuova lista che contenga tutti gli elementi, esclusi il primo e l’ultimo. Esempio:
>> t = [1, 2, 3, 4]
>> mediani(t)
[2, 3"""


def mediani(lista):
    lFin = lista[1:-1]
    return lFin


def main():
    t = [1, 2, 3, 4]
    print(mediani(t))


if __name__ == "__main__":
    main()