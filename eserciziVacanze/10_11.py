"""Una coppia di parole è “bifronte” se l’una si legge nel verso opposto dell’altra.
Scrivete un programma che trovi tutte le parole bifronti nella lista di parole. Soluzione: http:
// thinkpython2. com/ code/ reverse_ pair. py ."""


def bifronte(lista):
    l = []
    for elemento in lista:
        if elemento[::-1] in l:
            return True
        l.append(elemento)
    return False


def main():
    print(bifronte(["acetone", "casa", "enoteca"]))


if __name__ == "__main__":
    main()
