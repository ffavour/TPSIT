"""Scrivete una funzione di nome ha_duplicati che richieda una lista e restituisca
True se contiene elementi che compaiono più di una volta. Non deve modificare la lista di origine."""


def ha_duplicati(lista):
    l = []
    for elemento in lista:
        if elemento in l:
            return True
        l.append(elemento)
    return False


def main():
    print(ha_duplicati([1, 2, 3, 4, 5, 1]))


if __name__ == "__main__":
    main()
