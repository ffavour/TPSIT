""". Scrivete una funzione di nome sed che richieda come argomenti una stringa modello, una stringa di sostituzione,
e due nomi di file. La funzione deve leggere il primo file e scriverne il contenuto nel secondo file (creandolo se
necessario). Se la stringa modello compare da qualche parte nel testo del file, la funzione deve sostituirla con la
seconda stringa. Se si verifica un errore in apertura, lettura, scrittura, chiusura del file, il vostro programma
deve gestire l’eccezione, stampare un messaggio di errore e terminare. Soluzione: http: // thinkpython2. com/ code/
sed. py"""


def leggiFile(nomeFile):
    try:
        file = open(nomeFile, "r")
        contenuto = file.read()
        file.close()
        return contenuto
    except IOError:
        print("errore nell'apertura del file")
        return


def scriviFile(nomeFile, stringa):
    try:
        file = open(nomeFile, "a")
        file.write(stringa)
        file.close()
    except IOError:
        print("errore nella creazione del file")
        return


def sed(stringaModello, stringaSostituzione, nomeFile1, nomeFile2):
    testo = leggiFile(nomeFile1)
    nuovo_testo = testo.replace(stringaModello, stringaSostituzione)
    scriviFile(nomeFile2, nuovo_testo)


def main():
    nomeFile1 = "file/testo.txt"
    nomeFile2 = "file/testo2.txt"
    stringaModello = "una"
    stringaSostituzione = "cielo"

    sed(stringaModello, stringaSostituzione, nomeFile1, nomeFile2)


if __name__ == "__main__":
    main()
