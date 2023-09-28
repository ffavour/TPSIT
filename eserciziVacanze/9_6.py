"""Scrivete una funzione di nome alfabetica che restituisca True se le lettere di una
parola compaiono in ordine alfabetico (le doppie valgono). Quante parole “alfabetiche” ci sono?"""


def alfabetica(parola):
    for i in range(len(parola) - 1):
        if parola[i] > parola[i+1]:
            return False
    return True


def main():
    print(alfabetica("aabcd"))


if __name__ == "__main__":
    main()