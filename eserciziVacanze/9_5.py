"""Scrivete una funzione di nome usa_tutte che richieda una parola e una stringa di
lettere richieste e che restituisca True se la parola utilizza tutte le lettere richieste almeno una volta.
Quante parole ci sono che usano tutte le vocali aeiou? E aeiouy?"""


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole


def usa_tutte(parola, lettereRichieste):
    for lettera in lettereRichieste:
        if lettera not in parola:
            return False
    return True


def trovaParole(listaParole, lettere):
    paroleTrovate = []
    for parole in listaParole:
        parole = parole.lower()
        if usa_tutte(parole, lettere):
            paroleTrovate.append(parole)
    return paroleTrovate


def main():
    print(usa_tutte("buongiorno", "ordbhjs"))
    parole = leggiFile().split()

    l1 = trovaParole(parole, "aeiou")
    l2 = trovaParole(parole, "aeiouy")
    print(l1)
    print(l2)


if __name__ == "__main__":
    main()
