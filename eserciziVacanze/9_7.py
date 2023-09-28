""". Questa domanda deriva da un quesito trasmesso nel programma radiofonico Car Talk (http: // www. cartalk. com/
content/ puzzlers ): “Ditemi una parola inglese con tre lettere doppie consecutive. Vi dò un paio di parole che
andrebbero quasi bene, ma non del tutto. Per esempio la parola “committee”, co-m-m-i-t-t-e-e. Sarebbe buona se non
fosse per la “i” che si insinua in mezzo. O “Mississippi”: M-i-s-s-i-s-s-i-p-p-i. Togliendo le “i” andrebbe bene. Ma
esiste una parola che ha tre coppie di lettere uguali consecutive, e per quanto ne so dovrebbe essere l’unica. Magari
ce ne sono altre 500, ma me ne viene in mente solo una. Qual è?” Scrivete un programma per trovare la parola.
Soluzione: http: // thinkpython2. com/ code/ cartalk1. py ."""


def leggiFile():
    file = open("file/words_eng.txt", "r")
    parole = file.read()
    file.close()

    return parole


def controlloDoppie(parola):
    cont = 0
    i = 0
    while i < (len(parola) - 1):
        if parola[i] == parola[i + 1]:
            cont += 1
            if cont == 3:
                return True
            i = i + 2
        else:
            i = i + 1
            cont = 0
    return False


def paroleCon3Doppie(listaParole):
    listaFinale = []
    for parola in listaParole:
        if controlloDoppie(parola):
            listaFinale.append(parola)
    return listaFinale


def main():
    parole = leggiFile().split()
    # print(parole)

    lDoppie = paroleCon3Doppie(parole)
    print(lDoppie)


if __name__ == "__main__":
    main()
