"""Nel 1939, Ernest Vincent Wright pubblicò una novella di 50.000 parole dal titolo
Gadsby che non conteneva alcuna lettera “e”. Dato che la “e” è la lettera più comune nella lingua
inglese, non è una cosa facile.
Infatti, in italiano non ho mai composto un piccolo brano siffatto: sono pochi i vocaboli privi tali da
riuscirci; finora non ho trovato alcun modo, ma conto di arrivarci in alcuni giorni, pur con un po’
di difficoltà! Ma ora, basta così.
Scrivete una funzione di nome niente_e che restituisca True se una data parola non contiene la
lettera “e”.
Modificate il programma del paragrafo precedente in modo che stampi solo le parole dell’elenco prive
della lettera “e”, e ne calcoli la percentuale sul totale delle parole."""


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole


def niente_e(parola):
    for lettera in parola:
        if lettera == "e" or lettera == "E":
            return False
            break

    return True


def paroleSenzaE(parole):
    listaParole = parole.split()
    parole_senza_e = []

    for elemento in listaParole:
        if niente_e(elemento):
            parole_senza_e.append(elemento)

    return parole_senza_e


def main():
    # print(niente_e("haaaaaaaaaaaaaaae"))
    parole = leggiFile()
    listaParoleNoE = paroleSenzaE(parole)
    print("parole senza e:")
    for elemento in listaParoleNoE:
        print(elemento)


if __name__ == "__main__":
    main()
