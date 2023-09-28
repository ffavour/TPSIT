"""Esercizio 9.1. Scrivete un programma che legga il file words.txt e stampi solo le parole composte
da più di 20 caratteri (caratteri spaziatori esclusi)."""


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole


def trovaParoleLunghe(elenco_parole):
    listaParole = elenco_parole.split()
    paroleLunghe = []

    for elemento in listaParole:
        if len(elemento) > 20:
            paroleLunghe.append(elemento)

    return paroleLunghe


def main():
    parole = leggiFile()

    listaParoleLunghe = trovaParoleLunghe(parole)
    print("parole più lunghe di 20 caratteri:")
    for elemnto in listaParoleLunghe:
        print(elemnto)


if __name__ == "__main__":
    main()
