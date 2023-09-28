"""Scrivete una funzione che legga il file words.txt e crei una lista in cui ogni parola
è un elemento. Scrivete due versioni della funzione, una che usi il metodo append e una il costrutto
t = t + [x]. Quale richiede più tempo di esecuzione? Perché?
Soluzione: http: // thinkpython2. com/ code/ wordlist. py ."""


import time


def leggiFileAppend():
    file = open("file/words_eng.txt", "r")
    l = []

    for elemento in file:
        elemento = elemento[:-1]
        l.append(elemento)

    file.close()
    return l


def leggiFileConcatenazione():
    file = open("file/words_eng.txt", "r")
    l = []

    for elemento in file:
        elemento = elemento[:-1]
        l = l + [elemento]

    file.close()
    return l


def main():
    inizioAppend = time.time()
    lista1 = leggiFileAppend()
    fineAppend = time.time()

    inizioConcatenazione = time.time()
    lista2 = leggiFileConcatenazione()
    fineConcatenazione = time.time()

    # print(lista1)
    # print(lista2)

    tempoTotAppend = fineAppend - inizioAppend
    tempoTotConcatenazione = fineConcatenazione - inizioConcatenazione
    print(f"tempo impiegato da append: {tempoTotAppend} secondi")
    print(f"tempo impiegato da concatenazione: {tempoTotConcatenazione} secondi")



if __name__ == "__main__":
    main()
