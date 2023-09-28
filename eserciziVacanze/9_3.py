"""Scrivete una funzione di nome evita che richieda una parola e una stringa di lettere
vietate, e restituisca True se la parola non contiene alcuna lettera vietata.
Modificate poi il programma in modo che chieda all’utente di inserire una stringa di lettere vietate, e
poi stampi il numero di parole che non ne contengono alcuna. Riuscite a trovare una combinazione
di 5 lettere vietate che escluda il più piccolo numero di parole?
"""
import itertools


def leggiFile():
    file = open("file/words.txt", "r")
    parole = file.read()
    file.close()

    return parole


def evita(parola, lettere_vietate):
    for lettera in lettere_vietate:
        if lettera in parola:
            return False
    return True


def paroleNonEvitate(listaP, lettere_vietate):
    listaOK = []
    for elemento in listaP:
        if evita(elemento, lettere_vietate):
            listaOK.append(elemento)
    return listaOK, len(listaOK)


def stampaLista(l):
    for elemento in l:
        print(elemento)


def trovaCombinazione(parole):
    combinazioni = itertools.combinations("abcdefghijklmnopqrstuvwxyz", 5)
    combinazioneMinima = ""

    for combinazione in combinazioni:
        lettere_vietate = "".join(combinazione)
        listaPOK, nParoleOK = paroleNonEvitate(parole, lettere_vietate)
        if nParoleOK > (len(parole) - nParoleOK):
            combinazioneMinima = lettere_vietate

    return combinazioneMinima


def main():
    print(evita("arancia", "sa"))
    lista_parole = leggiFile().split()

    stringa = input("inserire una stringa: ")
    print(f"elenco di parole non contenti \"{stringa}\": ")
    lista_paroleOK, n = paroleNonEvitate(lista_parole, stringa)
    stampaLista(lista_paroleOK)
    print("Combinazione minima di 5 lettere vietate:", trovaCombinazione(lista_parole))


if __name__ == "__main__":
    main()
